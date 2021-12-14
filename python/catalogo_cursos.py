import pandas as pd

class Catalogo_Cursos:
    contador = 0

    def __init__(self,vars):
        self.pk = self.contador
        self.clave_curso = vars[0] 
        self.clave_coordinacion = vars[1]
        self.nombre_curso = vars[2]
        self.tipo_curso = vars[3]
        self.tipo_diploma = vars[4]
        self.antecedentes = vars[5]
        self.consecuentes = vars[6]
        self.fecha_disenio = vars[7]
        self.presentacion = vars[8]
        self.objetivo = vars[9]
        self.contenido = vars[10]
        self.metodologia = vars[11]
        self.duracion = vars[12]

    def __str__(self):
        toReturn = ""
        toReturn += str(self.pk)+","
        if(self.clave_curso != ""and isinstance(self.clave_curso,str)):
            toReturn += self.clave_curso+","
        else:
            toReturn += ","
        if(self.clave_coordinacion != "" and isinstance(self.clave_coordinacion,str)):
            toReturn += self.clave_coordinacion+","
        else:
            toReturn += ","
        if(self.nombre_curso != "" and isinstance(self.nombre_curso,str)):
            toReturn += self.nombre_curso+","
        else:
            toReturn += ","
        if(self.tipo_curso != "" and isinstance(self.tipo_curso,str)):
            toReturn += self.tipo_curso+","
        else:
            toReturn += ","
        if(self.antecedentes != "" and isinstance(self.antecedentes,str)):
            temp = self.antecedentes.split("\n")
            for val in temp:
                toReturn += val
            toReturn += ","
        else:
            toReturn += ","
        temp = pd.to_datetime(self.fecha_disenio, errors='coerce')
        toReturn += str(temp)+"," if(not pd.isnull(temp)) else ","
        if(self.objetivo != ""  and isinstance(self.objetivo,str)):
            temp = self.objetivo.split("\n")
            for val in temp:
                toReturn += val
            toReturn += ","
        else:
            toReturn += ","
        if(self.contenido != ""and isinstance(self.contenido,str)):
            temp = self.contenido.split("\n")
            for val in temp:
                toReturn += val
            toReturn += ","
        else:
            toReturn += ","
        if(self.duracion != 0):
            toReturn += str(self.duracion)+","
        else:
            toReturn += ","
        return toReturn+"\n"
    
    def getCVECurso(self):
        return self.clave_curso