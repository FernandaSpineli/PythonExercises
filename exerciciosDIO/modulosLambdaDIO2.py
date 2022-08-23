from unicodedata import name


def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

coontador_letras = lambda lista: [len(x) for x in lista]

soma = lambda a, b: a + b
print(soma(5, 6))

if __name__ == '__main__':
    lista = ['Cachorro', 'Gato']
    print(contador_letras(lista))

    