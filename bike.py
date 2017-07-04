class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "Price:", self.price
        print "Maximum Speed", self.max_speed
        print "Total Miles", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self
    

bike1 = Bike(100, "10mph")
bike2 = Bike(150, "20mph")
bike3 = Bike(200, "25mph")

print "Bike 1 is riding 3 times, then reversing, then displaying the info"
bike1.ride().ride().ride().reverse().displayinfo()
print "=" * 50
print "Bike 2 is riding 2 times, then reversing 2 times, then displaying the info"
bike2.ride().ride().reverse().reverse().displayinfo()
print "=" * 50
print "Bike 2 is reversing 3 times, then displaying the info"
bike3.reverse().reverse().reverse().displayinfo()
