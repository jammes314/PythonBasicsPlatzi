def EsPrimo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador += 1
    if contador >= 0 or numero == 1:
        return False
    else:
        return True

def run():
    numero = int(input('escribe un numero: '))
    if EsPrimo(numero): 
        print('El numero es primo')
    else:
        print('El numero no es primo')


if __name__ == '__main__':
    run() 