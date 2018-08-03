from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('playground2.html', num=int(3))


@app.route('/play/<number>/<color>')
def play(number, color):
    return render_template('playground2.html',num=int(number), color=color)


if __name__=="__main__":
    app.run(debug=True) 


