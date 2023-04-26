def run():
    mi_Diccionario = {
        'Argentina': 44_938_712,
         'Brazil': 210_147_125 , 
         'Colombia': 50_372_434
         }
    # print(mi_Diccionario['Argentina'])
    # print(mi_Diccionario['Brazil'])
    # print(mi_Diccionario['Colombia'])
    # for pais in mi_Diccionario.keys():
    #     print(pais)
    # for pais in mi_Diccionario.values():
    #     print(pais)
    for pais, poblacion in mi_Diccionario.items():
        print(pais + ' tiene ' + str(poblacion)+ ' habitantes')
        

if __name__ == '__main__':
    run()