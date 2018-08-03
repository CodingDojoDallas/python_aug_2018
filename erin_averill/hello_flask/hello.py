# from flask import Flask 	#import Flask to allow us to make app
# app = Flask(__name__)   	# Global variable __name tells Flask whether or not we are 
#                         	# running the file directly, or importing it as a module
# print(__name__)  
# 					       	# just for 'fun' to see what it prints
# @app.route('/')         	# the @ symbol designates a decorator which attaches the following
# def hello_world():			
# 	return render_template("index.html")	# function to the '/' route. Meaning that when we send a request
# 							#to the localhost:5000/ we will run the "hello_world" function
# @app.route('/totally')
# def totally():
# 	return "success"

# @app.route('/more')
# def more():
# 	return "I've got a lovely bunch of coconuts"

# 							#return string 'Hello World!' as response
# if __name__=="__main__":	# if __name__ is "__main__" we know we are running the file directly
# 							# and not importing it from a different module
# 	app.run(debug=True)		# run app in debug mode


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return render_template('index.html', phrase="hello", times=5, list=[1,2,3,4])

# if __name__=="__main__":
# 	app.run(debug=True)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['name']
    email = request.form['email']
    # redirects back to the '/' route
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True) 
