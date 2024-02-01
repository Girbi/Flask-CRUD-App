from flask import Blueprint, redirect, render_template, request, url_for

from utils.init import mysql

employees_bp = Blueprint("employees", __name__, template_folder="templates")


@employees_bp.route("/", methods=["POST", "GET"])
def employees():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM angajat ORDER BY id_angajat DESC")
        employees = cur.fetchall()
        return render_template(
            "employees.html",
            employees=employees,
        )
    else:
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        email = request.form["email"]
        departament = request.form["departament"]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO angajat (nume, prenume, email, departament) VALUES (%s, %s, %s, %s)",
            (nume, prenume, email, departament),
        )
        mysql.connection.commit()
        return redirect(url_for("employees.employees"))


@employees_bp.route("/delete/<id_angajat>", methods=["POST", "GET"])
def delete_employee(id_angajat):
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM angajat WHERE id_angajat = %s", (id_angajat,))
        mysql.connection.commit()
        return redirect(url_for("employees.employees"))
    else:
        return render_template("delete.html", id=id_angajat, url="employees")


@employees_bp.route("/update/<id_angajat>", methods=["POST", "GET"])
def update_employee(id_angajat):
    if request.method == "POST":
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        email = request.form["email"]
        departament = request.form["departament"]
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE angajat SET nume = %s, prenume = %s, email = %s, departament = %s WHERE id_angajat = %s",
            (
                nume,
                prenume,
                email,
                departament,
                id_angajat,
            ),
        )
        mysql.connection.commit()
        return redirect(url_for("employees.employees"))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM angajat WHERE id_angajat = %s", (id_angajat,))
        employee = cur.fetchone()
        return render_template(
            "updateEmployee.html", employee=employee, url="employees"
        )
