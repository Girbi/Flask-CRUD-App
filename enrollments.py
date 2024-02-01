from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from utils.init import mysql
from utils.options import get_select_options

enrollments_bp = Blueprint("enrollments", __name__, template_folder="templates")


@enrollments_bp.route("/", methods=["POST", "GET"])
def enrollments():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT id_inscriere, data_inscriere, angajat.nume, angajat.    prenume, curs.nume, stadiu FROM inscriere JOIN angajat USING    (id_angajat) JOIN curs USING(id_curs) ORDER BY id_inscriere     DESC"
        )
        enrollments = cur.fetchall()
        options = get_select_options(mysql)

        return render_template(
            "enrollments.html", enrollments=enrollments, options=options
        )
    else:
        employee_id = request.form["employees"]
        course_id = request.form["courses"]
        state = request.form["state"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO inscriere (id_angajat, id_curs, stadiu, data_inscriere) VALUES (%s, %s, %s, %s)",
            (employee_id, course_id, state, datetime.now()),
        )
        mysql.connection.commit()
        return redirect(url_for("enrollments.enrollments"))


@enrollments_bp.route("/delete/<id_inscriere>", methods=["POST", "GET"])
def delete_enrollment(id_inscriere):
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM inscriere WHERE id_inscriere = %s", (id_inscriere,))
        mysql.connection.commit()
        return redirect(url_for("enrollments.enrollments"))
    else:
        return render_template("delete.html", id=id_inscriere, url="enrollments")


@enrollments_bp.route("/update/<id_inscriere>", methods=["POST", "GET"])
def update_enrollment(id_inscriere):
    if request.method == "POST":
        employee = request.form["employees"]
        course = request.form["courses"]
        state = request.form["state"]

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE inscriere SET id_angajat = %s, id_curs = %s, stadiu = %s WHERE id_inscriere = %s",
            (employee, course, state, id_inscriere),
        )
        mysql.connection.commit()
        return redirect(url_for("enrollments.enrollments"))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM inscriere WHERE id_inscriere = %s", (id_inscriere,))
        enrollment = cur.fetchone()
        options = get_select_options()
        return render_template(
            "updateEnrollment.html",
            enrollment=enrollment,
            url="enrollments",
            options=options,
        )
