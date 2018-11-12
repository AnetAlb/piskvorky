import pytest
import piskvorky




def test_umi_poznat_vyhru():
    vysledek = piskvorky.hra('-------xxxo--xx--oo-')
    assert vysledek =='xxx'


def test_druhe_vyhry():
    vysledek = piskvorky.hra('-------xooo--xx--oo-')
    assert vysledek == 'ooo'


def test_kratsiho_vstupu():
    vysledek = piskvorky.hra('-------xooo-')
    assert vysledek == 'ooo'


def test_hraje_pc():
    vysledek = piskvorky.tah_pc('-------xoo--xx--oo-')
    assert vysledek != '-------xoo--xx--oo-'



#python -m pytest -v test_piskvorky.py
