"""Interface de linha de comando: python -m gerador --help"""

import argparse
import getpass
import sys

from . import avaliar_forca, gerar_frase_senha, gerar_hash, gerar_senha, verificar_hash


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="gerador", description="Gerador de senhas seguro 🔐")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("senha", help="gera senhas aleatórias")
    s.add_argument("-t", "--tamanho", type=int, default=16)
    s.add_argument("-q", "--quantidade", type=int, default=1)
    s.add_argument("--sem-simbolos", action="store_true")
    s.add_argument("--sem-ambiguos", action="store_true", help="remove I, l, 1, O, 0, o")

    f = sub.add_parser("frase", help="gera frases-senha")
    f.add_argument("-p", "--palavras", type=int, default=5)
    f.add_argument("-s", "--separador", default="-")

    sub.add_parser("hash", help="gera o hash Argon2id de uma senha digitada")
    v = sub.add_parser("verificar", help="confere uma senha contra um hash Argon2id")
    v.add_argument("hash")
    sub.add_parser("forca", help="avalia a força de uma senha digitada")

    a = p.parse_args(argv)
    if a.cmd == "senha":
        for _ in range(a.quantidade):
            senha = gerar_senha(a.tamanho, simbolos=not a.sem_simbolos, sem_ambiguos=a.sem_ambiguos)
            bits, nivel = avaliar_forca(senha)
            print(f"{senha}   ({bits} bits, {nivel})")
    elif a.cmd == "frase":
        print(gerar_frase_senha(a.palavras, a.separador))
    elif a.cmd == "hash":
        print(gerar_hash(getpass.getpass("Senha: ")))
    elif a.cmd == "verificar":
        ok = verificar_hash(a.hash, getpass.getpass("Senha: "))
        print("✔ Senha correta" if ok else "✘ Senha incorreta")
        return 0 if ok else 1
    elif a.cmd == "forca":
        bits, nivel = avaliar_forca(getpass.getpass("Senha: "))
        print(f"{bits} bits: {nivel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
