velocidade = int(input('Digite a velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Velocidade acima do limite de 80km/h \n recebeu uma multa de R$ {},00.'
          .format(multa))
else:
    print('Velocidade dentro do limite.')