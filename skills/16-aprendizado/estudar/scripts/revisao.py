#!/usr/bin/env python3
"""
revisao.py - a fila de revisao espacada da trilha de aprendizado.

Motor deterministico da skill /estudar. Le e escreve a tabela de
`progresso-estudos.md` no Cerebro, para que a conta de datas nao dependa do modelo.

Uso:
  python revisao.py pendentes [--hoje AAAA-MM-DD]
      Lista as notas cuja proxima revisao ja venceu (ou vence hoje).

  python revisao.py registrar <nota> --acertos N --total M [--hoje AAAA-MM-DD]
      Registra uma sessao ou revisao da nota e calcula a proxima data.
      Nota nova entra no degrau 0. Nota existente sobe, fica ou cai de degrau.

  python revisao.py diario "<texto>" [--hoje AAAA-MM-DD]
      Acrescenta uma linha no topo do diario de sessoes.

  python revisao.py fila
      Mostra a fila inteira, ordenada pela proxima revisao.

Opcao comum: --arquivo <caminho do progresso-estudos.md>

Codigos de saida:
  0 = feito
  1 = feito, mas com aviso que merece o seu olho (ex.: a nota nao existe na trilha)
  2 = erro (arquivo ou marcador ausente, argumento invalido) - nada foi escrito

So stdlib. Le e grava sempre em UTF-8: no Windows o padrao do open() no Python 3.10
e o cp1252, e ele estraga acento em silencio.
"""

import argparse
import datetime as dt
import os
import re
import sys

ARQUIVO_PADRAO = r"A:\Claude\02-cerebro\70-aprendizado\90-progresso\progresso-estudos.md"
RAIZ_TRILHA = r"A:\Claude\02-cerebro\70-aprendizado"

# Degrau -> dias ate a proxima revisao. Precisa bater com a tabela explicada no .md.
INTERVALOS = [1, 3, 7, 14, 30, 60]
SOBE_A_PARTIR = 0.80   # acertou 80%+ -> sobe um degrau
MANTEM_A_PARTIR = 0.50  # 50%-79% -> fica; abaixo de 50% -> volta ao degrau 0

MARCA_FILA_INI = "<!-- revisao:inicio -->"
MARCA_FILA_FIM = "<!-- revisao:fim -->"
MARCA_DIARIO_INI = "<!-- diario:inicio -->"
MARCA_DIARIO_FIM = "<!-- diario:fim -->"
CABECALHO = [
    "| Nota | Degrau | Última revisão | Resultado | Próxima revisão |",
    "|---|---|---|---|---|",
]


class Erro(Exception):
    """Erro que vira mensagem humana e codigo de saida 2."""


# --------------------------------------------------------------------------- arquivo

def ler(caminho):
    if not os.path.isfile(caminho):
        raise Erro(f"Não achei o arquivo de progresso em: {caminho}")
    with open(caminho, "r", encoding="utf-8", newline="") as f:
        return f.read()


def gravar(caminho, texto):
    # Grava num temporario e troca: se algo falhar no meio, o original fica inteiro.
    temporario = caminho + ".tmp"
    with open(temporario, "w", encoding="utf-8", newline="") as f:
        f.write(texto)
    os.replace(temporario, caminho)


def trecho(texto, inicio, fim):
    """Devolve (antes, miolo, depois) entre dois marcadores."""
    i = texto.find(inicio)
    j = texto.find(fim)
    if i == -1 or j == -1 or j < i:
        raise Erro(
            f"Os marcadores {inicio} e {fim} sumiram ou estão fora de ordem no arquivo. "
            "Restaure-os (veja o modelo no próprio progresso-estudos.md) antes de rodar de novo."
        )
    i_fim = i + len(inicio)
    return texto[:i_fim], texto[i_fim:j], texto[j:]


def quebra_de_linha(texto):
    return "\r\n" if "\r\n" in texto else "\n"


# --------------------------------------------------------------------------- tabela

