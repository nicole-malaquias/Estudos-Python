import requests
#é preciso instalar a request pip install request

class BuscaEndereco:

    def __init__(self,cep):
        cep = str(cep)
        if(self.cep_eh_validado(cep)):
            self.cep = cep
        else:
            print(len(cep))
            raise ValueError("Esse cep não é valido")

    def cep_eh_validado(self, cep):
        if(len(cep)==8):
            return True
        else:
            return False


    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[4:])


    def __str__(self):
        return self.format_cep()


    def acessa_via_cep(self):
        url = "http://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()

        return(
            dados['bairro'], dados['localidade'],dados['uf']
        )
