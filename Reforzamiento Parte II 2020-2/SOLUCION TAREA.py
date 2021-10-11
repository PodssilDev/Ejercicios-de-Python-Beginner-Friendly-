def tiene_restriccion(registro, patente, dia):
    i = 0
    while i < len(registro):
        if patente in registro[i][0]:
            lista_correcta = registro[i]
            patente_correcta = lista_correcta[0]
            catalitico = lista_correcta[3]
            if catalitico == True:
                if patente_correcta[2] == "-":
                    ultima_letra = patente_correcta[1]
                else:
                    ultima_letra = patente_correcta[3]
                if dia == "LUNES":
                    if ultima_letra <= "G":
                        return True
                    else:
                        return False
                elif dia == "MIERCOLES":
                    if ultima_letra > "G" and ultima_letra <= "N":
                        return True
                    else:
                        return False
                elif dia == "VIERNES":
                    if ultima_letra > "N":
                        return True
                    else:
                        return False
                else:
                    return False
            elif catalitico == False:
                ultimo_numero = patente_correcta[6]
                if dia == "LUNES":
                    if ultimo_numero == "0" or ultimo_numero == "1" or ultimo_numero == "2" or ultimo_numero == "3":
                        return True
                    else:
                        return False
                elif dia == "MIERCOLES":
                    if ultimo_numero == "4" or  ultimo_numero == "5" or ultimo_numero ==  "6":
                        return True
                    else:
                        return False
                elif dia == "VIERNES":
                    if ultimo_numero == "7" or ultimo_numero == "8" or ultimo_numero == "9":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return "Hay un error en registro"
        else:
            i += 1
            

registro = [
['CRTJ 32', 'Valpyraiso', 'Juan Perez', True],
['RX-2134', 'Sanpyago', 'Ana Martinez', False],
['ADNT 28', 'Pyna del Mar', 'Fernanda Jara', False],
['ZZ-9999', 'Pyca', 'Pedro Allende', True],
['AK-2130', 'Sanpyago', 'Paloma Blanco', True],
['ABCD 19', 'Copymbo', 'Ana Roa', False]]
booleano = tiene_restriccion(registro,"ZZ-9999", "VIERNES")
print(booleano)
