from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route('/toyform')
def page():
	return render_template('toyinfopage.html')

@app.route('/process', methods=['POST'])
def process():
	toyname=request.form['toyname']
	age=request.form['agegroup']
	session['a'] = age
	# session.pop('a')
	print (toyname)
	print (agegroup)
	return redirect('/display')

@app.route('/display')
	def display():
		return "Sucess" + session['a']

if __name__ == '__main__':
	app.run(debug=True)