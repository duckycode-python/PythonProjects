
from unicodedata import name
import cv2
from os import listdir
from os.path import isfile, join
import os
import random
import string

kopialubnie = []
usuniete = 0
path = input("Podaj sciezke do folderu ze zdjeciami:")
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
def usuwanie():
    global path
    global usuniete
    global kopialubnie
    global onlyfiles
    global usuniete1
    usuniete1 = 0
       
    for plik in onlyfiles:
        prawdziwePath = f"{path}\{plik}"
        file_name = os.path.join(os.path.dirname(__file__), prawdziwePath)
        assert os.path.exists(file_name)
        prawdziwe = cv2.imread(file_name)
        for plik in onlyfiles:
            kopiaPath = f"{path}\{plik}"
            file_name1 = os.path.join(os.path.dirname(__file__), kopiaPath)
            try:    
                assert os.path.exists(file_name1)
            except AssertionError:
                pass
            kopia = cv2.imread(file_name1)
            try:
                if prawdziwe.size == kopia.size:
                    if kopiaPath == prawdziwePath:
                        continue
                    else:
                        os.remove(kopiaPath)
                        usuniete = usuniete + 1
                        usuniete1 += 1
                else:
                    continue
            except (AttributeError, OSError, AssertionError):
                pass
        if usuniete1 == 0:
            pass
        else:
            usuwanie()

usuwanie()
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
for plik in onlyfiles:
    path = f"{path}\{plik}"
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    zmienionePath = f"{path}\{file_name}.png"
    os.rename(path, zmienionePath)
print(f"Usunięto {usuniete} kopii.")
input()