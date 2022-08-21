lanche = ('hamburgue', 'suco', 'pizza', 'pudim')
print(lanche[1])

teste = list()
teste.append('Maria')
teste.append(14)
galera = list()
galera.append(teste[:])
teste[0] = 'Ana'
teste[1] = 25
galera.append(teste[:])
print(galera)

turma = list()
dado = list()

for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])
    dado.clear()

print(turma)
