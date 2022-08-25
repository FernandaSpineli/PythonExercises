salario = int(input('Digite o valor do salário atual: '))

if salario > 1250:
    aumento = (salario * 10) / 100
    final = salario + aumento
    print('O salário com aumento é R${:.2f}.' .format(final))
else:
    aumento = (salario * 15) / 100
    final = salario + aumento
    print('O salário com aumento é R${:.2f}.' .format(final))