---
name: estudar
description: "Conduz uma SESSÃO DE ESTUDO de programação com método: diagnostica o que você já sabe, explica pelo mecanismo, passa exercício que VOCÊ roda, fecha com perguntas de recordação e registra o resultado numa fila de revisão espaçada no Cérebro. Tem três modos: aprender um tema, revisar o que venceu hoje e montar um roteiro de estudo para um objetivo ou projeto. Usa a trilha 70-aprendizado (Big-O, estruturas de dados, JavaScript, TypeScript, Python, SQL, Git, React, system design) como currículo. Use quando disser 'quero estudar X', 'me ensina X', 'não entendo direito como X funciona', 'me testa em X', 'o que tenho pra revisar hoje', 'revisão', 'monta um plano de estudo', 'o que devo aprender pra mexer no projeto Y', 'quero virar full stack'. NÃO use para resolver um bug ou entregar tarefa com pressa (aí é trabalho, não estudo), nem para reconstruir uma ferramenta inteira (construir-do-zero) ou treinar algoritmo em código real (algoritmos-na-pratica)."
---

# Estudar

Uma sessão de estudo que deixa rastro: você sai entendendo o mecanismo, com um exercício feito
por você e com a data da próxima revisão calculada.

**A ideia que sustenta tudo:** entender não é reconhecer. Ler uma explicação boa dá a
*sensação* de ter entendido. O que prova o entendimento é **recuperar da memória e usar**:
explicar sem consultar, resolver sem guia, responder dias depois. As três fontes da trilha
dizem isso por caminhos diferentes:

- O autor do coding-interview-university abre a lista de erros assim: assistiu a horas de vídeo,
  anotou tudo, e meses depois não lembrava de quase nada. A regra dele: resolver problema
  **enquanto** estuda cada tópico, não depois.
- O developer-roadmap manda refazer o projeto **2 a 3 vezes sem olhar** e depois construir um
  parecido, mas diferente.
- O freeCodeCamp retira o andaime aos poucos: aula → workshop guiado → **lab sem guia** com
  testes. Só o lab prova que aprendeu.

Por isso, nesta skill, **quem produz é a pessoa**: ela explica, escreve o código, responde as
perguntas. O Claude explica, pergunta, confere e registra.

---

## Onde as coisas moram

