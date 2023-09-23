from zooAnimales import animal


class Anfibio(animal):

    _listado = []
    ranas = 0 
    salamandras = 0 

    #inicializador
    def __init__(self, nombre , edad, habitat, genero, colorPiel,venenoso) :
        super.__init__(nombre , edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

        self._listado.append(self)

    #crear rana
    def crearRana(self, nombre , edad,  genero):
        colorPiel = "rojo"
        habitat = "selva"
        venenoso = True
        
        a = Anfibio(nombre , edad, habitat,  genero, colorPiel, venenoso )

        self.ranas += 1 
        return a 
    
    #crear salamandra
    def crearSalamandra(self, nombre , edad,  genero):
        colorPiel = "negro y amarillo"
        habitat = "selva"
        venenoso = False
        
        a = Anfibio(nombre , edad, habitat,  genero, colorPiel, venenoso )

        self.salamandras += 1 
        return a  
    
    #cantidad mamiferos
    @classmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    #getters n setters

    def setListado(self, listado):
        self._listado = listado

    def getListado(self):
        return self._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self , venenoso):
        self._venenoso = venenoso 

    def getVenenoso(self):
        return self._venenoso
    

