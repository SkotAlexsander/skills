# Uma biblioteca de 139 skills para o Claude Code — auditada, catalogada e medida

139 skills organizadas em 16 temas, em português e inglês, para o
[Claude Code](https://claude.com/claude-code). Cada uma passou por **16 verificações de
segurança antes de entrar**, carrega a licença do autor dentro da própria pasta, e tem uma nota
explicando por que existe e quando usar.

Junto vai o [**Guia das Skills**](guia/GUIA-DAS-SKILLS.md) — 223 skills de uma máquina real com o
tamanho **medido em tokens** e um nível de custo de uso de 🟢 1 a 🔴 5, com o motivo escrito em
cada uma. É a parte deste repositório que serve para quem não vai instalar nada.

> **Seis skills são minhas. As outras 133 são de terceiros**, de 18 repositórios públicos, sob
> MIT, Apache-2.0 e — em oito casos — os Termos de Desenvolvedor da Figma.
> **[A procedência de cada uma está em ATRIBUICAO.md](ATRIBUICAO.md)**, com os commits fixados
> e as alterações declaradas.

---

## Os 16 temas

| Tema | Skills | Do que se trata |
|---|---:|---|
| [`01-estrutura-e-layout`](skills/01-estrutura-e-layout/) | 4 | Landing page, showcase de produto, loop de design |
| [`02-design-visual`](skills/02-design-visual/) | 13 | Cor em OKLCH, tipografia, acessibilidade, design system, Apple design |
| [`03-componentes-e-codigo`](skills/03-componentes-e-codigo/) | 8 | shadcn/ui, Tailwind, padrões de React, bibliotecas animadas |
| [`04-responsividade-e-qualidade`](skills/04-responsividade-e-qualidade/) | 10 | Breakpoints, teste em navegador real, auditoria de UX, performance |
| [`05-assets-e-marca`](skills/05-assets-e-marca/) | 5 | Geração de imagem por IA, ícones, favicon, arte algorítmica |
| [`06-conteudo-e-seo`](skills/06-conteudo-e-seo/) | 2 | Estratégia de conteúdo, SEO de negócio local |
| [`07-ia-e-agentes`](skills/07-ia-e-agentes/) | 13 | Desenho de ferramenta, harness, MCP, avaliação, multi-agente |
| [`08-dados-e-backend`](skills/08-dados-e-backend/) | 4 | Schema, SQL, seed, migração D1 |
| [`09-engenharia-de-software`](skills/09-engenharia-de-software/) | 5 | TDD, depuração sistemática, git, verificação antes de concluir |
| [`10-eficiencia-de-contexto`](skills/10-eficiencia-de-contexto/) | 12 | Orçamento de contexto, compressão, degradação, memória |
| [`11-copy-e-conversao`](skills/11-copy-e-conversao/) | 8 | Copywriting, edição, ofertas, CRO, psicologia de marketing |
| [`12-motion-e-interacao`](skills/12-motion-e-interacao/) | 21 | GSAP, Framer Motion, Anime.js, Lottie, scroll, transição de página |
| [`13-estilos-visuais`](skills/13-estilos-visuais/) | 12 | Bento, brutalism, glassmorphism, editorial, retro, premium |
| [`14-figma`](skills/14-figma/) | 11 | Design → código, tokens, Code Connect — **ver a ressalva de licença** |
| [`15-3d-e-webgl`](skills/15-3d-e-webgl/) | 6 | Three.js, React Three Fiber, Spline, Rive |
| [`16-aprendizado`](skills/16-aprendizado/) | 5 | **As cinco que eu escrevi** — ver abaixo |

---

## As seis que são minhas

Cinco de aprendizado e o portão do Figma. A ideia que atravessa as cinco: **entender não é
reconhecer.** Ler uma explicação boa dá a *sensação* de ter entendido, e a sensação some em
semanas. O que prova o entendimento é recuperar da memória e usar. Por isso, nessas skills,
**quem produz é a pessoa** — o Claude explica, pergunta, confere e registra.

| Skill | O que faz | O detalhe que importa |
|---|---|---|
| [`/estudar`](skills/16-aprendizado/estudar/) | Sessão de estudo com método: diagnostica, explica pelo mecanismo, passa exercício que você roda, fecha com perguntas sem consulta | Fila de revisão espaçada em degraus de 1, 3, 7, 14, 30 e 60 dias, calculada **por script**, não pelo modelo |
| [`/ler-repositorio`](skills/16-aprendizado/ler-repositorio/) | Estuda a fundo um repositório que você não conhece e vira nota | Clona raso **em quarentena sem executar nada** e neutraliza as instruções para agentes que vêm no clone (`CLAUDE.md`, `.claude/`, `AGENTS.md`) |
| [`/desenhar-sistema`](skills/16-aprendizado/desenhar-sistema/) | System Design Primer aplicado a um projeto real, **na escala verdadeira dele** | Estimativa de carga com as contas à vista; cada decisão sai com critério, trade-off e o que faria ela mudar |
| [`/algoritmos-na-pratica`](skills/16-aprendizado/algoritmos-na-pratica/) | Acha e conserta custo algorítmico ruim em código real — laço dentro de laço, N+1, estrutura errada | **Mede antes e depois** com tamanhos crescentes e prova que o resultado não mudou |
| [`/construir-do-zero`](skills/16-aprendizado/construir-do-zero/) | Reconstruir uma tecnologia para entendê-la por dentro: Git, React, servidor HTTP, compilador | Fatia em marcos que rodam, cada um com teste. **Você** escreve o código; a dica é graduada, não é a resposta |
| [`/figma`](skills/14-figma/figma/) | O portão de tudo que envolve Figma | Confere **primeiro** se o MCP da Figma está conectado e diz o que falta. Existe porque o modo de falha sem ela é confuso |

### ⚠️ As cinco de aprendizado precisam de ajuste antes de usar

Elas leem e escrevem numa trilha de estudo em `A:\Claude\02-cerebro\70-aprendizado\` — um vault
Obsidian **que é meu e não está aqui**. Instaladas cru, vão procurar nota que não existe na sua
máquina. Troque esse caminho pela sua pasta de notas:

| Skill | Arquivos com o caminho | Ocorrências |
|---|---|---:|
| `estudar` | `SKILL.md`, `estudar.md`, `scripts/revisao.py` | 13 |
| `ler-repositorio` | `SKILL.md`, `references/spec-agentes.md` | 7 |
| `construir-do-zero` | `SKILL.md` | 5 |
| `algoritmos-na-pratica` | `SKILL.md` | 3 |
| `desenhar-sistema` | `SKILL.md` | 2 |

São **30 ocorrências**. Para achar todas de uma vez:

```bash
grep -rn 'A:\\Claude\\02-cerebro' ~/.claude/skills/
```

O script [`revisao.py`](skills/16-aprendizado/estudar/scripts/revisao.py) escapa disso: lá o
caminho é **padrão de argumento**, e `--arquivo <caminho>` sobrescreve. Ele é stdlib pura, sem
rede e sem `subprocess`, e grava sempre em UTF-8 (no Windows o `open()` padrão do Python 3.10 é
cp1252 e estraga acento em silêncio).

---

## Instalar

As skills estão agrupadas por tema, mas o Claude Code espera cada skill **direto** em
`~/.claude/skills/`. Os scripts fazem essa planificação:

```bash
git clone https://github.com/SkotAlexsander/skills.git
cd skills
bash instalar.sh            # todas
bash instalar.sh 16-aprendizado 02-design-visual   # só alguns temas
```

No Windows:

```powershell
git clone https://github.com/SkotAlexsander/skills.git
cd skills
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
powershell -ExecutionPolicy Bypass -File .\instalar.ps1 16-aprendizado 02-design-visual
```

O `-ExecutionPolicy Bypass` está aí porque o Windows vem com a política `Restricted`, e nela
`.\instalar.ps1` falha com *"a execução de scripts foi desabilitada neste sistema"*. O `Bypass`
vale **só para essa chamada** — não muda a configuração da sua máquina. Se a sua política já for
`RemoteSigned` ou mais permissiva, `.\instalar.ps1` direto funciona.

Os dois copiam; nada é apagado e nada é sobrescrito sem aviso — skill que já existe no destino é
**pulada**, com aviso. Para instalar uma só, à mão, basta copiar a pasta dela para
`~/.claude/skills/`. `CLAUDE_SKILLS_DIR` muda o destino nos dois scripts.

### Instale menos do que você acha que precisa

**Skill instalada custa mesmo sem ser usada.** A descrição de toda skill entra na lista que o
modelo recebe no começo de **toda** sessão. Na máquina medida, as 131 globais mais um plugin
somavam **~13,9 mil tokens de custo fixo por sessão**. Isso é contexto que sai do seu trabalho.

O [guia](guia/GUIA-DAS-SKILLS.md) existe em boa parte para essa decisão: ele diz o que cada skill
custa e por quê, e tem uma seção sobre como desligar uma skill sem apagar nada.

---

## O que o guia estabelece, com número

[`guia/GUIA-DAS-SKILLS.md`](guia/GUIA-DAS-SKILLS.md) · [em PDF](guia/GUIA-DAS-SKILLS.pdf) (4,9 MB) · gerado em 13/09/2026

- **Um subagente é uma sessão inteira.** Seis agentes medidos gastaram entre **208 e 291 mil
  tokens** cada. Antes deles, oito em paralelo estouraram o limite de uso duas vezes seguidas.
  Daí a regra de rodar em ondas de 3.
- **Imagem custa caro.** Uma captura Full HD custa **2.691 tokens** — umas 2 mil palavras. Skill
  que tira uma captura por estado de tela multiplica isso.
- **Os tamanhos são medidos; os níveis de custo são classificação minha**, com o critério
  explicado na abertura do documento.

O guia cobre 223 skills — mais do que as 139 daqui, porque inclui as embutidas no Claude Code, as
de plugin e as locais de um projeto meu, que não estão neste repositório.

---

## Segurança

As 139 entraram por um portão, não por `curl | bash`. Cada lote foi clonado para pasta temporária,
auditado lá **sem executar nada**, e só então copiado. As 16 verificações — binário disfarçado,
pipe-to-shell, `eval`/`atob`, roubo de credencial, comando destrutivo, persistência, domínios,
IP literal, injeção de prompt, unicode invisível, bypass de permissão, efeito externo, leitura
fora do projeto, `allowed-tools` do frontmatter e leitura manual de todo executável — estão
documentadas com o resultado de cada uma em
[`docs/00-CATALOGO-E-AUDITORIA.md`](docs/00-CATALOGO-E-AUDITORIA.md).

Esse documento também lista os **repositórios rejeitados e por quê** — inclusive vários muito
populares, barrados por falta de arquivo de licença.

**Isto não é atestado de segurança para a sua máquina.** É o registro de uma auditoria feita numa
data, em versões fixadas. Leia o `SKILL.md` do que você instalar: uma skill é instrução que o
modelo vai seguir.

---

## Licença

- **O que é meu** — as 6 skills, as notas `<skill>.md`, os mapas de tema, o catálogo e o guia:
  [MIT](LICENSE), © 2026 Alex Martins.
- **As outras 133** — cada uma sob a licença do seu autor, no `LICENSE.txt` dentro da pasta dela.
  Detalhe em [ATRIBUICAO.md](ATRIBUICAO.md).
- **As 8 da Figma** estão sob os Termos de Desenvolvedor da Figma, que não são licença open
  source. [Leia a ressalva](ATRIBUICAO.md#4-as-8-skills-da-figma--leia-antes-de-reusar) antes de
  reusar.

Autor de alguma delas e quer a sua fora daqui? Abra uma issue — eu removo.
