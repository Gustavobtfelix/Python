import re #Regular Expression -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, Rj, 23440-120"

#cep 5 digitos + hifen (opcional) + 3 digitos

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #digitos de 0 a 9 em 5 caracteres seguido de traco em 0 ou 1 caracteres seguido de digitos de 0 a 9 em 3 caracteres
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)
else: 
    print("nao encontrou cep")