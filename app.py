import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# inicializamos la database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        
        # guardamos el nombre,mes y dia
        message = ""
        nombre = request.form.get("name")
        mes = request.form.get("month")
        dia = request.form.get("day")

        # Comprueba si se proporciona el nombre, el mes y el día
        if not nombre:
            message = "Falta el nombre"
        elif not mes:
            message = "Falta el mes"
        elif not dia:
            message = "Falta un dia"
        else:
            # Inserta el nombre, mes y día en la base de datos
            db.execute(
                "INSERT INTO birthdays (name, month, day) VALUES(?, ?,?)",
                nombre,
                mes,
                dia,
            )
        
        # Obtiene todas las filas de la tabla birthdays
        birthdays = db.execute("SELECT * FROM birthdays")

        # Renderiza la plantilla "index.html" y pasa la variable message y birthdays a la plantilla
        return render_template("index.html", message=message, birthdays=birthdays)
    else:
        # Si no se realizó una solicitud POST, obtiene todas las filas de la tabla birthdays
        birthdays = db.execute("SELECT * FROM birthdays")

        # pY pasa la variable birthdays a la plantilla
        return render_template("index.html", birthdays=birthdays)
