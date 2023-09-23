class Zona():

    _zoo = []
    _animales = []

    #inicializador 
    def __init__ (self, nombre , zoo ):
        self._nombre = nombre 
        self._animales.append(zoo)

    #agregar animales
    def agregarAnimales(self, animal):
        self._animales.append(animal)

    #cantidad animales
    @classmethod
    def cantidadAnimales(cls):
        return len(cls._animales)
    
    def getZoo(self):
        return self._zoo
    
