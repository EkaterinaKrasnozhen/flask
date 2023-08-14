# Задание №1
# 📌 Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!"


import logging
from pathlib import PurePath, Path
from flask import Flask, redirect, render_template, request, flash, url_for, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
logger = logging.getLogger(__name__)


@app.route('/')
def start():
    return render_template('press.html')


@app.route('/hello')
def hello1():
    return f'Привет'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'Seminar2\\static\\uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


users = {'admin': '1234',
         'user1': '0000'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('login')
        passw = request.form.get('passw')
        if not request.form['login']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('login'))
        if (user_name, passw) in users.items():
            flash('Форма успешно отправлена!', 'success')
            return redirect(url_for('login'))
        return f' Неверный логин/пароль'
    return render_template('login.html')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        text = request.form.get('text')
        res = len(text.split())
        if not request.form['text']:
            flash('Введите текст!', 'danger')
            return redirect(url_for('enter'))
        flash('Форма успешно отправлена!', 'success')
        return f'Количество слов в тексте {res}'
    return render_template('enter.html')


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        operation = request.form.get('operation')
       
        match operation:
            case 'add':
                res = num1 + num2
            case 'substract':
                res = num1 - num2
            case 'multiply':
                res = num1 * num2
            case 'divide':
                res = num1 / num2
        return f'{res}'
    
    return render_template('calc.html')


@app.route('/user', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        #user_name = request.form.get('user_name')
        age = request.form.get('age')
        if int(age) < 18:
            abort(404)
        flash('Форма успешно отправлена!', 'success')
    return render_template('user_data.html')


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    return render_template('404.html'), 404           


@app.route('/number', methods=['GET', 'POST'])
def number():
    if request.method == 'POST':
        number = request.form.get('number')
        res = int(number) * int(number) 
        return redirect(url_for('result', result=res))
    return render_template('number.html')


@app.route('/result')
def result():
    return request.args.get('result')   


@app.route('/hello_name', methods=['GET', 'POST'])
def hello_name():
    if request.method == 'POST':
        user_name = request.form.get('name')
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('hello_name'))
        flash(f'Привет, {user_name}!', 'success')
    return render_template('hello_name.html')


if __name__ == '__main__':
    app.run(debug=True)