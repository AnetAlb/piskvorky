from random import randint

symbol = 'x'

def tah_pc(pole, symbol):
    delka_pole = len(pole)
    while True:
        cislo_policka=randint(1,delka_pole)

        if '-' in pole[cislo_policka-1]:
            pole=pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
            return(pole)
        else:
            print("PC spatne vybral. Vybira znovu")
