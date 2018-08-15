from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
    #cities
    #objects

class City(models.Model):
	name = models.CharField(max_length=145)
	state = models.ForeignKey(State,related_name="cities")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Highway(models.Model):
	name = models.CharField(max_length=200)
	cities = models.ManyToManyField(City, related_name="highways")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# def __str__(self):
	#  	return self.name
	def __repr__(self):
		return "<Highway object: {}>".format(self.name)





