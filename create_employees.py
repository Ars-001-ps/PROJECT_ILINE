from app import app, db
from models import Employee
from mimesis import Person
from mimesis.locales import Locale
import random
import datetime

person = Person(Locale.RU)

salary_ranges = {
    'CEO': (500000, 800000),
    'Manager': (200000, 400000),
    'Team Lead': (120000, 200000),
    'Senior Developer': (80000, 180000),
    'Developer': (35000, 80000),
}


# ~ ГЕНЕРИРУЕМ ЗАРПЛАТУ ПО ДОЛЖНОСТИ:
def get_salary(position):
    min_salary, max_salary = salary_ranges[position]
    return round(random.randint(min_salary, max_salary), -2)


# ~ СОЗДАЕМ ОБЬЕКТ СОТРУДНИКА С ЗАРПЛАТОЙ ПОД ЕГО ДОЛЖНОСТЬ:
def hire_employee(full_name, position, manager_id=None):
    salary = get_salary(position)
    employee = Employee(
        full_name=full_name,
        position=position,
        hire_date=datetime.date(2024, 1, 1),
        salary=salary,
        manager_id=manager_id,
    )
    return employee


def create_employees():
    print('генерация запущена')
    with app.app_context():
        print('создается СЕО')
        db.create_all()
        ceo_ids = []
        for _ in range(300):
            emp = hire_employee(person.full_name(), 'CEO')
            db.session.add(emp)
            db.session.commit()
            ceo_ids.append(emp.id)
        print('СЕО СОЗДАНЫ иду дальше...')

        manager_ids = []
        for _ in range(3000):
            emp = hire_employee(person.full_name(), 'Manager', random.choice(ceo_ids))
            db.session.add(emp)
            db.session.commit()
            manager_ids.append(emp.id)

        lead_ids = []
        for _ in range(8000):
            emp = hire_employee(
                person.full_name(), 'Team Lead', random.choice(manager_ids)
            )
            db.session.add(emp)
            db.session.commit()
            lead_ids.append(emp.id)

        senior_ids = []
        for _ in range(14200):
            emp = hire_employee(person.full_name(), 'Senior Developer', random.choice(lead_ids))
            db.session.add(emp)
            db.session.commit()
            senior_ids.append(emp.id)

        for _ in range(24500):
            emp = hire_employee(person.full_name(), 'Developer', random.choice(senior_ids))
            db.session.add(emp)
            db.session.commit()

        print('Готово! 50 000 сотрудников были созданы.')


create_employees()
