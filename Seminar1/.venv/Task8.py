# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

# head
# подключаем стили
#<link rel="stylesheet" href="/static/css/bootstrap.min.css">
# делаем название странички
#<title>Мой сайт</title>

#body
# текст на страничке
# <h1> - заголовок </h1> жирный
# <p> Параграф </p> Lorem20 + TAB случайный текст из 20
# <ul> список марикированный
#     <li> *Элемент </li>
#     <li> *Элемент </li>  
# </ul>
# 
# <ol> список нумерованный
#     <li> 1.Элемент </li>
#     <li> 2.Элемент </li>  
# </ol>
#
#<div> блоки
#</div>

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')
    
    
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)