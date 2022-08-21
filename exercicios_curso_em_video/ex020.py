nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em letras maiusculas {}.' .format(nome.upper()))
print('Nome em letras maiusculas {}.' .format(nome.lower()))
print('Seu nome tem {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.' .format(nome.find(' ')))
