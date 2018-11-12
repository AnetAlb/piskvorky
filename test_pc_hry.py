import ai, pytest

def test_hraje_pc():
    vysledek = ai.tah_pc('-------xoo--xx--oo-')
    assert vysledek != '-------xoo--xx--oo-'

def test_prilis_kratke_zadane_pole():
    with pytest.raises(IndexError):
        vysledek = ai.tah_pc('--')
        #assert vysledek != '-------xoo--xx--oo-'
