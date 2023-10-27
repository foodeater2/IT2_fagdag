#oppgave csv baby

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rows = []
col = []
inntekter = ["mindre en 8mil"]
region = ["fattige folk"]
tapere = 0
with open("./skogeiere.csv", 'r', encoding="ISO-8859-1") as file:
  filinnhold = csv.reader(file, delimiter=";")
  overskrifter = next(filinnhold)
  print(overskrifter)
  for rad in filinnhold:
    try:
        if rad[0]=="Bruttoinntekt":
            print("brutto")
            print(rad[12])
            if (rad[12]<200000):
                print("fatiig")
                tapere = tapere + 1
            else:
                print("Ikke fattig")
                region.append(rad[1])
                inntekter.append(rad[12])
    except:
        print("\n!Linje parset ikke!\n")
        
        
plt.title("Inntekter 2017 for skogfjerter")
plt.barh(region,inntekter)