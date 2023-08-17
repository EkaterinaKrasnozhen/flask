from flask import Flask, render_template, request
from Task4.models import db, User
from flask_wtf.csrf import CSRFProtect

from Task4.forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')
    
    
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        password = form.password.data
        exist_user = User.query.filter((User.username == username) | (User.email == email)).first()
        user = User(username=username, email = email, password=password)
        if exist_user:
            error_msg = 'User allready exist.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)
        db.session.add(user)
        db.session.commit()
        return 'Succes!'
    return render_template('register.html', form=form)
    
    
if __name__ == "__main__":
    app.run(debug=True)