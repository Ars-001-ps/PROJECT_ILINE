from sqlalchemy import func
from models import Employee, db
from flask import render_template, request, Flask, redirect  # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)
all_employees = None


@app.route('/employees')
def employees():
    sort_field = request.args.get('sort', 'id')
    sort_order = request.args.get('order', 'asc')
    search_query = request.args.get('search', '')
    all_employees = Employee.query.all()

    if search_query:
        result = []
        for emp in all_employees:
            if search_query.lower() in emp.full_name.lower():
                result.append(emp)
        all_employees = result

    if sort_order == 'asc':
        all_employees = sorted(
            all_employees,
            key=lambda e: (getattr(e, sort_field) is None, getattr(e, sort_field)),
        )
    else:
        all_employees = sorted(
            all_employees,
            key=lambda e: (getattr(e, sort_field) is None, getattr(e, sort_field)),
            reverse=True,
        )
    return render_template(
        'employees.html',
        employees=all_employees,
        current_order=sort_order,
        current_sort=sort_field,
    )


@app.route('/update_manager', methods=['POST'])
def update_manager():
    emp_id = request.form.get('emp_id')
    new_manager_id = request.form.get('new_manager_id')
    if not emp_id or not new_manager_id:
        return 'Ошиька: не указан id сотрудника или id нового начальника'
    
    employee = db.session.get(Employee, emp_id)
    new_manager = db.session.get(Employee, new_manager_id)
    if not new_manager:
        return f'Ошибка: сотрудник с id {new_manager_id} не найден.'
    if employee and new_manager:
        if emp_id == new_manager_id:
            return 'Ошибка: нельзя назначить сотрудника начальником самому себе.'
        employee.manager_id = new_manager_id
        db.session.commit()

    return redirect('/employees')


with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
