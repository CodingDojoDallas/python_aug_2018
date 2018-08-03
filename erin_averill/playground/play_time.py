from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('play_time.html')

@app.route('/play/<number>/<color>')
def play(number, color):
	print(number)
	print(color)
	return render_template('play_time.html',num=int(number), shade=color)


if __name__=="__main__":
	app.run(debug=True)