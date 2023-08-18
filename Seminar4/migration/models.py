

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)# автонумерация с 1
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    group = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    
    def __repr__(self):
        return f'Student({self.name}, {self.surname})'
    

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)
    
    def __repr__(self):
        return f'Faculty({self.id}, {self.name})'