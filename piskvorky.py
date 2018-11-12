from random import randint

import ai


def tah_hrace(pole):

    while True:
        cislo_policka=int(input("Zadej pole kam chces hrat: " ))
        symbol='o'
        if '-' in pole[cislo_policka-1]:
            pole=pole[:cislo_policka-1] + symbol + pole[cislo_policka:]
            return(pole)
        else:
            print("Zadej jinou pozici. Tato je obsazena.")



def vyhodnot(pole):
    if 'xxx' in pole:
        print('Vyhral hrac s krizky.')
        return 'xxx'
        #break
    elif 'ooo' in pole:
        print('Vyhral hrac s kolecky.')
        return 'ooo'
        #break
    elif '-' not in pole:
        print('Remiza!')
        return '-'
        #break
    else:
        print('Hra jeste neskoncila!')
        return '!'


def hra(pole):
    aktualni_stav='!'
    while aktualni_stav=='!':
        pole=ai.tah_pc(pole)
        print(pole)
        aktualni_stav=vyhodnot(pole)
        if  aktualni_stav!='!':
            print(aktualni_stav)
            return aktualni_stav
        pole=tah_hrace(pole)
        print(pole)
        aktualni_stav=vyhodnot(pole)
