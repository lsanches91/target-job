entrada = input('Digite a palavra que deseja inverter: ')
tamanho = len(entrada)
pilha = []

for i in entrada:
    pilha.append(i)

index = 0
resultado = ''
while index < tamanho:
    print(pilha.pop(), end='')
    index += 1

print(resultado)
