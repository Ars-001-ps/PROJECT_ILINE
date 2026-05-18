from app import app, db
from models import Employee
from mimesis import Person
from mimesis.locales import Locale
import random

person = Person(Locale.RU)

salary_ranges = {
    'CEO': (500000, 800000),
    'Manager': (200000, 400000),
    'Team Lead': (120000, 200000),
    'Senior Developer': ( 80000, 180000),
    'Developer': (35000, 80000)
}

# ~ ГЕНЕРИРУЕМ ЗАРПЛАТУ ПО ДОЛЖНОСТИ:
def get_salary(position):
    min_salary, max_salary = salary_ranges[position]
    return round(random.randint(min_salary, max_salary), -2)

# ~ СОЗДАЕМ ОБЬЕКТ СОТРУДНИКА С ЗАРПЛАТОЙ ПОД ЕГО ДОЛЖНОСТЬ:
def hire_employee(full_name, position, manager_id = None):
    salary = get_salary(position)
    employee = Employee(
        full_name = full_name,
        position = position,
        hire_date = '2024-01-01',
        salary = salary,
        manager_id = manager_id
    )
    return employee
