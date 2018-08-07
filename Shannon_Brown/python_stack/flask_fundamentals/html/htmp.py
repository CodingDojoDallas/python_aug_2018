from flask import Flask, render_template  
app = Flask(__name__)    

print(__name__) 
         				 
@app.route("/")                                   
def checkered():
    return render_template ("htmp.html")

if __name__=="__main__":
    
    app.run(debug=True)