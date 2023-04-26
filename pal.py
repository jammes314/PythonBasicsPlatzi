def palindrome(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.upper()
    if palabra == palabra[: : - 1]:
        return True
    else:
        return False


    palabra = input('escribe una palabra: ')
    IsItaPalindrome = palindrome(palabra)

    if IsItaPalindrome == True:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')
 



if __name__ == '__main__':
    run()