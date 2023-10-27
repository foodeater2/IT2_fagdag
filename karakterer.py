#blandede oppgaver

import numpy as np
import matplotlib.pyplot as plt

#oppgave 1
xverdier = np.linspace(1,6,6)
Klassekarakterer = [5, 3, 6, 3, 5, 1, 2, 2, 2, 4, 2, 2, 5, 5, 6, 3, 5, 3, 5, 4, 2, 6, 1, 4, 2, 3, 3, 3, 5, 5]
yverdier = [0,0,0,0,0,0]

for x in Klassekarakterer:
    print(x)
    yverdier[x-1] = yverdier[x-1] + 1
    

#first row, first column
ax1 = plt.subplot2grid((2,2),(0,0))
plt.pie(yverdier, labels=xverdier)
plt.title('Karakterer')

#first row sec column
ax1 = plt.subplot2grid((2,2), (0, 1))
plt.bar(xverdier, yverdier)
plt.title('Karakterer bar')

plt.grid()