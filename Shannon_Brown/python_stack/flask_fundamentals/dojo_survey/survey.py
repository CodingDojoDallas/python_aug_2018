from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('survey.html')

@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('result.html', name = name, location = location, language = language, comments = comments)
    return redirect("/")



app.run(debug = True)