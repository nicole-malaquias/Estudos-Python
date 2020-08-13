from datetime import datetime

class DatasBr:

    def __init__(self):
        self.momento_cadastro =datetime.today()  # pega um meotodo da classe que mostra a hora exata do instanciamento

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro"
            "outubro", "novembro","dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month #tem um range de 1 a 12
        return meses_do_ano[mes_cadastro -1]

    def semana_cadastro(self):
        semana=[
            "segunda","terça","quarta","quinta","sexta","sabado","domingo"
        ]
        semana_do_cadastro = self.momento_cadastro.weekday()
        return semana[semana_do_cadastro-1]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y") #transforma conforme o código
        return data_formatada

    def __str__(self):
        return self.formata_data()