import piskvorky


def test_vyhodnocuje_remizu():
    vysledek = piskvorky.vyhodnot('xo')
    assert vysledek == '-'

def test_vyhodnocuje_pokracovani_hry():
    vysledek = piskvorky.vyhodnot('-xxo')
    assert vysledek == '!'

def test_prazdny_retezec():
    vysledek = piskvorky.vyhodnot('')
    assert vysledek == '-'
    #assert vysledek == '!'
