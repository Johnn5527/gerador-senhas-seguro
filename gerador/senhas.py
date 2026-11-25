"""Geração de senhas e frases-senha usando apenas aleatoriedade criptográfica."""

from __future__ import annotations

import math
import secrets
import string

MINUSCULAS = string.ascii_lowercase
MAIUSCULAS = string.ascii_uppercase
DIGITOS = string.digits
SIMBOLOS = "!@#$%&*()-_=+[]{};:,.?"
AMBIGUOS = set("Il1O0o")

# Lista curta de palavras em português (sem acento) para frases-senha.
PALAVRAS = (
    "abacaxi areia astro azul balao banco barco bola bravo brisa cafe caju calor "
    "campo canto carta casa cedro chave chuva cidade cinza clima cobre coral corda "
    "cristal dado dente disco doce duna eco escada estrela faca farol festa flor "
    "fogo folha fonte foto fruta gato gelo girafa globo gota grama guia ilha janela "
    "jardim jogo lago lapis leao letra limao livro lobo lua luz manga mapa mar "
    "massa mel metal milho mundo musica navio neve nuvem oceano olho onda ouro "
    "ovo palco papel pato pedra peixe pena piano pipa planeta ponte porta prato "
    "praia quadro raio rede rio robo roda rosa sal selo sino sol sombra tambor "
    "tela terra tigre torre trem trevo uva vale vela vento verde vidro vulcao zebra"
).split()


def _remover_ambiguos(conjunto: str) -> str:
    return "".join(c for c in conjunto if c not in AMBIGUOS)


def gerar_senha(
    tamanho: int = 16,
    *,
    maiusculas: bool = True,
    digitos: bool = True,
    simbolos: bool = True,
    sem_ambiguos: bool = False,
) -> str:
    """Gera uma senha aleatória garantindo ao menos um caractere de cada grupo escolhido."""
    grupos = [MINUSCULAS]
    if maiusculas:
        grupos.append(MAIUSCULAS)
    if digitos:
        grupos.append(DIGITOS)
    if simbolos:
        grupos.append(SIMBOLOS)
    if sem_ambiguos:
        grupos = [_remover_ambiguos(g) for g in grupos]

    if tamanho < max(8, len(grupos)):
        raise ValueError("A senha precisa ter pelo menos 8 caracteres.")

    alfabeto = "".join(grupos)
    caracteres = [secrets.choice(g) for g in grupos]
    caracteres += [secrets.choice(alfabeto) for _ in range(tamanho - len(caracteres))]

    # Embaralha com Fisher-Yates usando secrets (random.shuffle não é criptográfico).
    for i in range(len(caracteres) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    return "".join(caracteres)


def gerar_frase_senha(palavras: int = 5, separador: str = "-", com_numero: bool = True) -> str:
    """Gera uma frase-senha fácil de lembrar e difícil de adivinhar."""
    if palavras < 4:
        raise ValueError("Use pelo menos 4 palavras.")
    escolhidas = [secrets.choice(PALAVRAS) for _ in range(palavras)]
    if com_numero:
        escolhidas.append(str(secrets.randbelow(100)).zfill(2))
    return separador.join(escolhidas)


def avaliar_forca(senha: str) -> tuple[float, str]:
    """Estima a entropia (bits) pelo tamanho do alfabeto usado e devolve uma classificação."""
    alfabeto = 0
    if any(c in MINUSCULAS for c in senha):
        alfabeto += len(MINUSCULAS)
    if any(c in MAIUSCULAS for c in senha):
        alfabeto += len(MAIUSCULAS)
    if any(c in DIGITOS for c in senha):
        alfabeto += len(DIGITOS)
    if any(c not in MINUSCULAS + MAIUSCULAS + DIGITOS for c in senha):
        alfabeto += len(SIMBOLOS)
    bits = len(senha) * math.log2(alfabeto) if alfabeto else 0.0

    if bits < 40:
        nivel = "fraca"
    elif bits < 60:
        nivel = "razoável"
    elif bits < 80:
        nivel = "forte"
    else:
        nivel = "muito forte"
    return round(bits, 1), nivel
