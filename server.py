from flask import Flask, redirect, render_template, request, session, flash
import datetime
from datetime import datetime
app = Flask(__name__)
app.secret_key = '12AB3FEE4589'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results')
def results():
	return render_template('results.html', name=session['name'])

@app.route('/submission', methods=['POST'])
def submission():
	fields = {'first':'First Name', 'last':'Last Name', 'dob':'Date of Birth', 'password':'Password', 'confirm':'Confirm Passowrd', 'email':'Email'}
	valid = True
	for item in request.form:
		if len(request.form[item]) == 0:
			flash(fields[item] + " field must not be empty.")
			valid = False
	if request.form['password'] != request.form['confirm']:
		flash("Passwords do not match.")
		valid = False
	if not any(char.isupper() for char in request.form['password']):
		flash("Password must contain at least one upper case letter.")
		valid = False
	if not any(char.islower() for char in request.form['password']):
		flash("Password must contain at least one lower case letter.")
		valid = False
	if not any(char.isdigit() for char in request.form['password']):
		flash("Password must contain at least one number.")
		valid = False
	dob = request.form['dob'].split('-')
	dob = datetime(int(dob[0]),int(dob[1]),int(dob[2]))
	if not dob < datetime.now():
		flash("You cannot be born in the future, check your date of birth.")
		valid = False
	if not valid:
		return redirect('/')
	session['name'] = request.form['first']
	return redirect('/results')
app.run(debug=True)
