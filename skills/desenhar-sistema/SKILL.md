---
name: desenhar-sistema
description: "Aplica o método do System Design Primer a um projeto REAL, na escala verdadeira dele: levanta casos de uso, o que fica fora e as suposições; estima carga com contas à vista (usuários → requisições/s → armazenamento → banda); desenha em alto nível; detalha fluxos, dados e API; e só então decide banco, cache, fila, consistência e ponto único de falha, cada decisão com critério, trade-off e o que faria mudar. Entrega um documento de design. Use quando disser 'como eu estruturo esse sistema', 'qual arquitetura', 'isso aguenta X usuários?', 'preciso de fila/cache/Redis?', 'SQL ou NoSQL', 'vou pôr no ar, o que pode cair?', 'um servidor dá conta?', 'desenha a arquitetura do app', ou antes de começar backend, API, realtime, bot com servidor ou app com banco. NÃO use para layout de tela e UX (front_god, ux-audit), para decisão já tomada que só precisa ser registrada (documentation-and-adrs) nem para schema de tabela isolado (database-schema-designer)."
---

# Desenhar sistema

O roteiro que leva de "quero um sistema que faça X" a um desenho **justificado por números**, e
não por moda.

**A ideia central do primer cabe numa frase: tudo é trade-off.** E só dá para escolher o
trade-off certo depois de saber o tamanho do problema. Por isso a ordem não se negocia: primeiro
"fazendo o quê, para quantos", depois as peças. Pular direto para "põe um Redis e uma fila"
entrega peças que ninguém mediu, e cada peça é mais uma coisa que cai e que alguém precisa operar.

**O método vale para cinco usuários ou para cem milhões — o resultado é que muda.** Num projeto
pequeno, a resposta correta muitas vezes é "uma máquina só, com backup testado". O primer manda
tratar os gargalos das *suas* restrições; copiar a arquitetura de um Twitter para um grupo de
amigos trai o próprio método.

---

## Leia antes (a base desta skill)

| Nota | Para quê |
|---|---|
| `A:\Claude\02-cerebro\70-aprendizado\30-system-design\system-design-como-abordar.md` | **O método inteiro**, a estimativa do Pastebin e a calculadora em Python. Leia sempre |
| `...\30-system-design\numeros-de-referencia.md` | Ordens de grandeza para estimar (com as ressalvas de época) |
| `...\30-system-design\estudo-de-caso-trindade.md` | O método aplicado a um projeto real e pequeno: o modelo de saída |
| `...\30-system-design\desempenho-escala-disponibilidade.md` | CAP, consistência, disponibilidade em "noves" |
| `...\30-system-design\bancos-de-dados-em-escala.md` | Replicação, sharding, SQL ou NoSQL |
| `...\30-system-design\cache-estrategias.md` | Onde cachear, cache-aside e cia., invalidação |
| `...\30-system-design\filas-e-assincronismo.md` | Filas de mensagem e de tarefa, back pressure |
| `...\30-system-design\dns-cdn-balanceador-proxy.md` e `comunicacao-http-tcp-rpc-rest.md` | Borda e comunicação |

(`...` = `A:\Claude\02-cerebro\70-aprendizado`.) Leia as notas de decisão **quando a decisão
aparecer**, não todas de uma vez.

---

## Passo 0 — projeto que existe ou projeto novo?

**Existe:** leia primeiro, **só leitura**, o que o projeto já decidiu: `README`, `docs/`, e os
arquivos que denunciam a arquitetura (`docker-compose.yml`, `wrangler.*`, `package.json`,
`pnpm-workspace.yaml`, `Caddyfile`, migrations). No documento, separe sempre:

- **Doc:** está escrito no arquivo citado.
- **Análise:** é conclusão sua, com a conta ou o raciocínio à vista.

Sem essa separação, a pessoa não sabe o que é fato do projeto e o que é opinião.

**Doc é o que o arquivo afirma, não o que é verdade.** Afirmação que sustenta uma decisão se
confere na fonte oficial. No teste real desta skill (Bene, 13/09/2026), um comentário do código
dizia que `cache-control: max-age=60` "tira a maior parte da carga do D1"; a documentação da
Cloudflare mostra que resposta gerada pelo Worker não é guardada pela CDN sem a Cache API. O cache
valia só para o navegador de quem pediu.

