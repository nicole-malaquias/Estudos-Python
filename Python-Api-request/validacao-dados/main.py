<<<<<<< HEAD
from Acesso_Cep import BuscaEndereco
import requests

# telefone = "551236325841"
# telefoneObj = TelefoneBr(telefone)


# cadastro = DatasBr()# instancia o objeto
# print(cadastro)


# data1 = DatasBr()
# data2 = DatasBr()
# data1.tempo_cadastro()
# print(data1.tempo_cadastro())
# print(data2)

#
# cep = "12010490"
# objCep= BuscaEndereco(cep)
# print(objCep)

#r = requests.get("https://viacep.com.br/ws/")

cep ="12010490"
objeto_cep= BuscaEndereco(cep)

bairroCidadeUf= objeto_cep.acessa_via_cep()
print(bairroCidadeUf)
=======
from TelefonesBr import TelefoneBr
import re

telefone = "551236325841"
telefoneObj = TelefoneBr(telefone)

>>>>>>> ced18dcff728aef366fb497241942a75ac349581
