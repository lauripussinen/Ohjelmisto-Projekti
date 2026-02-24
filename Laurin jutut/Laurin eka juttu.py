import Tarina

storyDialog = input('Haluatko lukea pelin alkutarinan? (Kyllä/Ei): ')
if storyDialog == 'Kyllä':
    # print wrapped string line by line
    for line in Tarina.haetarina():
        print(line)