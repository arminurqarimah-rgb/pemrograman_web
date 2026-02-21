from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <div style="font-family: Arial; padding: 20px;">
        <h1>Daftar Tugas Qarimah</h1>
        <hr>
        <ul>
            <li><a href="/no1" style="font-size: 1.2rem;">Lihat Tugas No 1</a></li>
            <li><a href="/no2" style="font-size: 1.2rem;">Lihat Tugas No 2</a></li>
            <li><a href="/no3" style="font-size: 1.2rem;">Lihat Tugas No 3</a></li>
            <li><a href="/no4" style="font-size: 1.2rem;">Lihat Tugas No 4</a></li>
        </ul>
    </div>
    """

@app.route('/no1')
def no_1():
    return render_template('no_1.html')

@app.route('/no2')
def no_2():
    return render_template('no_2.html', jumlah_kotak=3)

@app.route('/no3')
def no_3():
    return render_template('no_3.html')

@app.route('/no4')
def no_4():
    return render_template('no_4.html')

if __name__ == '__main__':
    app.run(debug=True)