**Novo:** siga direto para o passo 1.

---

## Passo 1 — casos de uso, fora do escopo, suposições

- **Casos de uso como ator + ação.** "**Paciente** encontra terapeuta perto dele sem criar
  conta." Inclua o ator **Serviço** ("Serviço apaga convites vencidos", "Serviço faz backup"): o
  trabalho que ninguém clica gera carga e ponto de falha tanto quanto o usuário.
- **Fora do escopo, por escrito, com o porquê de cada corte.** Cortar faz parte do desenho.
- **As perguntas:** quem usa? como? quantos hoje, e em que horizonte (diga o horizonte: 12
  meses)? o que entra e o que sai? quanto dado? quantas requisições por segundo? qual a proporção
  leitura:escrita? qual o fator de pico sobre a média? **o que acumula com o tempo, e por quanto
  tempo fica guardado?** Histórico com retenção longa cresce mesmo com o número de usuários parado.
- **Qualidades como frases testáveis:** "abrir o link deve levar menos de 1 s", "perder a
  conversa de hoje se o PC cair é aceitável", "custo mensal máximo de R$ X", "quem opera é uma
  pessoa, sem plantão". Para projeto pequeno, **custo e esforço de operação são restrições de
  primeira classe**: muitas vezes decidem mais que a carga.
- **Número desconhecido:** pergunte. Se a pessoa também não sabe, assuma com faixa (otimista e
  pessimista) e marque **SUPOSIÇÃO**. Número sem suposição escrita não pode ser refeito quando a
  realidade mudar.

## Estimativa de guardanapo

Roteiro: **usuários → requisições/s → armazenamento → banda.** Contas à vista, sempre.

- 1 mês ≈ 2,5 milhões de segundos (atalho do primer; o valor exato erra uns 3,5%, o que não muda
  decisão). Logo: 1 req/s ≈ 2,5 M/mês · 40 req/s ≈ 100 M/mês · 400 req/s ≈ 1 bilhão/mês.
- Armazenamento = tamanho de um item (some os campos) × itens por mês × horizonte.
- Banda = requisições/s × bytes por resposta × 8.
- Dimensione pelo **pico**, e declare o fator usado.
- A calculadora em Python está na nota do método; use-a para refazer com outros números.

**Em serverless ou em plano gratuito, estime na unidade que o provedor cobra e limita**, não só
em requisições por segundo: linhas lidas por consulta, milissegundos de CPU por requisição,
invocações por dia. Confira esses limites na documentação oficial e anote a data. Havendo
emulador local que devolve a métrica, **meça em vez de estimar**: o `getPlatformProxy` do
`wrangler` expõe `meta.rows_read` de cada consulta D1. No teste com o Bene, o tráfego era
irrelevante (0,6 req/s no cenário alto), e o que derrubava o app era uma subconsulta que relia o
histórico inteiro a cada busca: 7 buscas por dia esgotavam a cota do D1 gratuito.

**O objetivo da estimativa é achar o único número grande** — e, igualmente, descobrir que as
outras peças não precisam de nada. No Trindade, o número grande é a banda de vídeo; o banco é
irrelevante na escala do grupo. Estimativa que serviu para *não* acrescentar peça cumpriu o papel.

## Passo 2 — desenho de alto nível

Caixas e setas em bloco de texto, com **toda** peça importante, e uma frase de justificativa por
peça ligada a algo do passo 1. Se a proporção leitura:escrita for desequilibrada, separe já os
caminhos de leitura e de escrita: é o que depois deixa escalar cada um no seu ritmo.

## Passo 3 — componentes centrais

- Cada caso de uso vira um **fluxo numerado** (quem chama quem, o que grava onde).
- **Modelo de dados:** tabelas ou coleções, chaves, índices, e o que vai para object store em
  vez de para o banco (conteúdo pesado no storage, só a chave no banco).
- **O algoritmo que é o coração do problema**, se houver (geração de link curto, fan-out,
  deduplicação, presença).
- **API:** REST para fora, RPC entre serviços internos, WebSocket quando o servidor precisa
  empurrar dado.

## Passo 4 — gargalos e decisões

