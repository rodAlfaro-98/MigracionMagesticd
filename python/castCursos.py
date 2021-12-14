import castCatalogoCursos as castCc
import cursos as C
import pandas as pd
import castSede as castS

cursos = pd.ExcelFile('../Cursos.xlsx')
registros = cursos.parse(0)

registros_cursos = {}
count = 0
recuperado = []
campos = registros.keys().tolist()

registros_catalogo = castCc.getCatalogo()
registros_sede = castS.getSedes()

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
    C.Curso.count = count+1
    registro = C.Curso(vars)
    registros_cursos[count]=registro
    fk = 0
    for catalogo in registros_catalogo:
        if(registros_catalogo[catalogo].getCVECurso() == vars[1]):
            fk = catalogo + 1
            break
    registros_cursos[count].setCatalogoId(fk)
    for sede in registros_sede:
        if(registros_sede[sede].getSede() == vars[3]):
            fk = sede + 1
            break
    registros_cursos[count].setSedeId(fk)

f = open("../Cursos.csv","w",encoding='utf-8')
for registro in registros_cursos:
    f.write(str(registros_cursos[registro]))
f.close()