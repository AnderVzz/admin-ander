import pytest
from suma import incrementar_saldo

def test_incrementar_saldo():
    saldo_inicial = 500
    saldo_esperado = 1500
    assert incrementar_saldo(saldo_inicial) == saldo_esperado
