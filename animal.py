class Animal(object):
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
        print "Health of", self.name, "=", self.health

class Dog(Animal):
    def __init__(self, name):
        health = 150
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        health = 170
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a dragon!"
        return self


# Test out the classes 
g = Animal('GrrGrr', 50)
print "The giraffe will now walk three times, then run twice.  It's final health should be 37."
g.walk().walk().walk().run().run().display_health()
print "=" * 50

r = Dog('Rocky')
print "The dog will now walk three times, then run twice, then get pet once.  It's final health should be 142."
r.walk().walk().walk().run().run().pet().display_health()
print "=" * 50

p = Dragon('Puff')
print "The dragon will now walk, then run, then fly.  It's final health should be 154."
p.walk().run().fly().display_health()
print "=" * 50

# Check to confirm that GrrGrr cannot use the pet or fly methods
# g.pet() Got an error message: "AttributeError: 'Animal' object has no attribute 'pet'""
# g.fly() Got an error message: "AttributeError: 'Animal' object has no attribute 'fly'""

# Check to confirm that GrrGrr and Rocky will now say "I'm a dragon" when displaying health:
g.display_health()
r.display_health()

# Check to confirm that Rocky cannot fly
# r.fly() Got an error message: "AttributeError: 'Animal' object has no attribute 'fly'""