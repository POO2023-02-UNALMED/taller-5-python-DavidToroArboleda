from zooAnimales import animal


class Pez(animal):

    _listado = []
    salmones = 0 
    bacalaos = 0 

    #inicializador
    def __init__(self, nombre , edad, habitat, genero, colorEscamas,canitdadAletas) :
        super.__init__(nombre , edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = canitdadAletas

        self._listado.append(self)

    #crear Salmon
    def crearSalmon(self, nombre , edad,  genero):
        colorEscamas = "rojo"
        habitat = "oceano"
        canitdadAletas = 6
        
        a = Pez(nombre , edad, habitat,  genero, colorEscamas, canitdadAletas )

        self.salmones += 1 
        return a 
    
    #crear Bacalao
    def crearBacalao(self, nombre , edad,  genero):
        colorEscamas = "gris"
        habitat = "oceano"
        canitdadAletas = 6
        
        a = Pez(nombre , edad, habitat,  genero, colorEscamas, canitdadAletas )

        self.bacalaos += 1 
        return a 
    
    #cantidad mamiferos
    @classmethod
    def cantidadPeces():
        return len(Pez._listado)
    
    #getters n setters

    def setListado(self, listado):
        self._listado = listado

    def getListado(self):
        return self._listado
    
    def setColorEscamas(self, colorPiel):
        self._colorEscamas = colorPiel

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self , venenoso):
        self._cantidadAletas = venenoso 

    def getCantidadAletas(self):
        return self._cantidadAletas