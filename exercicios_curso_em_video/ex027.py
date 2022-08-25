year = int(input('Digite o ano que quer analisar: '))

if year % 4 == 0:
    print("O ano {} é BIXESTO." .format(year))
else:
    print("O ano {} não é BIXESTO." .format(year))
