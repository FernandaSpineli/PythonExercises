from base64 import b16decode


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

resto1 = n1 % 2 
resto2 = n2 % 2

if resto1 == 0 or not resto2 == 0:
    print('Possui número par.')

if n1 > n2 and n1 > n3:
    print('O maior número é: {}' .format(n1))
    
b1 = int(input('Digite a nota do primeiro bimestre: '))    
while b1 > 10:
    print(input('Nota inválida. Digite a nota do primeiro bimestre: '))
b2 = int(input('Digite a nota do segundo bimestre: '))
while b2 > 10:
    print('Nota inválida. Digite a nota do segundo bimestre: ')
