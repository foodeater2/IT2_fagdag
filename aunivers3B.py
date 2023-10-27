#oppgave csv baby

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rows = []
col = []

with open("./fritidsboliger_moh_2019.csv", 'r', encoding="ISO-8859-1") as file:
  filinnhold = csv.reader(file, delimiter=";")
  overskrifter = next(filinnhold)
  print(overskrifter)
  for rad in filinnhold:
    rows.append(rad)
   
plt.grid()
plt.xlabel("$Fritidsbolig$")
plt.ylabel("$meter over havet$")
plt.barh(overskrifter, rows[0])