# -*- coding: cp1252 -*-
# Calcula los primeros n t�rminos de una serie

# DATOS DE ENTRADA
# Solicita un n�mero
numero = int(input("Ingrese el n�mero de t�rminos de la serie: "))
# Inicializa la variable iteradora
k = 1
# Inicializa la variable acumuladora
suma = 0

# PROCESAMIENTO
while k <= numero:
    # Calcula los resultados parciales
    suma = suma + ((k ** 2 + 2)/(k ** 3 + 6 * k))
    # Incremeta el iterador
    k = k + 1

# SALIDA
print("La suma de los primeros", numero, "t�rminos de la serie es: ", suma)
