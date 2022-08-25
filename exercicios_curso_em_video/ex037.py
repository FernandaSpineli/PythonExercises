from random import randint
from urllib.response import addinfo

sorteia = randint(0, 5)
adivinha = int(input('Em que número pensei? '))

if sorteia == adivinha:
    print('Você adivinhou!!')
else:
    print('Tente novamente, você consegue.')
