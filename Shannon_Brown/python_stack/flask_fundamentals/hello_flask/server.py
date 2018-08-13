from flask import Flask  
app = Flask(__name__)    
                         
@app.route("/")        
def index ():
		return "Hello World"

@app.route("/coding") 
def coding():
    return "<h1>Dojo</h1>" 

@app.route("/say/flask") 
def flask():
    return "Hi Flask" 

@app.route("/say/michael") 
def michael():
    return "Hi Michael" 

@app.route("/say/john") 
def john():
    return "Hi John" 

@app.route("/repeat/35/hello") 
def hello():
    return "hello " * 35

@app.route("/repeat/80/hello") 
def hello2():
    return "hello " * 80

@app.route("/repeat/99/dogs") 
def dogs():
    return "dogs " * 99

if __name__ == '__main__':                          	                        
    app.run(debug=True)    