from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from models import db, User
from flask import Flask, request
from pprint import pprint
from flask.ext.httpauth import HTTPBasicAuth
import hashlib
import redis
import json

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
 
db = SQLAlchemy(app)

#http://techarena51.com/index.php/flask-sqlalchemy-tutorial/
#http://code.tutsplus.com/tutorials/intro-to-flask-signing-in-and-out--net-29982

# connect to redis cache server
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/insertdb', methods=['POST'])
def insertdb():
    pprint (request.get_json())

    email = getHash(request.get_json()['email'])
    fn = getHash(request.get_json()['firstname'])
    ln = getHash(request.get_json()['lastname'])
    sex = getHash(request.get_json()['sex'])
    age = getHash(request.get_json()['age'])
    u = User( firstname=fn, lastname=ln, email=email, sex = sex, age = age,
              ssn = request.get_json()['ssn'], phone = request.get_json()['phone'], url = request.get_json()['url'], password =request.get_json()['password'],
              passwordStrngth = request.get_json()['passwordStrngth'], dob = request.get_json()['dob'], dobWithTime = request.get_json()['dobWithTime'],
              creditcardnumber = request.get_json()['creditcardnumber'])
    # Insert user data to database
    db.session.add(u)
    db.session.commit()
    # get the generated id for the user recoed
    userId = str(u.id)
    pprint('User saved with userID ' + userId)
    retrievedUser = User.query.filter_by(id=userId).first()
    # convert user record retrieved from database to json format
    userJson = json.dumps(retrievedUser.as_dict())
    # store this json object as value with generted id as key in redis cache
    redis.set(userId, userJson)
    pprint('User cached in redis with key ' + userId)
    pprint('Value = ' + userJson)
    return 'row inserted!!!'

def getHash(input):
    return hashlib.md5(input).hexdigest()


@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'


@app.route('/')
def index():
    return render_template('Registration.html')
    
if __name__ == "__main__":
    app.run(debug=True)


