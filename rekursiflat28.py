#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:00:54 2022

@author: rhenatabella
"""

def latihan2():
    print()
    print("Ini merupakan program pemangkatan negatif dan positif, Tekan enter untuk berhenti")
    angka = input("Masukkan Angka: ")
    if angka == '':
        print("Terima Kasih telah menggunakan Program ini. Program selesai")
        return 0
    pangkat = input("Masukkan Pangkatnya: ")
    eksekusi = int(angka)**int(pangkat)
    print("Hasilnya adalah: ",eksekusi)
    latihan2()

latihan2()
