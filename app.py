from flask import Flask  # type: ignore
from models import Employee, db
from flask import render_template  # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)
all_employees = None


@app.route('/employees')
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', employees=all_employees) 



with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
