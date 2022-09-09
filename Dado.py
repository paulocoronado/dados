import random

class Dado:

    def __init__(self):
        
        self.valor=0



    def rodar(self):
        self.valor= random.randint(1,6)
        return self.valor
