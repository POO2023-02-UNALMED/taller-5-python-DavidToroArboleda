from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Animal():
    
    _totalAnimales = 0
    _zona = []
     
    #inicializador
    def __init__(self, nombre , edad, habitat, genero) :
        self._nombre = nombre
        self._edad = edad 
        self._habitat = habitat
        self._genero = genero

        self._totalAnimales += 1


    #cantidad Total Animales
    def cantidadTotalAnimales(self):
        contador = 0
        for i in range(0, len(self._zona)):
            if self._zona[i] == Zona:
                contador += Zona.cantidadAnimales
        
        return contador
    

    #total por tipo
    def totalPorTipo():
        return "Mamiferos: " + Mamifero.cantidadMamiferos + "\nAves: " + Ave.cantidadAves + "\nReptiles: "+ Reptil.cantidadReptiles+"\nPeces: " + Pez.cantidadPeces + "\nAnfibios: " + Anfibio.cantidadAnfibios

    #to String
    def toString(self):
        if self._zona[0] == None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de "+ self._edad +", habito en " + self._habitat + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de "+ self._edad +", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona[0] + ", en el " + Zona.getZoo[0]

