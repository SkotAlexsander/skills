---
name: construir-do-zero
description: "Guia a reconstrução de uma tecnologia do zero para entendê-la por dentro — Git, React, servidor HTTP, motor de template, navegador, compilador — partindo de uma dúvida real: define o recorte mínimo e o que fica de fora, escolhe um tutorial conferido do catálogo build-your-own-x, fatia em marcos que rodam, cada um com teste, e faz VOCÊ escrever o código enquanto o Claude explica, revisa e dá dica graduada. Fecha comparando com a ferramenta real e com uma nota de aprendizado no Cérebro. Use quando disser 'quero entender como o X funciona por dentro', 'bora construir meu próprio X', 'build your own X', 'quero fazer um mini git/react/servidor', 'projeto de estudo', 'aprender fazendo', ou para retomar: 'continua o projeto do zero', 'próximo marco'. NÃO use para construir produto de cliente (front_god, fundacao-app-web), para estudar lendo um repositório existente (ler-repositorio) nem para exercício curto de algoritmo (algoritmos-na-pratica)."
---

# Construir do zero

> *What I cannot create, I do not understand.* — escrito por Richard Feynman no quadro-negro
> dele no Caltech (foto de 1988, Caltech Archives `1.10-29`), e frase de abertura do
> build-your-own-x.

Usando uma ferramenta, você aprende a **interface**. Reconstruindo, você é obrigado a tomar as
decisões que ela esconde: onde o Git guarda os arquivos, como o React sabe o que mudar no DOM,
como o servidor sabe onde termina o cabeçalho. Cada decisão que dá errado mostra uma lacuna exata
no seu modelo mental. Ler não produz esse sinal.

**Por isso a regra desta skill é uma só: o Claude ensina e revisa, a pessoa escreve.** Se o Claude
escreve o código, sobra um programa que roda e ninguém que entendeu — e o critério do Feynman
não é cumprido.

---

## A base

