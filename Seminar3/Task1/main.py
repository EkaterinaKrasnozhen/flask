from flask import Flask, render_template
from Task1.models import db, Student, Faculty
from random import randint
# import black, black.main автоформатор

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')


@app.cli.command("create_base")
def create_base():
    for i in range(1, 6):
        faculty = Faculty(name=f'Faculty_{i}')
        db.session.add(faculty)
    for i in range(1, 11):
        student = Student(
            name = 'Kate', surname = f'Kras_{i}', age=22, 
            group = f'{i}', sex = True, faculty_id=randint(1, 5))
        db.session.add(student)
    db.session.commit()
    print('Student ok!')
    
    
@app.route('/students/')
def all_users():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)
    #return render_template('students.html', students=students)
    
    
# flask run
# flask init-db


if __name__ == "__main__":
    app.run(debug=True)