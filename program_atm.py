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
    while True:
            print("Selamat datang di ATM Kelompok 32..")
            print("\n1 - Cek Saldo\t2 - Debet\t3 - Simpan\t4 - Ganti Pin\t5 - Keluar")
            selectmenu = int(input("\nSilahkan pilih menu (1-5): "))
            if selectmenu == 1:
                print("\nSaldo anda sekarang: Rp. " + str(atm.cekBalance()) + "\n")
            elif selectmenu == 2:
                nominal = float(input("Masukkan nominal debet: "))
                verify_withdraw = input(
                    "Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y / n " + str(nominal) + " ")
                if verify_withdraw == "y":
                    print("Saldo awal anda adalah: Rp. " +
                          str(atm.cekBalance()) + "")
                    if nominal < atm.cekBalance():
                        atm.withdrawBalance(nominal)
                        print("Transaksi debet berhasil!")
                        print("Saldo sisa sekarang: Rp. " +
                              str(atm.cekBalance()) + "")
                    else:
                        print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                        print("Silakan lakukan penambahan nominal saldo")
                else:
                    break
            elif selectmenu == 3:
                nominal = float(input("Masukkan nominal penyimpanan: "))
                verify_deposit = input(
                    "Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? y / n :" + str(nominal) + " ")
                if verify_deposit == "y":
                    atm.depositBalance(nominal)
                    print("Saldo anda sekarang: Rp. " + str(atm.cekBalance()) + "")
                else:
                    break
            elif selectmenu == 4:
                verify_pin = int(input("Masukkan pin anda: "))
                trial = 0
                while verify_pin != int(atm.cekPin()) and trial < 3:
                    verify_pin = int(input("Pin anda salah, silakan masukkan pin: "))
                    trial += 1
                    if trial == 3:
                        print("Error. Silakan ambil kartu dan coba lagi..")
                        exit()
                updated_pin = int(input("Silahkan masukkan pin baru: "))
                print("Pin anda berhasil diganti!")
                verify_newpin = int(input("Coba masukkan pin baru: "))
                if verify_newpin == updated_pin:
                    print("Pin baru anda sukses!")
                    atm.custPin = updated_pin
                else:
                    print("Maaf, pin anda salah! ")
            elif selectmenu == 5:
                print("Resi tercetak otomatis saat anda keluar.\nHarap simpan tanda terima ini\nsebagai bukti transaksi "
                      "anda.")
                print("No. Record: ", random.randint(100000, 1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.cekBalance())
                print("Terima kasih telah menggunakan ATM Kelompok 32!")
                exit()
            else:
                print("Error. Maaf, menu tidak tersedia")