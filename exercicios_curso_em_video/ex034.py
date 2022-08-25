number = int(input('Digite um número: '))
total = 0

for c in range(1, number + 1):
    if number % c == 0:
        total += 1

if total == 2:
    print('O número {} é PRIMO!'.format(number))
else:
    print('O número {} não é PRIMO.'.format(number))
        