from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/qs")
def qs():
    return render_template("qs.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto", methods=["GET", "POST"])  
def contacto():
    if request.method == "POST":
        
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        
        return redirect(url_for('index'))  
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(port=5002) 