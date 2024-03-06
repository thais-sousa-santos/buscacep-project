# tests/test_busca_cep.py
import pytest

from busca_cep import ViaCepService, BrasilApiCepService


@pytest.mark.parametrize(
    "service, cep, data_esperado, raises",
    [
        (
                ViaCepService(),
                "59010-036",
                {
                    "rua": "Travessa Vinte e Cinco de Dezembro",
                    "bairro": "Praia do Meio",
                    "cidade": "Natal",
                    "estado": "RN",
                },
                False,
        ),
        (
                ViaCepService(),
                "05002-070",
                {
                    "rua": "Rua Airosa Galvão",
                    "bairro": "Água Branca",
                    "cidade": "São Paulo",
                    "estado": "SP",
                },
                False,
        ),
        (
                ViaCepService(),
                "00000-000",
                {},
                ValueError,
        ),
        (
                BrasilApiCepService(),
                "59010-036",
                {
                    "rua": "Travessa Vinte e Cinco de Dezembro",
                    "bairro": "Praia do Meio",
                    "cidade": "Natal",
                    "estado": "RN",
                },
                False,
        ),
        (
                BrasilApiCepService(),
                "05002-070",
                {
                    "rua": "Rua Airosa Galvão",
                    "bairro": "Água Branca",
                    "cidade": "São Paulo",
                    "estado": "SP",
                },
                False,
        ),
        (
                BrasilApiCepService(),
                "00000-000",
                {},
                ValueError,
        ),
    ],
)
def test_busca_cep(service, cep, data_esperado, raises):
    if raises:
        with pytest.raises(raises):
            service.buscar(cep)
    else:
        data = service.buscar(cep)
        assert data == data_esperado
