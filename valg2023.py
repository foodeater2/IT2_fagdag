#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:20:18 2023

@author: saroa002

Oppgaver til datasettet Valg2023 i mappen Data valg2023. Data er hentet herfra .https://www.valgresultat.no/valg/2023/ko
* Finn topp fem partier med høyest prosentandel oppslutning i sin kommune og de fem med lavest prosentandel oppslutning i sin kommune
* Finn topp 5 partier med høyest prosentvis økning i oppslutning i sin kommune i forrige tilsvarende valg og de fem med størst prosentvis tilbakegang
* Finn antall kommunestyrerepresentanter for Høyre, Venstre og AP i hvert fylke
* Finn hvilket parti som er valgvinneren i de fem kommunene med kortest navn (færrest antall bokstaver) og i de fem kommunene med lengst navn (flest antall bokstaver)

"""

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

rows = []
col = []


with open("./valg2023.csv", 'r', encoding="ISO-8859-1") as file:
  filinnhold = csv.reader(file, delimiter=";")
  overskrifter = next(filinnhold)
  print(overskrifter)
  
  for rad in filinnhold:
    try:
        rad[8].replace(',', '.')
        print("1 done", rad[8])
        b = float(rad[8])
        print("2 done")
        sted = rad[3]
        print("3 done")
    except:
        print("Err, rad not avalibale")
    print(rad[8])
    rows.append(rad)
    
