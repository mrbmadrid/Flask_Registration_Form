from flask import Flask, redirect, render_template, request, session, flash
app = Flask(__name__)
app.secret_key = '12AB3FEE4589'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/submission', methods=['POST'])
def submission():
	if len(request.form['name']) == 0:
		flash("Name field must not be empty.")
		return redirect('/')
	session['name']=request.form['name']
	session['location']=request.form['location']
	session['favorite']=request.form['favorite_language']
	if len(request.form['comment']) == 0:
		flash("Comment field must not be empty.")
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash("Comment must be no more than 120 characters.")
		return redirect('/')
	session['comment']=request.form['comment']
	return redirect('/results')
app.run(debug=True)
