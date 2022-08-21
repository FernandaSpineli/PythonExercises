valorproduto = float(input('Digite o valor do produto para aplicar o desconto: '))
desconto = (valorproduto * 5) / 100
valorfinal = valorproduto - desconto

print('O valor do produto com desconto de 5% é R${}' .format(valorfinal))