import math


msj_entrada = [0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0]

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ,.-;()0123456789abcdeéfghiíjklmnñoópqrstuvwxyz"

long_min = int(math.log2(len(alfabeto)))

#Funcion que separa el mensaje en bloques de 7 digitos
def generaCod2(msj_entrada):
    palabra = []
    listaCod2 = []
    count = 0

    #Bucle que recorre todos los caracteres del mensaje
    for i in range(len(msj_entrada)):

        #Bucle que da n = 7 vueltas(nos da el codigo despues de multiplicar por la matriz generadora)
        palabra.append(msj_entrada[i])
        count += 1
        if count > 6:
            listaCod2.append(palabra)
            count = 0
            palabra = []
        

    return listaCod2

def eliminaSobrantes(listaCod2):
    listaCod1=[]

    for i in listaCod2:
        for j in range(3):
            del i[len(i) - 1]
        listaCod1.extend(i)

    return listaCod1

def generaCod1(listaCod):
    listaBloques = []
    palabra = []
    count = 0

    for i in range(len(listaCod)):
        palabra.append(listaCod[i])
        count += 1
        if count > 5:
            listaBloques.append(palabra)
            count = 0
            palabra = []

        listaBloques.append(palabra)
  
    return listaBloques

def corrigeNums(listaBloques):
    for i in range(len(listaBloques)):
        num = listaBloques[i]
        for j in range(len(num)):
            if num[0] == 0:
                del num[0]
    return listaBloques

def generaMsj(listaBloques):
    listaLetras = []
    for i in listaBloques:
        if len(i) != 0:
            strAux = ""
            for j in range(len(i)):
                strAux += str(i[j])   
            listaLetras.append(alfabeto[int(strAux,2)])
    return listaLetras

print(generaCod1(eliminaSobrantes(generaCod2(msj_entrada))))
print(generaMsj(corrigeNums(generaCod1(eliminaSobrantes(generaCod2(msj_entrada))))))