LINHA_RE = re.compile(
    r"^\|\s*\[\[(?P<nota>[^\]|]+)(?:\|[^\]]*)?\]\]\s*"
    r"\|\s*(?P<degrau>\d+)\s*"
    r"\|\s*(?P<ultima>\d{4}-\d{2}-\d{2})\s*"
    r"\|\s*(?P<resultado>[^|]*?)\s*"
    r"\|\s*(?P<proxima>\d{4}-\d{2}-\d{2})\s*\|\s*$"
)


def ler_fila(miolo):
    itens = []
    for n, linha in enumerate(miolo.splitlines(), start=1):
        linha = linha.strip()
        if not linha or linha in CABECALHO or set(linha) <= set("|-: "):
            continue
        m = LINHA_RE.match(linha)
        if not m:
            raise Erro(
                f"Não entendi esta linha da fila de revisão (linha {n} do bloco):\n  {linha}\n"
                "Formato esperado: | [[nota]] | 0 | AAAA-MM-DD | 4/5 | AAAA-MM-DD |"
            )
        itens.append({
            "nota": m["nota"].strip(),
            "degrau": int(m["degrau"]),
            "ultima": data(m["ultima"]),
            "resultado": m["resultado"],
            "proxima": data(m["proxima"]),
        })
    return itens


def escrever_fila(itens, nl):
    itens = sorted(itens, key=lambda i: (i["proxima"], i["nota"]))
    linhas = list(CABECALHO)
    for i in itens:
        linhas.append(
            f"| [[{i['nota']}]] | {i['degrau']} | {i['ultima'].isoformat()} "
            f"| {i['resultado']} | {i['proxima'].isoformat()} |"
        )
    return nl + nl.join(linhas) + nl


# --------------------------------------------------------------------------- regras

def data(texto):
    try:
        return dt.date.fromisoformat(texto)
    except ValueError:
        raise Erro(f"Data inválida: '{texto}'. Use AAAA-MM-DD, por exemplo 2026-09-12.")


def data_argumento(texto):
    # O argparse só converte ArgumentTypeError em mensagem + saída 2; qualquer outra
    # exceção dentro de um type= escapa como traceback com saída 1.
    try:
        return data(texto)
    except Erro as e:
        raise argparse.ArgumentTypeError(str(e))


def novo_degrau(degrau_atual, acertos, total, nota_nova):
    if nota_nova:
        return 0
    taxa = acertos / total
    if taxa >= SOBE_A_PARTIR:
        return min(degrau_atual + 1, len(INTERVALOS) - 1)
    if taxa >= MANTEM_A_PARTIR:
        return degrau_atual
    return 0


def nota_existe(nota):
    for pasta, _, arquivos in os.walk(RAIZ_TRILHA):
        if f"{nota}.md" in arquivos:
            return True
    return False


# --------------------------------------------------------------------------- comandos

def cmd_pendentes(args):
    texto = ler(args.arquivo)
    _, miolo, _ = trecho(texto, MARCA_FILA_INI, MARCA_FILA_FIM)
    itens = ler_fila(miolo)
    vencidas = sorted((i for i in itens if i["proxima"] <= args.hoje), key=lambda i: i["proxima"])
    if not vencidas:
        prox = min((i["proxima"] for i in itens), default=None)
        extra = f" A próxima vence em {prox.isoformat()}." if prox else " A fila está vazia."
        print(f"Nada para revisar em {args.hoje.isoformat()}.{extra}")
        return 0
    print(f"{len(vencidas)} nota(s) para revisar em {args.hoje.isoformat()}:")
    for i in vencidas:
        atraso = (args.hoje - i["proxima"]).days
        quando = "vence hoje" if atraso == 0 else f"atrasada {atraso} dia(s)"
        print(f"  - {i['nota']}  (degrau {i['degrau']}, {quando}, último resultado {i['resultado']})")
    return 0


def cmd_fila(args):
    texto = ler(args.arquivo)
    _, miolo, _ = trecho(texto, MARCA_FILA_INI, MARCA_FILA_FIM)
    itens = sorted(ler_fila(miolo), key=lambda i: i["proxima"])
    if not itens:
        print("A fila de revisão está vazia.")
        return 0
    for i in itens:
        print(f"{i['proxima'].isoformat()}  degrau {i['degrau']}  {i['nota']}  ({i['resultado']})")
    return 0


