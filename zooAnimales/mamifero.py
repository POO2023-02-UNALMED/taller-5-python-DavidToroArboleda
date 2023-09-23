from zooAnimales import animal


class Mamifero(animal):

    _listado = []
    caballos = 0 
    leones = 0 

    #inicializador
    def __init__(self, nombre , edad, habitat, genero, pelaje, patas) :
        super.__init__(nombre , edad, habitat, genero)
        self._pelaje = pelaje 
        self._patas = patas

        self._listado.append(self)

    #crear caballo 
    def crearCaballo(self, nombre , edad,  genero):
        pelaje = True
        habitat = "pradera"
        patas = 4

        a = Mamifero(nombre , edad, habitat,  genero, pelaje , patas )

        self.caballos += 1 
        return a 
    
    #crear Leon
    def crearLeon(self, nombre , edad,  genero):
        pelaje = True
        habitat = "selva"
        patas = 4

        a = Mamifero(nombre , edad, habitat,  genero, pelaje , patas )

        self.leones += 1 
        return a 
    
    #cantidad mamiferos
    @classmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)
    
    
    #getters n setters

    def setListado(self, listado):
        self._listado = listado

    def getListado(self):
        return self._listado
    
    def setPelaje(self, colorPiel):
        self._pelaje = colorPiel

    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self , venenoso):
        self._patas = venenoso 

    def getVenenoso(self):
        return self._patas



    

        
 
    