from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('playground.html')


@app.route('/')        
def hello_world():
    return 'Hello!' 

@app.route('/play/<number>')
def play(number):
    print(number)
    return render_template('play_time.html',num=int(number))



def hello_world():
  return render_template("index.html", first_name="Avani", last_name="Chandwaney")


if __name__=="__main__":
    app.run(debug=True) 



from flask import Flask, render_template
app = Flask(name)
@app.route('/')
def index():
    return render_template('play_time.html')
@app.route('/play/<number>')
def play(number):
    print(number)
    return render_template('play_time.html',num=int(number))
if name=="main":
    app.run(debug=True)

