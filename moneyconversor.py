def money_change_to_dollars(moneda, cantidad):
  
    result = 0 
    # moneda chilena
    if moneda == 1:
        result = cantidad * 0.0013 
        print(f'Los {cantidad} de pesos chilenos equivalen a {result} dolares')
    # moneda colombiana
    elif moneda == 2:
        result = cantidad * 0.00027
        print(f'Los {cantidad}  de pesos colombianos a {result} dolares')
    # moneda argentina 
    elif moneda == 3:
        result = cantidad * 0.014
        print(f'Los {cantidad} de pesos argentinos a {result} dolares')
    # moneda mexicana 
    elif moneda == 4:
        result = cantidad * 0.044
        print(f'Los {cantidad} de pesos mexicanos a {result} dolares')
    else: 
        print('Ingresa solo un numero de la lista')
if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda chilena a Dolar
            [2] Moneda colombiana a Dolar
            [3] Moneda argentida a Dolar
            [4] Moneda mexicana a Dolar
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda,cantidad)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')