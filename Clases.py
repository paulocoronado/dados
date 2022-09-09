import math

class Calculadora:

    def sumar(self, a,b):
        return a+b    

    def restar(self, a,b):
        return a-b

    def multiplicar(self, a,b):
        return a*b

    def dividir(self, a,b):
        return a/b

class CalculadoraTrigonometrica(Calculadora):

    def seno(self,a):
        return math.sin(a)

    def coseno(self,a):
        return math.cos(a)

    def tangente(self,a):
        return math.tan(a)

class CalculadoraConversion(CalculadoraTrigonometrica):

    def fahrenheit2celsius(self,a):
        #Convertir grados fahrenheit a celsius
        return (a-32)/1.8
    
    def pulgadas2centimetros(self, a):
        return a*2.54










