from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET"])
def render():
    return "<center><h1>Aplicacion Flask</h1></center>"
@app.route("/formulario",methods=["GET","POST"])
def formulario():
    if request.method=="GET":
        return render_template("formulario.html",nombre="")
    if request.method=="POST":
        nombre = request.form["nombre"]
        return render_template("formulario.html",nombre = nombre)

app.run(host="0.0.0.0",debug = False,threaded = True,port=80)
    
