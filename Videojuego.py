
import random


def run():
    randomNumber = random.randint(0,100)
    
    chosenNumber = int(input("Enter a number from 1 to 100: "))
    while chosenNumber != randomNumber:
        if chosenNumber < randomNumber:
            print('busca un numero mas grande')
        else:
            print('busca un numero mas pequenio')
        chosenNumber = int(input("Enter another number from 1 to 100: "))

    print('Ganaste!!')



if __name__ == '__main__':
    run()