from sqlalchemy import func
from models import Employee, db
from flask import render_template, request, Flask # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)
all_employees = None


@app.route('/employees')
def employees():
    search_query = request.args.get('search', '')
    all_employees = Employee.query.all()
    
    if search_query:
        result = []
        for emp in all_employees:
            if search_query.lower() in emp.full_name.lower():
                result.append(emp)
        all_employees = result
        
    return render_template('employees.html', employees=all_employees)
        
    



with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)








    
     