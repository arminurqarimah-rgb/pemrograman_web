from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template("/pages/beranda.html")

@app.route("/dokumen")
def dokumen():
    return render_template("/pages/dokumen.html")

@app.route("/keahlian")
def keahlian():
    return render_template("/pages/keahlian.html")

@app.route("/kontak")
def kontak():
    return render_template("/pages/kontak.html")

@app.route("/pendidikan")
def pendidikan():
    return render_template("/pages/pendidikan.html")

@app.route("/pengalaman")
def pengalaman():
    return render_template("/pages/pengalaman.html")

@app.route("/tentang")
def tentang():
    return render_template("pages/tentang.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)