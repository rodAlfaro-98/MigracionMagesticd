import pandas as pd
from datetime import datetime

class Curso:
    count = 0
    
    def __init__(self,vars):
        self.pk = self.count
        semestre = vars[0].split("-")
        self.semestre_anio = semestre[0]
        self.semestre_pi = semestre[1][0]
        self.semestre_si = semestre[1][1]
        self.fecha_inicio = vars[10]
        self.fecha_fin = vars[11]
        self.hora_inicio = vars[12]
        self.hora_fin = vars[13]
        self.dias_semana = vars[14]
        self.numero_sesiones = vars[16]
        self.sesiones = vars[15]
        self.acreditacion = ""
        self.costo = ""
        self.cupo_maximo = vars[30]
        self.cupo_minimo = vars[31]
        self.fecha_envio_constancia = ""
        self.fecha_envio_reconocimiento = ""
        self.num_modulo = ""
        self.catalogo_id = ""
        self.salon_id = vars[4]
        self.diplomado_id = ""

    def __str__(self):
        toReturn = str(self.pk) +","
        toReturn += self.semestre_anio +","
        toReturn += self.semestre_pi +","
        toReturn += self.semestre_si +","
        temp = pd.to_datetime(self.fecha_inicio, errors='coerce')
        toReturn += str(temp)+"," if(not pd.isnull(temp)) else ","
        temp = pd.to_datetime(self.fecha_fin, errors='coerce')
        toReturn +=  str(temp)+"," if(not pd.isnull(temp)) else ","
        toReturn += self.hora_inicio.strftime("%H:%M") +","  if( not isinstance(self.hora_inicio,float)) else ","
        toReturn += self.hora_fin.strftime("%H:%M") +"," if( not isinstance(self.hora_fin,float)) else ","
        toReturn += self.dias_semana +"," if(isinstance(self.dias_semana,str)) else ","
        toReturn += str(self.numero_sesiones )+","
        toReturn += str(self.sesiones) +","
        toReturn += self.acreditacion +","
        toReturn += self.costo +","
        toReturn += str(self.cupo_maximo)+","
        toReturn += str(self.cupo_minimo)+","
        toReturn += self.fecha_envio_constancia +","
        toReturn += self.fecha_envio_reconocimiento +","
        toReturn += self.num_modulo +","
        toReturn += str(self.catalogo_id)+","
        toReturn += str(self.salon_id)
        toReturn += str(self.diplomado_id)
        toReturn += "\n"
        return toReturn

    def setCatalogoId(self,catalogo_id):
        self.catalogo_id = catalogo_id
    
    def setSedeId(self,sede_id):
        self.salon_id = sede_id

    def getCursoId(self):
        return self.pk