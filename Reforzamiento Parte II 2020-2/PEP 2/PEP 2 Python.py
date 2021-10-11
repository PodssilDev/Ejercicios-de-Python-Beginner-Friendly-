# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 
# PROFESOR DE TEORÍA: 
# PROFESOR DE LABORATORIO: 
#
# AUTOR
# NOMBRE: 
# RUT: 
# CARRERA: 
# DESCRIPCIÓN DEL PROGRAMA

# BLOQUE DE DEFINICION
# IMPORTACIONES
from Jojojo import leer_archivo
from Jojojo import escribir_archivo
# CONSTANTES
# FUNCIONES

# BLOQUE PRINCIPAL
# ENTRADA
bondad = leer_archivo("bondad.txt")
pedidos = leer_archivo("pedidos.txt")
# PROCESAMIENTO
i = 0
ninos_bondad = []
promedios_bondad = []
ninos_pedidos = []
listado_final = []
regalos = []
while i < len(bondad):
    promedio = 0
    linea = bondad[i]
    lista_linea = linea.split(",")
    j = 1
    ninos_bondad.append(lista_linea[0])
    while j < len(lista_linea):
        nota = float(lista_linea[j])
        promedio = promedio + nota
        j += 1
    promedio = promedio / 12
    promedio = round(promedio,1)
    promedios_bondad.append(promedio)
    i += 1

k = 0
while k < len(pedidos):
    linea = pedidos[k]
    lista_linea = linea.split(",")
    if lista_linea[0] not in ninos_bondad:
        del pedidos[k]
    else:
        ninos_pedidos.append(lista_linea[0])
    k+=1
n = 0
cant_regalos = []
while n < len(promedios_bondad):
    if promedios_bondad[n] < 4.0:
        # Se agrega un 0 a la lista de cantidad_regalos
        cant_regalos.append(0)
    # Si la bondad promedio esta entre 4.0 y 4.9 (limites incluidos)
    elif promedios_bondad[n] < 5.0:
        # Se agrega un 1 a la lista de cantidad_regalos
        cant_regalos.append(1)
    # Si la bondad promedio esta entre 5.0 y 5.4 (limites incluidos)
    elif promedios_bondad[n] < 5.5:
        # Se agrega un 2 a la lista de cantidad_regalos
        cant_regalos.append(2)
    # Si la bondad promedio esta entre 5.5 y 5.9 (limites incluidos)
    elif promedios_bondad[n] < 6.0:
        # Se agrega un 3 a la lista de cantidad_regalos
        cant_regalos.append(3)
    # Si la bondad promedio esta entre 6.0 y 6.4 (limites incluidos)
    elif promedios_bondad[n] < 6.5:
        # Se agrega un 4 a la lista de cantidad_regalos
        cant_regalos.append(4)
    # Si la bondad promedio esta entre 6.5 y 7.0 (limites incluidos)
    else:
        # Se agrega un 5 a la lista de cantidad_regalos
        cant_regalos.append(5)
    # Incremento i en 1 para continuar recorriendo la lista
    n += 1
print(cant_regalos)
e = 0
while e < len(cant_regalos):
    if cant_regalos[e] >= 1 and ninos_bondad[e] not in ninos_pedidos:
        cadena = ninos_bondad[e] + ", bicicleta\n"
        listado_final.append(cadena)
        ninos_bondad.pop(e)
        cant_regalos.pop(e)
    e+=1
c = 0
while c < len(cant_regalos):
    if cant_regalos[c] == 0:
        cadena = ninos_bondad[c] + ", carbon\n"
        listado_final.append(cadena)
        pedidos.pop(c)
        ninos_bondad.pop(c)
        cant_regalos.pop(c)
    c += 1
z = 0
while z < len(pedidos):
    linea_actual = pedidos[z]
    linea_actual = linea_actual.split(",")
    if cant_regalos[z] > len(linea_actual) - 1:
        diferencia = cant_regalos[z] - (len(linea_actual)- 1)
        cant_regalos[z] = cant_regalos[z] - diferencia
    cadena = linea_actual [0] + ","
    v = 1
    while cant_regalos[z] != 0:
        if cant_regalos[z] == 1 and "\n" not in linea_actual[v]:
            cadena = cadena + linea_actual[v] + "\n"
        elif cant_regalos[z] == 1 and "\n" in linea_actual[v]:
            cadena = cadena + linea_actual[v]
        else:
            cadena = cadena + linea_actual[v] + ","
        cant_regalos[z] = cant_regalos[z] - 1
        v += 1
    listado_final.append(cadena)
    z+= 1     
# SALIDA
escribir_archivo("regalos.txt",listado_final)
