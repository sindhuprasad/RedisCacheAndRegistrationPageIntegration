To run the app:

1. install python and Flask framework, http://flask.pocoo.org/docs/0.10/installation/ along with Mysql
2. install redis and run redis on default port(6379)
3. use user.sql to create table in Mysql DB
4. navigate to Registration app folder
5. to run the server, run 'python app.py'
6. navigate to http://localhost:5000/ to see the registration page
7. verify user details stored in redis client with commands 1) 'keys *'' 2) 'get {give your id}''