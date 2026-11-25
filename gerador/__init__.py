"""Gerador de senhas seguro: geração com `secrets` e hash com Argon2id."""

from .senhas import gerar_senha, gerar_frase_senha, avaliar_forca
from .hash import gerar_hash, verificar_hash

__all__ = ["gerar_senha", "gerar_frase_senha", "avaliar_forca", "gerar_hash", "verificar_hash"]
__version__ = "1.0.0"
