import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
# hip = (co ** 2 + ca ** 2) ** (1/2)

hip = math.hypot(co, ca)
print('A hipotenusa tem valor: {:.2f}' .format(hip))