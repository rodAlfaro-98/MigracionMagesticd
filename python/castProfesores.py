import profesores as p
import pandas as pd

catalogo = pd.ExcelFile('../Profesores.xlsx')
registros = catalogo.parse(0)

registros_profesores = {}
count = 0
recuperado = []
campos = registros.keys().tolist()
print(campos)
campos_profesores = {}
for campo in campos:
    campos_profesores[campo] = registros[campo]

print(campos_profesores['Mujer'][1])

count_max = 0
for row in registros.index:
    count_max += 1

for count in range(0,count_max):
    vars = []
    for llave in campos_profesores:
        vars.append(campos_profesores[llave][count])
    p.Profesor.count = count+1
    registro = p.Profesor(vars)
    registros_profesores[count]=registro

f = open("../Profesores.csv","w",encoding='utf-8')
for registro in registros_profesores:
    f.write(str(registros_profesores[registro]))
f.close()