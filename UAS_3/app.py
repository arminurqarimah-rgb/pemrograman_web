from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from utils import daftar_parkir 

app = Flask(__name__)

riwayat_bayar = []

TARIF = {"MOBIL": 5000, "MOTOR": 2000}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pilihan = request.form.get('pilihan')
        mapping = {
            '1': 'halaman_masuk', 
            '2': 'halaman_keluar', 
            '3': 'halaman_lihat', 
            '4': 'halaman_analisis'
        }
        if pilihan in mapping:
            return redirect(url_for(mapping[pilihan]))
        elif pilihan == '5':
            return "Aplikasi Berhenti. Silakan tutup tab browser ini."
    return render_template('index.html')

@app.route('/masuk', methods=['GET', 'POST'])
def halaman_masuk():
    error_msg = ""
    if request.method == 'POST':
        plat = request.form.get('plat').strip().upper()
        jenis = request.form.get('jenis')
        merk = request.form.get('merk')
        
        if any(item['plat'] == plat for item in daftar_parkir):
            error_msg = f"GAGAL: Kendaraan {plat} sudah ada di dalam!"
        else:
            daftar_parkir.append({
                "plat": plat, 
                "jenis": jenis, 
                "merk": merk,
                "waktu_masuk": datetime.now()
            })
            return redirect(url_for('index'))
    return render_template('masuk.html', error=error_msg)

@app.route('/keluar', methods=['GET', 'POST'])
def halaman_keluar():
    if request.method == 'POST':
        plat = request.form.get('plat').strip().upper()
        for i, item in enumerate(daftar_parkir):
            if item['plat'] == plat:
                waktu_keluar = datetime.now()
                durasi = waktu_keluar - item['waktu_masuk']
                jam = max(1, round(durasi.total_seconds() / 3600))
                total = jam * TARIF.get(item['jenis'], 2000)
                
                riwayat_bayar.append({
                    "plat": plat,
                    "jenis": item['jenis'],
                    "merk": item['merk'], 
                    "waktu_masuk": item['waktu_masuk'],
                    "waktu_keluar": waktu_keluar,
                    "biaya": total
                })

                
                data_struk = {"plat": plat, "total": total, "jam": jam}
                daftar_parkir.pop(i)
                return render_template('struk.html', data=data_struk)
        return "Kendaraan tidak ditemukan! <a href='/' style='color:white;'>Kembali</a>"
    return render_template('keluar.html')

@app.route('/lihat')
def halaman_lihat():
    return render_template('lihat.html', parkir=daftar_parkir)

riwayat_parkir = [
    {"plat": "B 1234 ABC", "merk": "Toyota Avanza", "jenis": "MOBIL", "biaya": 10000},
    {"plat": "D 5678 EFG", "merk": "Honda Beat", "jenis": "MOTOR", "biaya": 4000},
    {"plat": "B 9999 XYZ", "merk": "Mitsubishi Pajero", "jenis": "MOBIL", "biaya": 5000},
    {"plat": "F 1122 GH", "merk": "Yamaha NMAX", "jenis": "MOTOR", "biaya": 2000},
    {"plat": "L 7777 SS", "merk": "Suzuki Carry", "jenis": "MOBIL", "biaya": 10000}
]

@app.route('/analisis')
def halaman_analisis():

    total_hari = sum(r['biaya'] for r in riwayat_bayar)
    count_hari = len(riwayat_bayar)

    stats = {
        'h_cnt': count_hari,
        'hari': total_hari,
        'm_cnt': count_hari, 
        'minggu': total_hari,
        'b_cnt': count_hari,
        'bulan': total_hari,
        'th_cnt': count_hari,
        'tahun': total_hari
    }

    # 2. Kirim data ke template. 
    # Pastikan nama variabelnya 'riwayat_data' sesuai dengan {% for r in riwayat_data %}
    return render_template('analisis.html', s=stats, riwayat_data=riwayat_bayar)

if __name__ == '__main__':
    app.run(debug=True)

