from flask import Flask, render_template, flash,url_for,redirect,request,session
from flask_login import login_user , current_user, logout_user

#import sounddevice as sd 
#from playsound import playsound
from forms import RegistrationForm,LoginForm
#from scipy.io.wavfile import write 
#import wavio as wv 
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import MySQLdb.cursors 
import json

import os
from predict import predict

app = Flask(__name__)


app.config['SECRET_KEY'] = '4d5482dc5b0411eb983b3024a9431551'

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:@localhost/audio-recognition'.format(user='root', password='', server='localhost', database='audio-recognition')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'audio-recognition'
mysql = MySQL(app) 
db = SQLAlchemy(app)


class Signup(db.Model):
	username = db.Column(db.String(80),	unique=False,	nullable=False)
	email = db.Column(db.String(80),	unique=True,	primary_key=True,	nullable=False)
	password = db.Column(db.String(120),	nullable=False)


	
@app.route("/index", methods=['GET', 'POST'])
def home():
    return render_template('index.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method=='POST' and form.validate_on_submit():
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		secure_password = sha256_crypt.encrypt(str(password))
		entry = Signup(username=username,email = email,password = password)
		db.session.add(entry)
		db.session.commit()
		flash(f'Account created for {form.email.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method=='POST' and form.validate_on_submit():
		email=request.form.get('email')
		password = request.form.get('password')
		secure_password = sha256_crypt.encrypt(str(password))
		secure_pass = sha256_crypt.verify(password,secure_password)
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
		cursor.execute('SELECT * FROM signup WHERE email = % s AND password = % s', (email, password, ))  
		Signup = cursor.fetchone()  
		if Signup: 
			session['loggedin']=True
			session['id']=Signup['id'] 
			session['email']=Signup['email'] 
			flash('You have been logged in!', 'success')
			return redirect(url_for('analysis')) 
		else: 
			flash('Login Unsuccessful. Please check Email and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/index1")
def index1():
    return render_template('index1.html')


    
@app.route("/analysis")
def analysis():  
    return render_template('analysis.html')

@app.route("/analysis",methods=['GET', 'POST'])
def upload():
	if request.method=='POST':
		file=request.files["file"]
		file.save(os.path.join("uploads",file.filename))
		type_sound=predict(os.path.join("uploads",file.filename))
		print(type_sound)
		#return "Result:"+type_sound
		return render_template('analysis.html', prediction_text='Sound  is:-{}'.format(type_sound))
	return render_template('analysis.html')

	


			
			
	

app.run(debug=True)
