
class ConversorString:
    def __init__(self, string):
        self.string = self.sanitiza_string(string)

    def sanitiza_string(self, string):
        if type(string) == str:
            string = string.replace(" ", "")
            string = string.replace(",", ".")
            string = string.lower()
            print(string)
            return string
        else:
            raise ValueError("A string nao e valida")


    def get_valor_parametro(self, parametro_busca):
        parametro_busca = parametro_busca.lower()
        indice_parametro = self.string.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.string.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.string[indice_valor:]
        else:
            valor = self.string[indice_valor: indice_e_comercial]
        return valor
        


valorReal = "Dolar = 5,43 & Euro = 5,55 & Libra = 6,51"

print(valorReal)

converte1 = ConversorString(valorReal)

valor = converte1.get_valor_parametro('Dolar')
print(valor)