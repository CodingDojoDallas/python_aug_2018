class Product:
		def __init__(self, price, item_name, weight, brand, status='for sale'):
			self.price = price
			self.item_name = item_name
			self.weight = weight
			self.brand = brand
			self.status = status
		def sell(self):
			self.status = 'sold'
			return self
		def tax(self, sales_tax):
			self.price += sales_tax
			return self.price
		def return_item(self, reason_for_return):
			if reason_for_return == 'defective':
				self.status = 'defective'
				self.price = 0
			elif reason_for_return == 'opened':
				self.status = 'used'
				self.price *= 0.8
			elif reason_for_return == 'like new':
				self.status = 'for sale'
			return self
		def display_all(self):
			print(self.price, self.item_name, self.weight, self.brand, self.status)


product1 = Product(10,'car',10,'jaguar','defective')
product1.return_item('like new').display_all()
