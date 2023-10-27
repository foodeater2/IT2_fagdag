#blandede oppgaver

import numpy as np
import matplotlib.pyplot as plt
import math as m

#fibbonachos quest

def fibbonachos(x):#vanlig rekursiv fibbonachos sekvens
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    return fibbonachos(x-1)+fibbonachos(x-2)

def fiboround(x):#en matematisk funksjon for en tilnærmet fibbonacho sekvens
    if x >= 0:
        b = (1 + m.sqrt(5))/2
        return b**x/m.sqrt(5) #ikke avrundet her, så det er en tilnærming (veldig presis)
    else:
        return 0

for x in range(20):
    print("normal recursive:",fibbonachos(x), "for x =", x)
    print("round fiboonacho:",round(fiboround(x)), "for x =", x)
    
for x in range(100):
    print("round fiboonacho:",round(fiboround(x)), "for x =", x)
    #mye kjappere
    