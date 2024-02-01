def get_select_options(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT nume, id_curs FROM curs")
    courses = cur.fetchall()
    course_options = [
        {"label": course["nume"], "id": course["id_curs"]} for course in courses
    ]

    cur.execute("SELECT nume, prenume, id_angajat FROM angajat")
    employees = cur.fetchall()
    employee_options = [
        {
            "label": f"{employee['nume']} {employee['prenume']}",
            "id": employee["id_angajat"],
        }
        for employee in employees
    ]

    state_options = ["NEINCEPUT", "IN LUCRU", "TERMINAT"]
    options = {
        "course_options": course_options,
        "employee_options": employee_options,
        "state_options": state_options,
    }
    return options
