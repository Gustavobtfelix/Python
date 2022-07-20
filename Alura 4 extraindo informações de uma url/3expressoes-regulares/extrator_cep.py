import re #Regular Expression -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, Rj, 23440-120"

#cep 5 digitos + hifen (opcional) + 3 digitos

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)
else: 
    print("nao encontrou cep")