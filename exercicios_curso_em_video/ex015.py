quantdias = int(input('Por quantos dias o carro foi alugado? '))
quantkm = int(input('Quantos km o carro andou? '))

valordias = quantdias * 60
valorkm = quantkm * 0.15
valorfinal = valordias + valorkm

print('O valor total a ser pago é R${:.2f}' .format(valorfinal))
