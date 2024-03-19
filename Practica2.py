import math


msj_entrada = [0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1]
print(len(msj_entrada))
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ,.-;()0123456789abcdeéfghiíjklmnñoópqrstuvwxyz"

long_min = int(math.log2(len(alfabeto)))

#Funcion que separa el mensaje en bloques de 7 digitos
def generaCod2(msj_entrada):
    palabra = []
    listaCod2 = []
    count = 0

    #Bucle que recorre todos los caracteres del mensaje
    for i in range(len(msj_entrada)):

        #Agrupa los digitos de 7 en 7
        palabra.append(msj_entrada[i])
        count += 1
        if count > 6:
            listaCod2.append(palabra)
            count = 0
            palabra = []
        

    return listaCod2

#Funcion que elimina los 3 ultimos numeros de cada grupo de 7 digitos
def eliminaSobrantes(listaCod2):
    listaCod1=[]

    for i in listaCod2:
        for j in range(3):
            del i[len(i) - 1]
        listaCod1.extend(i)

    return listaCod1

#Funcion que agrupa los digitos de 6 en 6, los traduce de binario a decimal, obtiene la letra y devuelve el mensaje
def generaMsj(listaBloques):
    print(listaBloques)
    listaLetras = ""
    strAux = ""
    count = 0
    for i in range(len(listaBloques)):
            strAux += str(listaBloques[i])
            count += 1  
            if count == long_min:
                print(strAux)
                listaLetras += alfabeto[int(strAux,2)]
                strAux = ""
                count = 0
    return listaLetras

print(generaMsj(eliminaSobrantes(generaCod2(msj_entrada))))