| O quê | Caminho |
|---|---|
| **O método em 7 passos, a escada de dicas e o papel do Claude** | `A:\Claude\02-cerebro\70-aprendizado\50-construir-do-zero\construir-do-zero-metodo.md` — leia sempre |
| O catálogo filtrado (JS, TS, Python) | `...\50-construir-do-zero\construir-do-zero-catalogo.md` |
| Os projetos já planejados, com marcos e tutorial conferido | `...\50-construir-do-zero\projeto-*-do-zero.md` |
| A fonte | `...\01-fontes\repo-build-your-own-x.md` |
| Onde o código de estudo mora | `A:\Claude\05-estudos\<projeto>-do-zero\` (ver `A:\Claude\05-estudos\LEIA-ME.md`) |
| Fila de revisão | script `revisao.py` da skill `estudar` |

(`...` = `A:\Claude\02-cerebro\70-aprendizado`.)

---

## Começar um projeto novo

**1. A dúvida real, escrita como pergunta.** "Quero aprender compiladores" é vago demais para
virar projeto. "Como o Vite transforma o meu JSX em JavaScript?" dá recorte. Peça a pergunta à
pessoa; se ela não tiver, ofereça as do quadro "Você usa / Ao reconstruir, é obrigado a decidir"
da nota do método.

**2. Escolher o projeto.**
- Existe `projeto-<x>-do-zero.md` que responde à pergunta? **Leia a nota inteira.** Ela já traz
  os marcos, o tutorial com link conferido e os pré-requisitos.
- Não existe: procure no catálogo e, se preciso, no README do build-your-own-x. Aplique o
  critério do próprio repositório: o tutorial **constrói do zero** e tem **caminho guiado**. Se
  começa com `npm install` de bibliotecas que fazem a parte difícil, ensina a API delas, não o
  mecanismo. Confira que o link abre (`curl -sIL -o /dev/null -w "%{http_code}" <url>`) e leia a
  data e os avisos do tutorial: tutorial velho sem aviso ensina um mecanismo que mudou.
- Confira os pré-requisitos com a pessoa. Faltando base, ofereça uma sessão de `/estudar` antes.

**3. Recorte mínimo e "fora do escopo".** A menor versão que ainda responde à pergunta, e uma
lista escrita com **pelo menos 4 itens** que ficam de fora ("sem packfiles, sem merge, sem
rede"). Sem essa lista o projeto cresce até ser abandonado. O recorte é contrato.

**4. Marcos que rodam.** No máximo 6 na primeira versão. Cada marco termina em **algo que se
executa**, cabe em 1 a 2 horas e tem **um teste**: um comando e a saída esperada (`node --test`,
`python -m unittest`, um `curl` com a resposta esperada). "Escrever o parser" não é marco; "o
programa recebe `(add 2 3)` e imprime a lista de tokens" é.

**5. Montar a pasta.** Em `A:\Claude\05-estudos\<projeto>-do-zero\`:

```
README.md     a pergunta, o recorte, a lista "fora do escopo", os marcos como checklist
DIARIO.md     1 a 3 linhas por sessão: tentei / travou em / entendi / degrau de dica usado
src/
testes/       um arquivo de teste por marco
comparar/     script que roda a sua versão e a ferramenta real com a mesma entrada
```

e `git init` dentro dela. O histórico de commits vira o registro do aprendizado.

---

## Cada marco — o laço

1. **Explicar o conceito do marco**, curto, e apontar a seção do tutorial. A pessoa lê e
   **fecha a aba** antes de escrever.
2. **O teste primeiro, ou junto.** "Pronto" quer dizer que o teste passa, não que "parece
   funcionar".
3. **A pessoa escreve o código.** Travou: suba **um degrau por pedido** e pare quando destravar:
   1. pergunta de volta ("o que você espera que aconteça nessa linha? o que acontece?");
   2. aponta o conceito;
   3. aponta o lugar;
   4. estrutura em pseudocódigo, sem código da linguagem;
   5. trecho com a parte central em branco;
   6. solução **só com pedido explícito** — e aí a pessoa apaga e reescreve de memória no dia
      seguinte.
4. **Rodar o teste** e mostrar a saída. Depois **revisar** o código escrito: apontar o problema e
   o porquê, sem reescrever "do jeito certo".
5. **Comparar com a ferramenta real** quando o marco permitir: mesma entrada nas duas, incluindo
   casos de borda (arquivo vazio, UTF-8, entrada grande, objeto que não existe). A ferramenta
   real é a especificação.
6. **Registrar:** marcar o marco no `README.md`, 1 a 3 linhas no `DIARIO.md` (inclua o degrau de
   dica mais alto usado) e sugerir o commit `marco N: <o que passou a funcionar>`. Fazer o commit
   pela pessoa, só se ela pedir.

## Retomar

Leia o `README.md` (checklist de marcos) e as últimas linhas do `DIARIO.md` da pasta, diga em que
marco a pessoa está e o que travou da última vez, e siga o laço.

---

## Fechar

**A nota de aprendizado** — sem ela, em três semanas sobra "fiz um Git uma vez". Grave em
`A:\Claude\02-cerebro\70-aprendizado\50-construir-do-zero\aprendi-<projeto>.md`, no formato de
nota de estudo (`A:\Claude\02-cerebro\70-aprendizado\00-formato-das-notas.md`), escrita com as
palavras da pessoa, respondendo:

- a pergunta do início, respondida;
- o que surpreendeu (o que ela achava que era, e não era);
- o que a ferramenta real faz diferente, e por quê;
- o que ficou de fora e seria o próximo marco.

A seção *Revisão rápida* dessa nota recebe essas mesmas quatro respostas como perguntas. Depois:

1. acrescente a nota ao mapa `A:\Claude\02-cerebro\00-mapas\_MOC-aprendizado.md`;
2. faça as perguntas, sem consulta, e registre:
   `python "<caminho do revisao.py>" registrar aprendi-<projeto> --acertos N --total M`.

Projeto abandonado no marco 3 **com** nota vale mais que projeto completo sem nota. Se a pessoa
parar no meio, feche assim mesmo.

---

## Pegadinhas

- **Recorte grande demais.** O *Web Browser Engineering* tem 16 capítulos; começar decidido a
  fazer todos é o jeito mais comum de abandonar.
- **"Rodou" não é "entendi".** Se a pessoa não consegue explicar por que funciona, faltou o
  passo 5 ou falta a nota.
- **Testar só o caminho feliz.** A comparação com a ferramenta real precisa dos casos de borda.
- **Generalizar cedo.** Plugin, configuração e "suporte a tudo" matam o projeto.
- **Rodar o código do tutorial sem ler.** Baixar o ZIP e executar é rodar código de terceiro.
  Leia antes, e só depois de ter escrito a própria versão.
- **Pasta de estudo dentro de projeto de cliente ou do repo do agente.** Estudo tem casa própria.

---

## Como saber que funcionou

Passou se **todas** são verdade:

1. A pasta do projeto tem `README.md` com pergunta, recorte, fora do escopo (4+ itens) e marcos.
2. Todo marco marcado como feito tem uma execução de teste passando, mostrada na sessão.
3. O código foi escrito pela pessoa: o `DIARIO.md` registra o degrau de dica mais alto usado, e o
   degrau 6 só aparece com pedido explícito.
4. A comparação com a ferramenta real rodou pelo menos uma vez.
5. No fechamento, `aprendi-<projeto>.md` existe com os quatro itens, está no mapa, e o `registrar`
   saiu com código 0.

Faltou algum: diga qual, em vez de declarar o projeto concluído.
