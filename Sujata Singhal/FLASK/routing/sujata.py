from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')        
def hello_world():
    return 'Hello!'  # Return the string 'Hello World!' as a response.

@app.route('/dojo')
def dojo():
  return "Dojo3!"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    print(name)
    return "Hi "+name

@app.route('/repeat/<num>/<stuff>')
def repeat(num, stuff):
	print(num)
	print(stuff)
	return (stuff + " ") * int(num)



@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
	app.run(debug=True) 





# localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request.
# localhost:5000/say/michael - have it say "Hi Michael" (have the same function say() handle this routing request)
# localhost:5000/say/john - have it say "Hi John!" (have the same function say() handle this routing request)
# localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 35.  To do this use int().  For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, it should say "hello" 80 times.
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)