def cmd_registrar(args):
    if args.total <= 0:
        raise Erro("--total precisa ser maior que zero (quantas perguntas foram feitas).")
    if args.acertos < 0 or args.acertos > args.total:
        raise Erro(f"--acertos precisa estar entre 0 e {args.total}.")
    nota = args.nota.strip().removeprefix("[[").removesuffix("]]").split("|")[0].strip()
    if not nota:
        raise Erro("Informe o nome da nota, sem a extensão .md (ex.: complexidade-big-o).")

    texto = ler(args.arquivo)
    nl = quebra_de_linha(texto)
    antes, miolo, depois = trecho(texto, MARCA_FILA_INI, MARCA_FILA_FIM)
    itens = ler_fila(miolo)

    existente = next((i for i in itens if i["nota"] == nota), None)
    degrau_antigo = existente["degrau"] if existente else None
    degrau = novo_degrau(degrau_antigo or 0, args.acertos, args.total, existente is None)
    proxima = args.hoje + dt.timedelta(days=INTERVALOS[degrau])
    registro = {
        "nota": nota,
        "degrau": degrau,
        "ultima": args.hoje,
        "resultado": f"{args.acertos}/{args.total}",
        "proxima": proxima,
    }
    if existente:
        itens[itens.index(existente)] = registro
    else:
        itens.append(registro)

    gravar(args.arquivo, antes + escrever_fila(itens, nl) + depois)

    if existente:
        print(f"{nota}: degrau {degrau_antigo} -> {degrau} ({args.acertos}/{args.total}). "
              f"Próxima revisão: {proxima.isoformat()}.")
    else:
        print(f"{nota}: entrou na fila no degrau 0. Primeira revisão: {proxima.isoformat()}.")

    if not nota_existe(nota):
        print(f"AVISO: não existe '{nota}.md' dentro de {RAIZ_TRILHA}. "
              "O registro foi feito, mas o wikilink vai ficar quebrado no Obsidian.")
        return 1
    return 0


def cmd_diario(args):
    linha = " ".join(args.texto.split())
    if not linha:
        raise Erro("O texto do diário está vazio.")
    texto = ler(args.arquivo)
    nl = quebra_de_linha(texto)
    antes, miolo, depois = trecho(texto, MARCA_DIARIO_INI, MARCA_DIARIO_FIM)
    entradas = [l for l in miolo.splitlines() if l.strip()]
    entradas.insert(0, f"- **{args.hoje.isoformat()}** — {linha}")
    gravar(args.arquivo, antes + nl + nl.join(entradas) + nl + depois)
    print(f"Diário atualizado ({args.hoje.isoformat()}).")
    return 0


# --------------------------------------------------------------------------- main

def main(argv=None):
    comum = argparse.ArgumentParser(add_help=False)
    comum.add_argument("--arquivo", default=ARQUIVO_PADRAO, help="caminho do progresso-estudos.md")
    comum.add_argument("--hoje", type=data_argumento, default=dt.date.today(),
                       help="data de referência AAAA-MM-DD")

    p = argparse.ArgumentParser(description="Fila de revisão espaçada da trilha de aprendizado.")
    sub = p.add_subparsers(dest="comando", required=True)

    sub.add_parser("pendentes", parents=[comum], help="notas com revisão vencida")
    sub.add_parser("fila", parents=[comum], help="a fila inteira")

    r = sub.add_parser("registrar", parents=[comum], help="registra uma sessão ou revisão")
    r.add_argument("nota")
    r.add_argument("--acertos", type=int, required=True)
    r.add_argument("--total", type=int, required=True)

    d = sub.add_parser("diario", parents=[comum], help="acrescenta linha ao diário")
    d.add_argument("texto")

    try:
        args = p.parse_args(argv)
    except SystemExit as e:
        # argparse sai com 2 em argumento inválido e 0 no --help: preserva os dois.
        return e.code if isinstance(e.code, int) else 2

    comandos = {"pendentes": cmd_pendentes, "fila": cmd_fila,
                "registrar": cmd_registrar, "diario": cmd_diario}
    try:
        return comandos[args.comando](args)
    except Erro as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    # Garante acento certo no console do Windows, onde stdout pode estar em cp1252.
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    sys.exit(main())