| O quê | Caminho |
|---|---|
| A trilha (o currículo) | `A:\Claude\02-cerebro\70-aprendizado\` |
| O mapa da trilha | `A:\Claude\02-cerebro\00-mapas\_MOC-aprendizado.md` |
| Formato de nota nova | `A:\Claude\02-cerebro\70-aprendizado\00-formato-das-notas.md` |
| Fila de revisão e diário | `A:\Claude\02-cerebro\70-aprendizado\90-progresso\progresso-estudos.md` |
| Motor da fila (datas) | `A:\Claude\01-agente-wat\Projeto 9 Claude Mestre Neutro\30-sistema\biblioteca-skills\16-aprendizado\estudar\scripts\revisao.py` |
| Roteiros por tecnologia | `A:\Claude\02-cerebro\70-aprendizado\60-carreira-e-comunidade\roteiros-developer-roadmap.md` |
| A escada de dicas | seção "Como usar o Claude sem terceirizar o aprendizado" de `A:\Claude\02-cerebro\70-aprendizado\50-construir-do-zero\construir-do-zero-metodo.md` |

Nos comandos abaixo, `REVISAO` é o caminho completo do `revisao.py`. Chame sempre com
`python "<caminho>"` — o caminho tem espaço.

---

## Primeiro: qual modo

Diga o modo numa linha antes de começar ("Modo aprender: complexidade Big-O"), para a pessoa
poder corrigir.

| O pedido soa como | Modo |
|---|---|
| "quero estudar X", "me ensina X", "não entendo X", "me testa em X" | **aprender** |
| "o que tenho pra revisar", "revisão de hoje", "me pergunta o que já estudei" | **revisar** |
| "o que devo estudar", "monta um plano", "o que preciso saber pra mexer no projeto Y" | **roteiro** |

Se a pessoa está no meio de uma entrega e o "estudar" é na verdade "resolve isso pra mim agora",
diga isso com franqueza, resolva o trabalho fora do modo estudo e ofereça registrar o tema no
diário para estudar depois.

---

## Modo aprender

**1. Achar a nota.** Procure o tema na trilha (Glob por nome em `70-aprendizado\**`, ou pelo
mapa). Achou: **leia a nota inteira antes de ensinar**. Ela é o currículo, e os exemplos e
números dela já foram conferidos rodando. Nota longa (manual de linguagem): combine com a pessoa
qual seção estudar hoje.

Não achou: diga que a trilha não cobre o tema, ensine a partir da documentação oficial e, no
fim, ofereça criar a nota seguindo o formato. Não crie sem a pessoa querer.

**2. Diagnóstico — dois minutos.** Peça que a pessoa explique com as próprias palavras o que já
sabe do tema, ou faça 2 perguntas da seção *Revisão rápida* da nota. Serve para não reensinar o
que ela domina e para achar a lacuna real. Critério para "já sabe": **explica o mecanismo sem
consultar e consegue usar num exercício**. Reconhecer o nome não conta.

**3. Um mecanismo por vez.** Explique uma ideia, curta, e mostre um exemplo pequeno que a
**pessoa roda** na máquina dela (Windows: PowerShell 5.1 ou Git Bash, Node 24, Python 3.10).
Prefira os exemplos da nota. Antes de rodar, peça que ela **preveja a saída**: a diferença entre
a previsão e o resultado é onde o aprendizado acontece. Ligue a um projeto real só quando a nota
tiver a seção *Nos seus projetos*: ligação inventada ensina errado.

**4. Exercício feito pela pessoa.** Escolha um da seção *Exercícios*, do mais fácil ao mais
difícil. A pessoa escreve o código. Se travar, suba **um degrau por pedido** da escada de dicas
(pergunta de volta → aponta o conceito → aponta o lugar → estrutura em pseudocódigo → trecho com
lacuna → solução só com pedido explícito). Confira rodando, nunca "de olho".

**5. Uma pegadinha.** Mostre uma da seção *Pegadinhas* e peça a previsão antes de rodar.

**6. Fechar com recuperação.** Faça de 4 a 8 perguntas da *Revisão rápida*, uma por vez, **sem
mostrar a resposta** e sem a pessoa consultar a nota. Corrija cada uma com a resposta da nota e
uma linha de mecanismo. Conte com honestidade: **resposta parcial conta como erro**, porque a
revisão existe para achar o que ainda não está firme.

**7. Registrar.** Só registre a nota quando as perguntas de revisão dela foram feitas. Se só uma
parte foi estudada, pergunte só daquela parte e escreva no diário, sem registrar a nota.

```bash
python "REVISAO" registrar <nome-da-nota> --acertos N --total M
python "REVISAO" diario "aprender · [[<nome-da-nota>]] · <o que firmou> / <o que falhou>"
```

Saída 1 do `registrar` quer dizer que a nota não existe na trilha (wikilink quebrado): avise.
Saída 2 é erro, e nada foi gravado: leia a mensagem e corrija.

Uma sessão boa dura de 25 a 60 minutos e cobre **uma** nota, ou uma seção de uma nota longa.

---

## Modo revisar

1. `python "REVISAO" pendentes`. Se nada venceu, diga quando vence a próxima e ofereça
   estudar o próximo item do roteiro da pessoa, se houver um em `90-progresso\plano-*.md`.
2. Pegue no máximo **4 notas** por sessão, as mais atrasadas primeiro. Revisão longa demais vira
   chute por cansaço.
3. Para cada nota: leia a *Revisão rápida*, faça as perguntas uma por vez, sem mostrar a
   resposta, e corrija quando errar (resposta da nota + uma linha de mecanismo).
4. Registre cada nota com `registrar`, e escreva uma linha só no diário para a sessão.
5. Nota que caiu para o **degrau 0** pede reestudo: ofereça uma sessão curta do modo aprender
   focada só nas perguntas que falharam.

**Por que a escada funciona:** acertar sobe um degrau e afasta a próxima revisão (1 → 3 → 7 →
14 → 30 → 60 dias); esquecer derruba para 1 dia. Cada revisão acontece perto do ponto em que a
lembrança começaria a falhar, que é quando recuperar custa esforço e por isso fixa. A regra
exata está explicada no próprio `progresso-estudos.md`.

---

## Modo roteiro

**Entrada:** um objetivo ("mexer no backend do Trindade", "full stack", "entender o React") ou
um projeto.

1. **Leia a base.** A seção "Percurso sugerido para você" de `roteiros-developer-roadmap.md`
   (ordem e checklists) e, se veio um projeto, os manifestos dele **só para leitura**
   (`package.json`, `pnpm-workspace.yaml`, `pyproject.toml`, `wrangler.*`) para listar a stack
   real. O roteiro sai do que o projeto usa, não de um currículo genérico.
2. **Diagnóstico por bloco, não por item.** As checklists têm centenas de subtópicos: não
   pergunte um por um. Para cada bloco relevante, faça 1 ou 2 perguntas de mecanismo. Quem marca
   "sei" é a pessoa, pelo critério do modo aprender.
3. **Monte o plano:**
   - a lista ordenada das notas da trilha a estudar (as que existem primeiro, conferidas por
     Glob), com a lacuna que cada uma cobre;
   - onde praticar sem guia: um lab do freeCodeCamp (`curriculo-freecodecamp.md`) ou um projeto
     de `50-construir-do-zero\`;
   - ritmo realista, combinado com a pessoa (ex.: 3 sessões de 45 min por semana);
   - **um checkpoint por semana**: construir algo pequeno sem passo a passo, depois refazer
     variando. É o formato de lab.
4. **Grave** `A:\Claude\02-cerebro\70-aprendizado\90-progresso\plano-<slug>.md` (frontmatter
   `tipo: plano`, `area: aprendizado`, data absoluta), com as notas como checklist em wikilink e
   a data de reavaliação do plano.
5. Linha no diário: `roteiro · [[plano-<slug>]] · <objetivo>`.

---

## O que vale nos três modos

- **Sem resposta antes da tentativa.** Entregar a solução pronta produz um programa que roda sem
  que ninguém tenha aprendido. A nota `comprehension-debt` do Cérebro mostra o custo disso ao
  longo do tempo.
- **Exemplo com saída afirmada foi rodado.** Se não deu para rodar, diga.
- **Lei zero do agente:** o que não deu para validar sai escrito "NÃO FOI POSSÍVEL VALIDAR." —
  nunca uma resposta inventada com cara de certa.
- **Nota da trilha não se edita durante a sessão** para "melhorar": se achar um erro nela, conte
  à pessoa e registre no diário. Correção de nota é trabalho separado, com fonte.

---

## Como saber que funcionou

**Modo aprender — passou se as quatro coisas são verdade:**
1. A pessoa rodou pelo menos um exemplo ou exercício **escrito por ela**.
2. As perguntas de revisão foram respondidas sem consultar, e a contagem foi honesta.
3. `python "REVISAO" registrar` saiu com código 0, e a nota aparece em `python "REVISAO" fila`.
4. O diário em `progresso-estudos.md` tem a linha da sessão com a data de hoje.

**Modo revisar — passou se:** toda nota que estava em `pendentes` e foi revisada tem registro
novo, e rodar `pendentes` de novo não a lista mais.

**Modo roteiro — passou se:** `plano-<slug>.md` existe, cada wikilink de nota do plano aponta
para um arquivo que existe na trilha, e o plano tem pelo menos um checkpoint sem guia.

Falhou em qualquer item: diga qual, em vez de declarar a sessão concluída.
