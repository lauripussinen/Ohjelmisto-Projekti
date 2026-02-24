import random
import tarina


alkutarina = input('Haluatko lukea pelin alkutarinan? (Kyllä/Ei): ')
if alkutarina == 'Kyllä':
    # print wrapped string line by line
    for line in tarina.haetarina():
        print(line)