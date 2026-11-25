"""Hash de senhas com Argon2id (argon2-cffi)."""

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError

# Parâmetros alinhados à recomendação da OWASP para Argon2id.
_hasher = PasswordHasher(time_cost=3, memory_cost=64 * 1024, parallelism=2)


def gerar_hash(senha: str) -> str:
    """Retorna o hash Argon2id (já inclui salt e parâmetros)."""
    if not senha:
        raise ValueError("Senha vazia.")
    return _hasher.hash(senha)


def verificar_hash(hash_armazenado: str, senha: str) -> bool:
    """Confere a senha contra o hash sem lançar exceção para senha errada."""
    try:
        return _hasher.verify(hash_armazenado, senha)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False
