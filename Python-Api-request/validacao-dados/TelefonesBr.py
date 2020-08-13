<<<<<<< HEAD
import re
class TelefoneBr:

    def __init__(self, telefone):
        if(self.valida_telefone(telefone)):
            self.numero = telefone
        else:
            raise ValueError ("Este numero não confere")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})" # () forma grupos, ? deixa como opcional
        resposta = re.findall(padrao,telefone)  #findall retorna listas
        if resposta:  #se retorna algo é true
            return True
        else:  # se não é false
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return (numero_formatado)

    def __str__(self):
=======
import re
class TelefoneBr:

    def __init__(self, telefone):
        if(self.valida_telefone(telefone)):
            self.numero = telefone
        else:
            raise ValueError ("Este numero não confere")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})" # () forma grupos, ? deixa como opcional
        resposta = re.findall(padrao,telefone)  #findall retorna listas
        if resposta:  #se retorna algo é true
            return True
        else:  # se não é false
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return (numero_formatado)

    def __str__(self):
>>>>>>> ced18dcff728aef366fb497241942a75ac349581
        return self.format_numero()