

from http.client import CONTINUE


def run():
    LIMIT = 10000
    
    contador = 0 
    potenciaDe2 = 2**contador
    

    while potenciaDe2 < LIMIT:
        print("2 elevado a" + str(contador) + "es igual a " + str(potenciaDe2) )
        contador = contador + 1
        potenciaDe2 = 2**contador
if __name__ == '__main__':
    run()