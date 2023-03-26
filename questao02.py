entrada = int(input('Digite o número que deseja buscar: '))
penultimo = 1
ultimo = 1

if(entrada == 0) or (entrada == 1) or (entrada == 2):
    print('O número {} pertence a sequência de Fibonacci.'.format(entrada))
else:
    index = 3
    num = penultimo + ultimo
    while num < entrada:
        num = penultimo + ultimo
        penultimo = ultimo
        ultimo = num
        index += 1
    if num == entrada:
        print('O número {} pertence a sequência de Fibonacci.'.format(entrada))
    else:
        print('O número {} NÃO pertence a sequência de Fibonacci.'.format(entrada))
    