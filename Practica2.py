import math
import numpy as np


# Funcion que separa el mensaje en bloques de 7 digitos
def genera_cod2(msj_entrada):
    palabra = []
    lista_cod2 = []
    count = 0

    # Bucle que recorre todos los caracteres del mensaje
    for i in range(len(msj_entrada)):

        # Agrupa los digitos de 7 en 7
        palabra.append(int(msj_entrada[i]))
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
    # print(lista_bloques)
    lista_letras = ""
    str_aux = ""
    count = 0
    for i in range(len(lista_bloques)):
        str_aux += str(lista_bloques[i])
        count += 1
        if count == long_min:
            # print(str_aux)
            lista_letras += alfabeto[int(str_aux,2)]
            str_aux = ""
            count = 0

    return lista_letras


def calcula_matriz_sindrome(msj):
    # Calcula la matriz que contiene los síndromes de cada una de las palabras código
    m_control_hamming = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    cod2 = genera_cod2(msj)
    m_msj = np.transpose(np.array([cod for cod in cod2]))

    m_sindrome = m_control_hamming.dot(m_msj)

    for fila in m_sindrome:
        for i, num in enumerate(fila):
            if num % 2 == 0:
                fila[i] = 0
            else:
                fila[i] = 1

    return m_sindrome


def calcula_pos_sindrome(m_sindrome):
    # Calcula la posición equivalente a cada uno de los síndrome, en decimal
    m_sind_trasp = np.transpose(m_sindrome)

    lista_pos = []
    
    for fila in m_sind_trasp:
        res = 0
        for i, num in enumerate(fila):
            res += num * 2 ** (len(fila) - i - 1)

        lista_pos.append(res)

    return lista_pos

msj_entrada = "00001010100110110111101011010111111"
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ,.-;()0123456789abcdeéfghiíjklmnñoópqrstuvwxyz"
long_min = int(math.log2(len(alfabeto))) + 1

ruido = "si" == input("¿Hay ruido?: ").lower()

if ruido:
    calcula_pos_sindrome(calcula_matriz_sindrome(msj_entrada))

else:
    print(genera_msj(elimina_sobrantes(genera_cod2(msj_entrada))))