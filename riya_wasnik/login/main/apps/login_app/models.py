from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	#input == request.POST
	def validation_registration(self, input):
		error=[]
		if(len(input['name'])<3):
			error.append("Name should have atleast 3 characters")
		if not EMAIL_REGEX.match(input['email']):
			error.append("Invalid email format")
		if input['password'] != input['confirm_password']:
			error.append("Passwords donot match")
		return error
		
	def validation_login(self, input):
		error = []
		# try:
		# 	user = User.objects.get(email=request.POST['email'])
		# except:
		# 	print("error")
		user = User.objects.filter(email=input['email'])
		if len(user) == 0:
			error.append("Email doesnot exist")
			return error
		if bcrypt.checkpw(input['password'].encode(), user[0].password.encode()):
			print("password match")
		else:
			error.append("passwords donot match")                  
		return error

class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	objects = UserManager()
