from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(200), nullable = False)
    position = db.Column(db.String(100), nullable = False)
    hire_date = db.Column(db.Date, nullable = False)
    salary = db.Column(db.Float, nullable = False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable = True)