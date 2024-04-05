import math


# Funcion que separa el mensaje en bloques de 7 digitos
def genera_cod2(msj_entrada):
    palabra = []
    lista_cod2 = []
    count = 0

    # Bucle que recorre todos los caracteres del mensaje
    for i in range(len(msj_entrada)):

        # Agrupa los digitos de 7 en 7
        palabra.append(msj_entrada[i])
        count += 1
        if count > 6:
            lista_cod2.append(palabra)
            count = 0
            palabra = []

    return lista_cod2


# Funcion que elimina los 3 ultimos numeros de cada grupo de 7 digitos
def elimina_sobrantes(lista_cod2):
    lista_cod1=[]

    for i in lista_cod2:
        for j in range(3):
            del i[len(i) - 1]
        lista_cod1.extend(i)

    return lista_cod1


# Funcion que agrupa los digitos de 6 en 6, los traduce de binario a decimal, obtiene la letra y devuelve el mensaje
def genera_msj(lista_bloques):
    print(lista_bloques)
    lista_letras = ""
    str_aux = ""
    count = 0
    for i in range(len(lista_bloques)):
            str_aux += str(lista_bloques[i])
            count += 1  
            if count == long_min:
                print(str_aux)
                lista_letras += alfabeto[int(str_aux,2)]
                str_aux = ""
                count = 0
    return lista_letras


error_datos = True

while error_datos:
    msj_entrada = list(input("Introduce el mensanje: "))
    if msj_entrada is not list:
        print("ERROR. El mensaje se debe de introducir como una lista: ")
        continue

    alfabeto = input("Introduce el alfabeto: ")
    if alfabeto is not str:
        print("ERROR. El mensaje se debe de introducir como una lista: ")
        continue


long_min = int(math.log2(len(alfabeto))) + 1


print(long_min)
print(genera_msj(elimina_sobrantes(genera_cod2(msj_entrada))))