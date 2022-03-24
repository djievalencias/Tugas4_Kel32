import random
import datetime
from nasabah import nasabah

atm = nasabah(id)

while True:
    # Default PIN: 1212
    # Default balance: 100000
    id = int(input("Masukkan pin anda: "))
    trial = 0
    while id != int(atm.cekPin()) and trial < 3:
        id = int(input("Pin anda salah. Silakan masukkan lagi: "))
        trial += 1
        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
