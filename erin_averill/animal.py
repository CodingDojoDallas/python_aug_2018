class Animal:
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print(self.health)
class Dog(Animal):
	def __init__(self, name, health = 150):
		super().__init__(name, health)
	def pet(self):
		self.health += 5
		return self
class Dragon(Animal):
	def __init__(self, name, health = 170):
		super().__init__(name, health)
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		super().display_health()
		print('I am a Dragon')
		return self

animal1 = Animal('donkey', 10)
animal1.walk().walk().walk().run().run().display_health()


dog2 = Dog('fido')
dog2.walk().walk().walk().run().run().pet().display_health()


dragon3 = Dragon('Danny')
dragon3.fly().fly().display_health()



