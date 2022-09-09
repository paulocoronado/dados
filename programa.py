from Dado import *

dado_1=Dado()
dado_2=Dado()

dado_1.rodar()
dado_2.rodar()

if dado_1.valor+dado_2.valor==7:
    print("Eres muy bueno!!")
else:
    print("Eres muy malo!!")


