import sys
from utils import clear_screen, daftar_parkir

def jalankan_cli():
    while True:
        clear_screen()
        print("=== APLIKASI PARKIR ===")
        print("1. Kendaraan Masuk")
        print("2. Kendaraan Keluar")
        print("3. Lihat Parkir")
        print("4. Keluar")
        
        pilihan = input("\nPilihan : ")

        if pilihan == '1':
            plat_baru = input("Plat  : ").strip().upper()
            
            sudah_ada = False
            for item_parkir in daftar_parkir:
                if item_parkir['plat'] == plat_baru: 
                    sudah_ada = True
                    break
            
            if sudah_ada:
                print(f"\n[Gagal] Kendaraan {plat_baru} sudah ada di dalam!")
            else:
                jenis = input("Jenis : ")
                merk  = input("Merk  : ")
                
                data_masuk = {"plat": plat_baru, "jenis": jenis, "merk": merk}
                daftar_parkir.append(data_masuk)
                print(f"\n[Berhasil] {plat_baru} terdaftar.")

        elif pilihan == '2':
            if not daftar_parkir:
                print("Parkiran Kosong")
            else:
                cari_plat = input("Plat Kendaraan Keluar: ").strip().upper()
                
                ketemu = False
                for indeks in range(len(daftar_parkir)):
                    if daftar_parkir[indeks]["plat"] == cari_plat:
                        mobil_keluar = daftar_parkir.pop(indeks)
                        print(f"\nKeluar: {mobil_keluar['plat']} - {mobil_keluar['merk']}")
                        ketemu = True
                        break
                
                if not ketemu:
                    print("Kendaraan tidak ditemukan")

        elif pilihan == '3':
            if not daftar_parkir:
                print("Parkiran Kosong")
            else:
                print("\nDAFTAR KENDARAAN:")
                for no, info in enumerate(daftar_parkir, 1):
                    print(f"{no}. {info['plat']} ({info['merk']})")

        elif pilihan == '4':
            sys.exit()

        input("\nKlik Enter untuk melanjutkan...")