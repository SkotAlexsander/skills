---
name: algoritmos-na-pratica
description: "Acha e conserta custo algorítmico ruim em código REAL — laço dentro de laço, includes/indexOf/find/filter dentro de laço, shift() ou pop(0) em fila, cópia de array a cada iteração, ordenação repetida, recursão que recalcula, uma consulta ao banco por item (N+1), estrutura de dados errada — MEDINDO antes e depois com tamanhos crescentes e provando que o resultado não mudou. Também treina resolução de problemas de algoritmo com o método de 6 passos e dica graduada, sem entregar a resposta pronta. Use quando disser 'isso tá lento', 'trava com muitos itens', 'demora quando a lista cresce', 'otimiza esse loop', 'qual a complexidade disso', 'Big-O', 'Map ou objeto', 'Set ou array', 'qual estrutura de dados usar', 'quero treinar algoritmo', 'exercício de lógica', 'leetcode'. NÃO use para renderização lenta, rede ou Core Web Vitals (performance-optimization), animação travando (optimize-web-animations) nem consulta SQL lenta por falta de índice (sql-database-assistant)."
---

# Algoritmos na prática

Dois usos da mesma base: **consertar** código que fica lento quando os dados crescem, e
**treinar** a resolução de problemas.

**A ideia que manda aqui: análise é hipótese, medição é evidência.** Ler o código e dizer "isso
é O(n²)" é um palpite bem informado; dobrar o tamanho da entrada e ver o tempo quadruplicar é a
prova. E o contrário também vale: **saber o n real decide se vale mexer.** O `gateway.ts` do
Trindade tem o comentário certo: "Com cinco pessoas e talvez quinze conexões, percorrer o mapa
inteiro num broadcast custa nada — não invente índice por canal antes de precisar." Saber o custo,
saber o n e decidir não otimizar é uso maduro de Big-O.

---

## A base (leia a parte que a situação pedir)

| Nota | Para quê |
|---|---|
| `A:\Claude\02-cerebro\70-aprendizado\10-fundamentos\complexidade-big-o.md` | Como estimar lendo código, o custo dos métodos embutidos de JS e Python, e **como medir** (seções 7 e 8) |
| `...\10-fundamentos\estruturas-de-dados.md` | Tabela de custos e "qual escolher, na prática" em JS e Python |
| `...\10-fundamentos\paradigmas-de-algoritmo.md` | Os padrões (dois ponteiros, janela, prefix sum, hash) e a tabela "sinais no enunciado" |
| `...\10-fundamentos\ordenacao-e-busca.md` · `arvores-e-grafos.md` | Quando o problema é ordenar, buscar, caminho ou dependência |
| `...\60-carreira-e-comunidade\entrevista-tecnica.md` | O método de 6 passos e a ordem de tópicos para treino |

(`...` = `A:\Claude\02-cerebro\70-aprendizado`.)

---

## Modo A — código real está lento

### 1. Confirmar que o problema é de crescimento

Pergunte: **fica mais lento conforme os dados crescem?** Se uma requisição é lenta com poucos
dados, o gargalo provavelmente é rede, disco, banco ou renderização, e esta skill não é a
ferramenta: diga isso e aponte a certa. Descubra o **n real** (quantos itens, usuários, arquivos,
mensagens), hoje e no pior caso plausível.

**Separe as dimensões limitadas das que crescem com o tempo.** Procure o limite no próprio código:
validação (`z.array(...).max(6)`), constante compartilhada, tamanho do grupo. Dimensão limitada por
regra dá custo **constante**, por mais aninhado que o laço pareça. A que pesa é a que **acumula
sem teto**: histórico, mensagens, registros de uma consulta sem `limit`. No teste real desta skill
(13/09/2026, enquetes do Trindade), opções (≤ 6) e pessoas (5) eram limitadas; o número de
enquetes de um canal não era, e era ele que tornava a listagem quadrática.