O ciclo é **medir → achar o gargalo → tratar pesando alternativas → repetir**. Em projeto novo,
sem nada para medir, escreva *qual medição* dispararia cada mudança.

As decisões que sempre aparecem, com a pergunta que decide cada uma. A coluna "ponto de partida"
é o **degrau 1 da escada do `scaling_aws`**, a solução do primer que sobe de 1 usuário a
milhões uma peça por vez. É julgamento, não lei: mude quando o passo 1 disser outra coisa.

| Decisão | A pergunta que decide | Ponto de partida em projeto pequeno |
|---|---|---|
| Banco | Há relações e transações? Quanto dado, crescendo quanto? | Um banco relacional (Postgres ou SQLite/D1) |
| Cache | A leitura domina? O dado tolera ficar N segundos velho? Quem invalida? | Nenhum. Antes de Redis, cache HTTP e o cache do próprio banco |
| Fila | O trabalho pode acontecer depois? O pico passa da capacidade? O que acontece se falhar no meio? | Sem fila; tarefa no processo, com retentativa e idempotência |
| Consistência | O que dá errado se duas pessoas lerem versões diferentes? | Forte onde há dinheiro ou permissão; eventual no resto |
| Ponto único de falha | Se esta peça cair, o que para e por quanto tempo? O requisito aceita? | Aceitar, documentar e ter backup **restaurado em teste** |
| Escala | Uma máquina aguenta o pico × fator declarado? | Vertical primeiro; horizontal só com número |

Para cada decisão, registre: **escolha · por quê · o trade-off aceito · o que faria mudar.** A
última coluna é a mais valiosa: transforma o design num documento que avisa quando envelheceu.

**Escada de escala:** escreva 2 ou 3 degraus no formato *medição que dispara → peça que entra*.
Nenhuma peça entra sem a medição dela.

**O que o método mandaria NÃO fazer agora:** liste. Kubernetes, microserviços, sharding,
multi-região, fila "por precaução". Com o porquê, na escala real.

---

## O documento de saída

Onde o projeto guarda decisões (`docs/`), como `docs/design-<tema>.md`. Se não houver `docs/`,
pergunte onde gravar. Decisão isolada que merece registro formal combina com a skill
`documentation-and-adrs`.

```markdown
# Design: <sistema> — AAAA-MM-DD

## 1. Casos de uso, fora do escopo e suposições
## 2. Estimativa (as contas, com as suposições marcadas)
## 3. Desenho de alto nível (diagrama + justificativa de cada peça)
## 4. Componentes centrais (fluxos, modelo de dados, API)
## 5. Decisões (tabela: decisão | escolha | por quê | trade-off | o que faria mudar)
## 6. Escada de escala (medição → peça)
## 7. O que não fazer agora, e por quê
## 8. Riscos e o que ficou sem validar
```

A seção 8 é obrigatória mesmo quando está vazia. O que não deu para validar sai escrito
**"NÃO FOI POSSÍVEL VALIDAR."**, nunca como fato.

---

## Pegadinhas que esta skill existe para evitar

- **Dimensionar pela média.** Quem derruba o servidor é o pico.
- **Número sem suposição escrita.** Não dá para refazer a conta quando a realidade mudar.
- **Esquecer o ator Serviço:** backup, limpeza e lembrete também caem e também custam.
- **Copiar os números de latência como verdade de hoje.** São ordens de grandeza de uma época;
  a nota `numeros-de-referencia` diz qual e onde a cópia do primer diverge da origem.
- **Pseudocódigo do primer copiado como código.** O exemplo de cache-aside dele monta SQL com
  `.format()`, o que abre injeção de SQL. Consulta parametrizada, sempre.

---

## Como saber que funcionou

Passou se **todas** são verdade:

1. Toda peça do diagrama tem justificativa ligada a um caso de uso, a um número ou a uma
   restrição do passo 1.
2. A estimativa mostra as contas, e cada número tem a suposição escrita ao lado.
3. Cada decisão da seção 5 tem trade-off **e** "o que faria mudar".
4. Existe a lista do que não fazer agora.
5. Em projeto existente, Doc e Análise estão separados, e cada Doc cita o arquivo.
6. Nenhum número apareceu sem fonte ou sem marca de SUPOSIÇÃO.

Faltou algum: diga qual antes de entregar.
