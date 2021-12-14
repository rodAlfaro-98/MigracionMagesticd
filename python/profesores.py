class Profesor:
    count = 0

    def __init__(self,vars):
        self.pk = self.count 
        self.nombres = vars[6]
        apellidos = vars[5].split()
        self.apellido_paterno = apellidos[0]
        self.apellido_materno = ""
        for apellido in apellidos[:0]:
            self.apellido_materno += apellido+" "
        self.rfc = vars[1]
        self.numero_trabajador = vars[2]
        self.fecha_nacimiento = ""
        self.telefono = vars[12]
        self.grado = vars[16]
        self.abreviatura_grado = vars[17]
        self.email = vars[11]
        if(vars[33] == True):
            self.genero = "femenino"
        else:
            self.genero = "masculino"
        self.baja = vars[50]
        self.semblanza_corta = vars[42]
        self.facebook = vars[len(vars)-1]
        self.unam = False if vars[22] == True else True
        self.procedencia = vars[14]
        self.facultad_id = ""
    
    def __str__(self):
        toReturn = ""
        toReturn += str(self.pk)+","
        toReturn += self.nombres+"," if(self.nombres != ""and isinstance(self.nombres,str)) else ","
        toReturn += self.apellido_paterno+"," if(self.apellido_paterno != ""and isinstance(self.apellido_paterno,str)) else ","
        toReturn += self.apellido_materno+"," if(self.apellido_materno != ""and isinstance(self.apellido_materno,str)) else ","
        toReturn += self.rfc+"," if(self.rfc != ""and isinstance(self.rfc,str)) else ","
        toReturn += self.numero_trabajador+"," if(self.numero_trabajador != ""and isinstance(self.numero_trabajador,str)) else ","
        toReturn += self.fecha_nacimiento+"," if(self.fecha_nacimiento != ""and isinstance(self.fecha_nacimiento,str)) else ","
        toReturn += str(self.telefono)+"," if(self.telefono != 0) else ","
        toReturn += self.grado+"," if(self.grado != ""and isinstance(self.grado,str)) else ","
        toReturn += self.abreviatura_grado+"," if(self.abreviatura_grado != ""and isinstance(self.abreviatura_grado,str)) else ","
        toReturn += self.email+"," if(self.email != ""and isinstance(self.email,str)) else ","
        toReturn += self.genero+"," if(self.genero != ""and isinstance(self.genero,str)) else ","
        toReturn += self.baja+"," if(self.baja != ""and isinstance(self.baja,str)) else ","
        toReturn += self.semblanza_corta+"," if(self.semblanza_corta != ""and isinstance(self.semblanza_corta,str)) else ","
        toReturn += self.facebook+"," if(self.facebook != ""and isinstance(self.facebook,str)) else ","
        toReturn += str(self.unam)+"," 
        toReturn += self.procedencia+"," if(self.procedencia != ""and isinstance(self.procedencia,str)) else ","
        toReturn += self.facultad_id+","
        toReturn+="\n"
        return toReturn

    def getRFC(self):
        return self.rfc