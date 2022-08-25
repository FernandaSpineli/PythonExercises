n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = int(input('Digite um número: '))
n6 = int(input('Digite um número: '))

lista_numerica = [n1, n2, n3, n4, n5, n6]

soma = 0
for i in lista_numerica:
    if i % 2 == 0:
        soma += i
print(soma)