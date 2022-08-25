n1 = int(input('Digite a idade: '))
n2 = int(input('Digite a idade: '))
n3 = int(input('Digite a idade: '))
n4 = int(input('Digite a idade: '))
n5 = int(input('Digite a idade: '))
n6 = int(input('Digite a idade: '))
n7 = int(input('Digite a idade: '))

lista_idades = [n1, n2, n3, n4, n5, n6, n7]

maior = 0
menor = 0
for i in lista_idades:
    if i >= 18:
        maior += 1
    else:
        menor += 1
print('{} são menores de idade, {} já atingiram a maior idade.' .format(menor, maior))