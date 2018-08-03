class Bike:
    def __init__(self, price, max_speed, total_miles=0):
        self.price = price
        self.max_speed = max_speed
        self.total_miles = total_miles
    def ride(self):
        print("Riding")
        self.total_miles = self.total_miles + 10
        return self
    def reverse(self):
        if self.total_miles:
            print("Reversing")
            self.total_miles = self.total_miles - 5
            return self
    def display(self):
        print(f'$ {self.price}', f'{self.max_speed}mph', self.total_miles)
        return self


bike1 = Bike(200, 250, 10)
bike1.ride().ride().ride().reverse().display()

bike2 = Bike(20, 30, 0)
bike2.ride().ride().reverse().reverse().display()

bike3 = Bike(10, 15, 10)
bike3.reverse().reverse().reverse().display()

# to prevent a negative I added the if statement 