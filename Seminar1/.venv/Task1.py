# Задание №1
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

# Задание №2
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".

# Задание №3
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.

# Задание №4
# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

# Задание №5
# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
  
# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.



from flask import Flask, render_template

app = Flask(__name__)


html = """
    <h1>Привет, мир!</h1>
    """
    
students = [
    {'name': 'Екатерина', 'surname': 'Красножен', 'age': 37, 'score': 5},
    {'name': 'Павел', 'surname': 'Блинов', 'age': 38, 'score': 4.7},
    {'name': 'Ярослав', 'surname': 'Блинов', 'age': 8, 'score': 5},
    {'name': 'Святослав', 'surname': 'Блинов', 'age': 3, 'score': 5}
]

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def contact():
    return 'Contact'


@app.route('/<int:num1>/<int:num2>/')
def set_number(num1, num2):
    return f'сумма = {num1 + num2}'


@app.route('/<my_str>/')
def get_str_length(my_str):
    return f'длина строки = {len(my_str)}'


@app.route('/study/')
def study():
    return render_template('students.html', students = students)
    
    
@app.route('/text/')
def text():
    return html

#flask --app Task1.py run


if __name__ == '__main__':
    app.run(debug=True)