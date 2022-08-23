from codecs import _WritableStream


lista = [1, 3, 5, 7]

multiLista = lista * 2
print(multiLista)

print(sum(lista))
print(max(lista))
print(min(lista))

if 8 in lista:
    print('Existe o número 5 na lista.')
else:
    print('Precisa ser adicionado na lista.')
    lista.append(8)
    
print(lista)

lista.pop(2)

lista.remove(8)

lista.sort()
print(lista)

lista.reverse()
print(lista)


tupla = (1, 10, 12, 14)
tupla_numerica = tuple(lista)

list_tupla = list(tupla)
