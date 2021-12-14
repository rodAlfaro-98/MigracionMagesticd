class Sede:
    count = 0

    def __init__(self,vars):
        self.pk = self.count
        self.sede = vars[0]
        self.capacidad = vars[1]
    
    def getSede(self):
        return self.sede

    def __str__(self):
        return str(self.pk) + "," + self.sede + "," + str(self.capacidad) + "\n"