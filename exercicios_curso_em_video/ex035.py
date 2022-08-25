frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto)-1, -1, -1):
    inverso += junto[l]
print(junto, inverso)
