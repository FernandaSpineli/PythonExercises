largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
totaltinta = area / 2
print('Será necessario {} litros de tinta para a parede com área de {} metros.'
      .format(totaltinta, area))

