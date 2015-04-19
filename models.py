from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100) )
    lastname = db.Column(db.String(100) )
    email = db.Column(db.String(100) )
    sex = db.Column(db.String(100) )
    age = db.Column(db.String(100) )
    ssn = db.Column(db.String(10) )
    phone = db.Column(db.String(20))
    url = db.Column(db.String(1000))
    password = db.Column(db.String(50))
    passwordStrngth = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    dobWithTime = db.Column(db.String(100))
    creditcardnumber = db.Column(db.String(100))

    def __init__(self, firstname=None, lastname=None, email = None, sex = None, age = None, ssn = None, phone = None, url = None, password = None, passwordStrngth = None, dob = None, dobWithTime = None, creditcardnumber = None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.sex = sex
        self.age = age
        self.ssn = ssn
        self.phone = phone
        self.url = url
        self.password = password
        self.passwordStrngth = passwordStrngth
        self.dob = dob
        self.dobWithTime = dobWithTime
        self.creditcardnumber = creditcardnumber

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}        

    # def __repr__(self):
    #     return '<User %r>' % (self.nickname)
