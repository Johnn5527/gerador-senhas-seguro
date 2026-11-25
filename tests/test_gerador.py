import string

import pytest

from gerador import avaliar_forca, gerar_frase_senha, gerar_hash, gerar_senha, verificar_hash
from gerador.senhas import AMBIGUOS, SIMBOLOS


def test_senha_tem_tamanho_e_todos_os_grupos():
    for _ in range(200):
        s = gerar_senha(16)
        assert len(s) == 16
        assert any(c.islower() for c in s)
        assert any(c.isupper() for c in s)
        assert any(c.isdigit() for c in s)
        assert any(c in SIMBOLOS for c in s)


def test_senha_sem_simbolos_e_sem_ambiguos():
    for _ in range(200):
        s = gerar_senha(20, simbolos=False, sem_ambiguos=True)
        assert all(c in string.ascii_letters + string.digits for c in s)
        assert not set(s) & AMBIGUOS


def test_senha_curta_e_recusada():
    with pytest.raises(ValueError):
        gerar_senha(6)


def test_senhas_nao_se_repetem():
    assert len({gerar_senha() for _ in range(500)}) == 500


def test_frase_senha():
    frase = gerar_frase_senha(5)
    partes = frase.split("-")
    assert len(partes) == 6 and partes[-1].isdigit()


def test_forca():
    assert avaliar_forca("abc")[1] == "fraca"
    assert avaliar_forca(gerar_senha(20))[1] == "muito forte"


def test_hash_argon2id():
    h = gerar_hash("minha senha")
    assert h.startswith("$argon2id$")
    assert verificar_hash(h, "minha senha")
    assert not verificar_hash(h, "outra senha")
    assert not verificar_hash("hash-invalido", "minha senha")
