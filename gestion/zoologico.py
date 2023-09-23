from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio


class Zoologico():

    _zonas = []

    #inicializador 
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        
    #agregar zonas
    def agregarzonas(self, zona):
        self._zonas.append(zona)


    
    

           
                
        