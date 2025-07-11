"""
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
d =Dog()
print(d.speak())
d.bark()    
"""

"""
class User:
    def __init__(self, role):
        self.role = role
        
def create_user(role):
        return User(role)
    
u = create_user("admin")
print(u.role)
"""

class Singleton:
    _instance = None
    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b) 
