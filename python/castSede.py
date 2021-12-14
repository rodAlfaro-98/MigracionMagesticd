import Sede as S
import pandas as pd

def getSedes():
    catalogo = pd.ExcelFile('../Sedes.xlsx')
    registros = catalogo.parse(0)

    registros_sede = {}
    count = 0
    recuperado = []
    campos = registros.keys().tolist()

    campos_sede = {}
    for campo in campos:
        campos_sede[campo] = registros[campo]

    count_max = 0
    for row in registros.index:
        count_max += 1

    for count in range(0,count_max):
        vars = []
        for llave in campos_sede:
            vars.append(campos_sede[llave][count])
        S.Sede.count = count+1
        registro = S.Sede(vars)
        registros_sede[count]=registro
    return registros_sede

f = open("../Sedes.csv","w",encoding='utf-8')
registros_sede = getSedes()
for registro in registros_sede:
    f.write(str(registros_sede[registro]))
f.close()
