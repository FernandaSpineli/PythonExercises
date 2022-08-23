class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


try:
    lista = [1, 10]
    divisao = 10 / 1
    numero = lista[3]
except ZeroDivisionError:
    print('Não é possivel efetuar uma divisão por 0.')
except IndexError:
    print('Erro ao acessar índice inválido.') 
except BaseException as ex:
    print('Erro desconhecido. Descrição automática: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
   
    
while True:   
    try:
        x = int(input('Digite um número de 0 a 10:'))
        print(x)
        if x > 10:
            raise InputError('Número não pode ser maior que 10.')
        break
    except ValueError:
            print('Valor inválido. Digite apenas números.')
    
