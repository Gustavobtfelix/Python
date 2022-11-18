from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momentoCadastro = datetime.today()

    def mesCadastro(self):
        mesesDoAno=[
             "janeiro", "fevereiro", "março",
             "abril", "maio", "junho", "julho",
             "agosto", "setembro", "outubro",
             "novembro"
         ]
        mesCastro = self.momentoCadastro.month -1
        print(mesesDoAno[mesCastro])

    def diaSemana(self):
        diasDaSemana = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sabado",
            "domingo"
        ]
        diaSemana = self.momentoCadastro.weekday()
        print(diasDaSemana[diaSemana])

    def formataData(self):
        dataFormatada = self.momentoCadastro.strftime("%d/%m/%Y %H:%M")
        print (dataFormatada)


if(__name__ == "__main__"):
    data = DatasBr()
    data.mesCadastro()
    data.diaSemana()
    data.formataData()