### 2. Medir antes

Isole a função suspeita e rode com dados sintéticos em **pelo menos três tamanhos dobrando**
(n, 2n, 4n). A razão entre os tempos dá a classe:

| Dobrou n e o tempo… | Classe provável |
|---|---|
| ficou igual | O(1) ou O(log n) |
| dobrou | O(n) |
| pouco mais que dobrou | O(n log n) |
| quadruplicou | O(n²) |

Node: use a mediana de 5 execuções com `performance.now()` (o modelo está na seção 8 de
`complexidade-big-o.md`). Python: `timeit`. Sem saber onde está o gasto, perfile primeiro:
`node --cpu-prof arquivo.js` gera um `.cpuprofile` que o DevTools do Chrome abre, e
`python -m cProfile -s cumtime script.py` lista as funções pelo tempo acumulado.

### 3. Ler e estimar

Regras: passos em sequência **somam** (fica o maior); laços aninhados **multiplicam**; laço que
corta pela metade é **log**; recursão se analisa desenhando a árvore de chamadas; **método
embutido não é grátis**. Nomeie as variáveis de verdade: laço sobre usuários dentro de laço
sobre mensagens é O(u·m), não "O(n²)".

### 4. Caçar os sinais

| Sinal no código | Por que custa | Troca típica |
|---|---|---|
| `includes`/`indexOf`/`find`/`some` dentro de laço (JS) · `x in lista` dentro de laço (Py) | cada consulta percorre a lista: O(n·m) | montar um `Set`/`Map` (`set`/`dict`) **uma vez** antes do laço |
| `filter` dentro de `map` | O(a·b) | agrupar numa passada com `Map` (ou `Map.groupBy`, presente no Node 24) |
| `[...acc, x]`, `concat` ou `{...obj}` dentro de `reduce`/laço | copia tudo a cada item: O(n²) | acumulador local mutado com `push` ou atribuição |
| `shift()`/`unshift()` (JS) · `pop(0)`/`insert(0, x)` (Py) | move todos os outros: O(n) cada | índice de cabeça · `collections.deque` |
| `sort` dentro de laço, ou ordenar só para pegar o menor | O(n log n) repetido | uma passada, ou heap (`heapq`; em JS, heap próprio) |
| recursão que recalcula o mesmo subproblema | exponencial | memoização ou tabulação (ver as pegadinhas abaixo) |
| uma consulta ao banco por item (N+1) | cada passo custa milissegundos, não nanossegundos | uma consulta em lote + `Map` para achar cada resultado (padrão de `messages.db.ts` do Trindade) |

### 5. Propor a menor mudança que resolve

Diga a complexidade **antes e depois** e o custo de memória da troca: `Set` e `Map` compram tempo
com memória O(n). Não reescreva o módulo: troque a estrutura ou o laço.

### 6. Provar que o comportamento não mudou

Rode os testes que existirem. Se não houver, escreva uma **checagem de equivalência**: a função
antiga e a nova recebem os mesmos dados aleatórios e os mesmos casos de borda (vazio, um item,
duplicados, ordem), e as saídas precisam ser iguais. Isso existe porque as trocas desta tabela
mudam semântica em silêncio. `Set` compara objetos por **referência**, trata `NaN` como igual a
`NaN` e preserva a ordem de inserção. `dict` e `set` exigem chave imutável. Agrupar pode mudar a
ordem da saída.

### 7. Medir depois

Mesmo roteiro, mesmos tamanhos. Entregue a tabela `n | antes | depois | razão` e a explicação da
razão pela complexidade.

### 8. Decidir com o n real

Se o n real é pequeno e o ganho não se sente, **recomende não mudar** e diga por quê. Vale deixar
um comentário no código com o custo e o n, como o `gateway.ts` faz: vira decisão registrada, não
descuido.

Dois fatores mudam a régua:

- **Onde o código roda.** Num servidor Node, CPU gasta num laço **bloqueia o event loop**: enquanto
  o `filter` roda, nenhuma outra requisição nem mensagem de WebSocket é atendida, de ninguém. Meça
  contra esse orçamento (dezenas de milissegundos já atrasam o tempo real de todos), não só contra
  a paciência de quem clicou. No navegador, o mesmo vale para a thread de interface.
- **Quanto a troca custa.** Se a dimensão cresce sem teto, a correção é pequena, local e tem
  equivalência provada, dá para recomendar a troca **sem urgência**, dizendo em que n ela passa a
  doer. Se a correção é grande, espere a medição de produção pedir.

### Pegadinhas deste modo

- **Big-O ignora constantes, e o usuário não.** Para n pequeno, meça em vez de supor.
- **"O(1)" de hash é média.** Hash ruim leva tudo para o mesmo balde.
- **Memoização em JS com chave de array não funciona:** `memo.get([i, j])` compara referência e
  nunca acha. Use `` `${i},${j}` ``.
- **Recursão com cache ainda estoura a pilha.** O Python 3.10 para em 1.000 chamadas por padrão;
  tabule de baixo para cima.
- **Medir uma vez só.** A primeira execução no Node inclui o aquecimento do JIT; use mediana.

---

## Modo B — treinar

1. **Escolha o tópico.** Na ordem do coding-interview-university (complexidade → arrays, listas,
   pilha, fila, hash → busca binária → árvores e heap → ordenação → grafos → recursão e
   programação dinâmica), ou pelo ponto fraco que aparece no diário de
   `A:\Claude\02-cerebro\70-aprendizado\90-progresso\progresso-estudos.md`.
2. **Dê um problema pequeno e claro**, em JavaScript ou Python, como a pessoa preferir.
3. **A pessoa conduz os 6 passos**; o Claude faz a pergunta de cada um:
   1. *Esclarecer:* "qual o tamanho de n? pode ter repetido, negativo, vazio?"
   2. *Exemplos:* "monte um normal e dois de borda, e resolva à mão."
   3. *Força bruta:* "qual a solução óbvia, e qual a complexidade dela?"
   4. *Otimizar:* "que trabalho a força bruta repete? que estrutura ou padrão elimina?" — e a
      nova complexidade **antes** de codar.
   5. *Codar* narrando.
   6. *Testar:* percorrer à mão com o exemplo, depois as bordas, e repetir tempo e espaço.
4. **Travou:** um degrau por pedido da escada de dicas (pergunta de volta → aponta o conceito →
   aponta o lugar → pseudocódigo → trecho com lacuna → solução só com pedido explícito). A escada
   completa está em `...\50-construir-do-zero\construir-do-zero-metodo.md`.
5. **Depois de resolver:** compare com a tabela "sinais no enunciado" e proponha **uma variação**
   do mesmo problema. Refazer variando prova que entendeu e não decorou.
6. **Registre** uma linha no diário com o script da skill `estudar` (`revisao.py diario "..."`) e,
   se o treino cobriu as perguntas de revisão de uma nota da trilha, registre a nota também.

**Por que resolver durante o estudo, e não depois:** o autor do coding-interview-university
aprendeu isso do jeito caro: horas de vídeo e anotação, e meses depois não lembrava. A regra
dele é 2 ou 3 problemas ao terminar cada tópico, e voltar ao tópico mais tarde.

---

## Como saber que funcionou

**Modo A — passou se todas são verdade:**
1. Houve medição **antes e depois** em pelo menos 3 tamanhos, com a tabela entregue.
2. A razão observada foi explicada pela complexidade.
3. A checagem de equivalência (ou os testes existentes) passou, incluindo casos de borda.
4. Ou então: a recomendação foi **não mudar**, com o n real e o custo medido como argumento.

**Modo B — passou se:** a solução foi escrita pela pessoa, a complexidade foi dita antes de
codar, e pelo menos dois casos de borda foram testados rodando.
