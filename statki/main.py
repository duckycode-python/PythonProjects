from msilib.schema import Error
import random
import os
from tracemalloc import start

pola = [['A1'], ['A2'], ['A3'], ['A4'], ['A5'], ['A6'], ['A7'], ['A8'], ['A9'], ['A10'], ['B1'], ['B2'], ['B3'], ['B4'], ['B5'], ['B6'], ['B7'], ['B8'], ['B9'], ['B10'], ['C1'], ['C2'], ['C3'], ['C4'], ['C5'], ['C6'], ['C7'], ['C8'], ['C9'], ['C10'], ['D1'], ['D2'], ['D3'], ['D4'], ['D5'], ['D6'], ['D7'], ['D8'], ['D9'], ['D10'], ['E1'], ['E2'], ['E3'], ['E4'], ['E5'], ['E6'], ['E7'], ['E8'], ['E9'], ['E10'], ['F1'], ['F2'], ['F3'], ['F4'], ['F5'], ['F6'], ['F7'], ['F8'], ['F9'], ['F10'], ['G1'], ['G2'], ['G3'], ['G4'], ['G5'], ['G6'], ['G7'], ['G8'], ['G9'], ['G10'], ['H1'], ['H2'], ['H3'], ['H4'], ['H5'], ['H6'], ['H7'], ['H8'], ['H9'], ['H10'], ['I1'], ['I2'], ['I3'], ['I4'], ['I5'], ['I6'], ['I7'], ['I8'], ['I9'], ['I10'], ['J1'], ['J2'], ['J3'], ['J4'], ['J5'], ['J6'], ['J7'], ['J8'], ['J9'], ['J10']]
for x in pola:
    x.append(False)
def drukujPola():
    nextRow = 2
    row = ""
    for x in pola:
        if nextRow <=10:
            row += f"{x[0]}  "
            nextRow += 1
        else:
            row += f"{x[0]}  \n"
            print(row)
            row = ""
            nextRow = 2

def losowaniePolozeniaStatkow():
    for x in range(24):
        statek = random.choice(pola)
        polozenie = pola.index(statek)
        if pola[polozenie][1] == False:
            pola[polozenie].remove(False)
            pola[polozenie].append(True)
        print(statek)

losowaniePolozeniaStatkow()
def startGry():
    os.system("cls")
    drukujPola()
    strzal = input("W jakie pole chcesz strzelic? ")
    for x in pola:
        if x[0] == strzal:
            czyPole = True
            if x[1] == True:
                print("Trafiony zatopiony!")
                x.remove(True)
                x.insert(1, False)
                x.remove(strzal)
                x.insert(0, "XX")
                x.insert(2, True)
                input()
                startGry()
            else:
                x.insert(0, "##")
                print("Pudło!")
                input()
                czyPole = True
                x.insert(2, True)
                startGry()
        else:
            czyPole = False
    if czyPole:
            startGry()
    else:
        if czyStrzelano(strzal):
            print("Te miejsce zostało już odstrzelone!")
            input()
            startGry()
        else:
            print("Wybierz poprawne pole!")
            input()
            startGry()
def czyStrzelano(pole):
    polozenie = 0
    for x in pola:
        czyPole = False
        if x[0] == pola[polozenie][0]:
            czyPole = True
        polozenie += 1
    if czyPole:
        if pole[2]:
            return True
        else:
            return False
    else:
        raise Error
startGry()