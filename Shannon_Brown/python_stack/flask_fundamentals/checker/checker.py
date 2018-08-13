from flask import Flask, render_template  
app = Flask(__name__)    
@app.route("/")                        
def index():
	return "Welcome Home"
         				 
@app.route("/play")                                   
def play():
    return render_template ("playground.html")

@app.route("/play/<var>")                                  
def box_7(var):
	v = int (var) 
	return render_template ("playground2.html", num = v)

@app.route("/play/<var>/<color>")                                 
def box_5(var, color):
	v = int (var)
	return render_template ("playground3.html", num = v)

if __name__== "__main__":
    app.run(debug=True)