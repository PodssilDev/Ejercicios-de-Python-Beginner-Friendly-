# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO:
# PROFESOR DE TEORÍA:
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE:
# RUT:
# CARRERA: Ingeniería Civil Informática
# DESCRIPCIÓN DEL PROGRAMA:

# BLOQUE DE DEFINICIÓN
# CONSTANTES
LETRA = ['A', 'B', 'C', 'CH', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K', 'L', 'LL',
         'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
         'RR', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '?']
VALOR = [1, 3, 3, 5, 2, 1, 4, 2, 4, 1, 8, 8,
         1, 8, 3, 1, 8, 1, 3, 5, 1, 8, 1, 1, 1,
         4, 10, 8, 4, 10, 0]
# ENTRADA
lista_palabras = eval(input("Ingrese una lista con las palabras que desee: "))
# PROCESAMIENTO
lista_puntajes = []
i = 0
j = 0
posicion = 0
suma = 0
while i < len(lista_palabras):
    palabra = lista_palabras[i].upper()
    while j < len(palabra):
        letra = palabra[j]
        if letra == "C" and palabra.index(letra) != len(palabra) - 1:
            if palabra[j+1] == "H":
                posicion = 3
                j +=1
            else:
                posicion = LETRA.index(palabra[j])
        elif letra == "L" and palabra.index(letra) != len(palabra) - 1:
            if palabra[j+1] == "L":
                posicion = 13
                j +=1
            else:
                posicion = LETRA.index(palabra[j])
        elif letra == "R" and palabra.index(letra) != len(palabra) - 1:
            if palabra[j+1] == "R":
                posicion = 21
                j +=1
            else:
                posicion = LETRA.index(palabra[j])
        else:
            posicion = LETRA.index(palabra[j])
        suma = suma + VALOR[posicion]
        j +=1
    lista_puntajes.append(suma)
    suma = 0
    j = 0
    i+=1

mayor = 0
i = 0
while i < len(lista_puntajes):
    if lista_puntajes[i] > mayor:
        mayor = lista_puntajes[i]
    i += 1

posicion_mayor = lista_puntajes.index(mayor)
mejor_palabra = lista_palabras[posicion_mayor].upper()              
# SALIDA
print("La palabra con mayor puntaje es:", mejor_palabra , "con", mayor, "puntos")

