#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:18:21 2023

@author: saroa002

Eksamen-eksempel
"""

import csv
import math
import numpy as np
import matplotlib.pyplot as plt

    
# Åpner CSV-filen og leser inn dataene i en liste
with open('./Eksempeleksamen22.csv', 'r', encoding="ISO-8859-1") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Lager en dictionary for å telle antall turer fra hver startlokasjon (chat-gpt)
start_locs = dict()
for row in data:
    if row['start_station_name'] in start_locs:
        start_locs[row['start_station_name']] += 1
    else:
        start_locs[row['start_station_name']] = 1

# Sorterer startlokasjonene basert på antall turer og viser de tre mest brukte og minst brukte (chat-gpt)
most_used = sorted(start_locs.items(), key=lambda x: x[1], reverse=True)[:3]
least_used = sorted(start_locs.items(), key=lambda x: x[1])[:3]

print('\nDe tre mest brukte startlokasjonene er:\n')
for loc, count in most_used:
    print(loc, '- Antall turer:', count)

print('\nDe tre minst brukte startlokasjonene er:')
for loc, count in sorted(least_used, reverse=True):
    print(loc, '- Antall turer:', count)
    
stasjoner = list()
turer = list()
for b, c in sorted(start_locs.items(), key=lambda x: x[1], reverse=True):
    stasjoner.append(b)
    turer.append(c)
    
plt.barh(stasjoner, turer)
plt.xticks(rotation=90)
plt.xlabel('Startlokasjon')
plt.ylabel('Antall turer')
plt.title('Antall turer fra hver startlokasjon')

plt.show()