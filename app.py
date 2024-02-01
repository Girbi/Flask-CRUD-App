from flask import redirect, url_for

from courses import courses_bp
from employees import employees_bp
from enrollments import enrollments_bp
from utils.init import app

app.register_blueprint(employees_bp, url_prefix="/employees")
app.register_blueprint(courses_bp, url_prefix="/courses")
app.register_blueprint(enrollments_bp, url_prefix="/enrollments")


@app.route("/")
def index():
    # Redirect to employees page
    return redirect(url_for("employees.employees"))


if __name__ == "__main__":
    app.run(debug=True)
