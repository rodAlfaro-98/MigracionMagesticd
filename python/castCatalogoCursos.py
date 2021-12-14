import catalogo_cursos as Cc
import pandas as pd

def getCatalogo():
    catalogo = pd.ExcelFile('../CatalogoCursos.xlsx')
    registros = catalogo.parse(0)

    registros_catalogo = {}
    count = 0
    recuperado = []
    campos = registros.keys().tolist()

    campos_catalogo = {}
    for campo in campos:
        campos_catalogo[campo] = registros[campo]

    count_max = 0
    for row in registros.index:
        count_max += 1

    for count in range(0,count_max):
        vars = []
        for llave in campos_catalogo:
            vars.append(campos_catalogo[llave][count])
        Cc.Catalogo_Cursos.contador = count+1
        registro = Cc.Catalogo_Cursos(vars)
        registros_catalogo[count]=registro
    return registros_catalogo

f = open("../CatalogoCursos.csv","w",encoding='utf-8')
registros_catalogo = getCatalogo()
for registro in registros_catalogo:
    f.write(str(registros_catalogo[registro]))
f.close()