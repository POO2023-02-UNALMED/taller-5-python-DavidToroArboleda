from zooAnimales import animal


class Reptil(animal):

    _listado = []
    iguanas = 0 
    serpientes = 0 

    #inicializador
    def __init__(self, nombre , edad, habitat, genero, colorEscamas,largoCola) :
        super.__init__(nombre , edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

        self._listado.append(self)

    #crear iguana
    def crearIguana(self, nombre , edad,  genero):
        colorEscamas = "verde"
        habitat = "humedal"
        largoCola = 3
        
        a = Reptil(nombre , edad, habitat,  genero, colorEscamas, largoCola )

        self.iguanas += 1 
        return a 
    
    #crear sSerpiente
    def crearSerpiente(self, nombre , edad,  genero):
        colorEscamas = "blanco"
        habitat = "jungla"
        largoCola = 1
        
        a = Reptil(nombre , edad, habitat,  genero, colorEscamas, largoCola )

        self.serpientes += 1 
        return a 
    
    #cantidad mamiferos
    @classmethod
    def cantidadReptiles():
        return len(Reptil._listado)
    
    #getters n setters

    def setListado(self, listado):
        self._listado = listado

    def getListado(self):
        return self._listado
    
    def setColorEscamas(self, colorPiel):
        self._colorEscamas = colorPiel

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self , venenoso):
        self._largoCola = venenoso 

    def getVenenoso(self):
        return self._largoCola