import requests
from abc import ABC, abstractmethod


class BuscaCep(ABC):
    @abstractmethod
    def buscar(self, cep):
        ...


class ViaCepService(BuscaCep):
    url_format = "https://viacep.com.br/ws/{cep}/json/"

    def buscar(self, cep):
        url = self.url_format.format(cep=cep)
        response = requests.get(url)

        data = response.json()
        if data.get("erro"):
            raise ValueError(f"CEP {cep} inválido.")

        return {
            "rua": data.get("logradouro"),
            "bairro": data.get("bairro"),
            "cidade": data.get("localidade"),
            "estado": data.get("uf"),
        }


class BrasilApiCepService(BuscaCep):
    url_format = "https://brasilapi.com.br/api/cep/v1/{cep}"

    def buscar(self, cep):
        url = self.url_format.format(cep=cep)
        response = requests.get(url)
        if response.status_code == 404:
            raise ValueError(f"CEP {cep} inválido.")
        data = response.json()

        return {
            "rua": data.get("street"),
            "bairro": data.get("neighborhood"),
            "cidade": data.get("city"),
            "estado": data.get("state"),
        }