from codigo.bytebank import Funcionario


ana = Funcionario('Ana Carvalho Bourbon', '12/03/1997', 10000)

print(ana.idade())
print(ana.sobrenome())
print(ana._eh_socio())
print(ana.decrescimo_salario())
print(ana.calcular_bonus())
print(ana)