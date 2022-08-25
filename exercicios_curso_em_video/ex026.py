value = int(input('Digite a distancia em Km a ser percorrida: '))

if value <= 200:
    total = value * 0.50
    print('A passagem custará R${:.2f}' .format(total))
else:
    total= value * 0.45
    print('A passagem custará R${:.2f}' .format(total))
