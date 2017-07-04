# declare a class and give it the name User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self

# make instances of the class User
user1 = User('Anna Propas', 'anna@anna.com')
print user1.name
print user1.logged
print user1.email
