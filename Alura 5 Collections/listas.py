"""Introdução a Collections"""

idades = [39, 30, 27, 18]

for indice, valor in enumerate(idades):
    print(indice, valor)
print(indice)

print(idades)
print(type(idades))
idades.append(15)#adiciona no final
idades.remove(30)#remove o primeiro identificado do final ao começo
print(28 in idades)
print(39 in idades)
idades.extend([10, 20])
print(idades)
for elemento in idades:
    break
    print(elemento)

#idades.clear()#limpa a lista

nova_idade = [(idade + 1) for idade in idades]
print(nova_idade)
nova_idade2 = [(idade) for idade in idades if idade >21]
print(nova_idade2)
#list comprehension




