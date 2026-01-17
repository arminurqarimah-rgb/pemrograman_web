import sys
from utils import clear_screen, daftar_antrian

def jalankan_cli():
    while True:
        clear_screen()
        print("1. Tambah Antrian")
        print("2. Panggil Antrian")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilihan : ")

        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            daftar_antrian.append(nama)
            print(f"Nama '{nama}' berhasil disimpan.")

        elif pilihan == '2':
            if len(daftar_antrian) == 0:
                print("tidak ada antrian")
            else:
                dipanggil = daftar_antrian.pop(0)
                print(f"Memanggil {dipanggil}")

        elif pilihan == '3':
            if len(daftar_antrian) == 0:
                print("tidak ada antrian")
            else:
                print("Daftar Antrian:")
                for i, nama in enumerate(daftar_antrian, 1):
                    print(f"{i}. {nama}")

        elif pilihan == '4':
            sys.exit()

        input("\nKlik Enter untuk melanjutkan...")