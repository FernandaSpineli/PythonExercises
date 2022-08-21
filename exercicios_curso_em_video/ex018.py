import math

angulo = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(angulo))
print('O seno do ângulo tem valor {:.2f}.' .format(seno))

cosseno = math.cos(math.radians(angulo))
print('O cosseno do ângulo tem valor {:.2f}.' .format(cosseno))

tangente = math.tan(math.radians(angulo))
print('A tagente do ângulo tem valor {:.2f}.' .format(tangente))