from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('checkers.html')


@app.route('/size/<length>/<width>')
def color(length, width):
	print(length)
	print(width)
	return render_template('checkers.html', length=int(int(length)/2), width=int(int(width)/2))

if __name__ == '__main__':
	app.run(debug=True)
	