from flask import Blueprint, redirect, render_template, request, url_for

from utils.init import mysql

courses_bp = Blueprint("courses", __name__, template_folder="templates")


@courses_bp.route("/", methods=["POST", "GET"])
def courses():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM curs ORDER BY id_curs DESC")
        courses = cur.fetchall()
        return render_template(
            "courses.html",
            courses=courses,
        )
    else:
        nume = request.form["nume"]
        durata = request.form["durata"]
        pret = request.form["pret"]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO curs (nume, durata, pret) VALUES (%s, %s, %s)",
            (nume, durata, pret),
        )
        mysql.connection.commit()
        return redirect(url_for("courses.courses"))


@courses_bp.route("/delete/<id_curs>", methods=["POST", "GET"])
def delete_course(id_curs):
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM curs WHERE id_curs = %s", (id_curs,))
        mysql.connection.commit()
        return redirect(url_for("courses.courses"))
    else:
        return render_template("delete.html", id=id_curs, url="courses")


@courses_bp.route("/update/<id_curs>", methods=["POST", "GET"])
def update_course(id_curs):
    if request.method == "POST":
        nume = request.form["nume"]
        durata = request.form["durata"]
        pret = request.form["pret"]
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE curs SET nume = %s, durata = %s, pret = %s WHERE id_curs = %s",
            (nume, durata, pret, id_curs),
        )
        mysql.connection.commit()
        return redirect(url_for("courses.courses"))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM curs WHERE id_curs = %s", (id_curs,))
        course = cur.fetchone()
        return render_template("updateCourse.html", course=course, url="courses")
