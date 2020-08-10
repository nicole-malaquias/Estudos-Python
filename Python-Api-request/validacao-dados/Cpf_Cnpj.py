##cpf validação - deve conter 11 digitos e ultizar biblioteca de validação
##mascara   999 09990 999

## cnpj deve conter 14 digitos e utlizar biblioteca de validação
##  99 999 999 /9999 99

##telefone / celiilar
## validação



from validate_docbr import CPF
from validate_docbr import CNPJ







class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) ==11:
            return DocCpf(Documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError ("Quantidade de digito está incorreta")

class DocCpf:

    def __init__(self):
        if self.valida(documento):
            self.cpf =documento
        else:
            raise ValueError("Cpf invalido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador= Cpf()
        return validador.validate(documento)

    def format(self):
        mascara= cpf()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self,documento):
        if self.valida(documento):
            self.cpnj = documento
        else:
            raise ValueError("Cnpj invalido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = cnpj()
        return mascara.mask(self.cnpj)

