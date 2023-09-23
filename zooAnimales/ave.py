from zooAnimales import animal


class Ave(animal):

    _listado = []
    halcones = 0 
    aguilas = 0 

    #inicializador
    def __init__(self, nombre , edad, habitat, genero, colorPlumas) :
        super.__init__(nombre , edad, habitat, genero)
        self._colorPlumas = colorPlumas

        self._listado.append(self)

    #crear Halcon
    def crearHalcon(self, nombre , edad,  genero):
        colorPlumas = "cafe glorioso"
        habitat = "montanas"
        
        a = Ave(nombre , edad, habitat,  genero, colorPlumas )

        self.halcones += 1 
        return a 
    
    #crear Aguila
    def crearAguila(self, nombre , edad,  genero):
        colorPlumas = "blanco y amarillo"
        habitat = "montanas"
        
        a = Ave(nombre , edad, habitat,  genero, colorPlumas )

        self.aguilas += 1 
        return a 
    
    #cantidad mamiferos
    @classmethod
    def cantidadAves():
        return len(Ave._listado)
    
    
    #getters n setters

    def setListado(self, listado):
        self._listado = listado

    def getListado(self):
        return self._listado
    
    def setColorPlumas(self, colorPiel):
        self._colorPlumas = colorPiel

    def getColorPlumas(self):
        return self._colorPlumas
    
