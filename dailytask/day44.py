#Create a Vehicle class with a method start() that prints "Vehicle is starting".
#Create a Car class that inherits from Vehicle and overrides start() to print "Car starts with a key".
#Create a Car object and call start(). Expected Output: Car starts with a
"""
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("car strats with a  key")
call=Car()
call.start()

"""
#Create Dog and Cat classes. Both classes should have a method sound().
#Dog.sound() should print "Dog barks" Cat.sound() should print "Cat meows"
#Create objects of both classes and call sound() using the same variable name one after another.Expected Outpu
"""class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("cat meows")

ob=Dog()
og=Cat()
ob.sound()
og.sound()"""

#Create Bike and Car classes with a method move(). Bike.move() →
#"Bike moves on two wheels" Car.move() → "Car moves on four wheels" Create a function show_movement(vehicle)
#that calls vehicle.move().Pass both objects to the function. Expected Output: Bike
"""class Bike:
     def move(self):
         print("Bike moves on two wheels")
class Car:
    def move(slef):
        print("car moves on four wheeels")
def show_movement(vehicle):
    vehicle.move()
ob=show_movement(Car())
"""
#Create a parent class Employee with a method salary() that prints "Basic Salary".
#Create two child classes: Developer → salary() prints "Developer Salary: 50000"
#Tester → salary() prints "Tester Salary: 40000" Create objects of both child classes and call
"""class Employee:
    def  salary(slef):
        print("Basic salary")
class Developer(Employee):
    def salary(self):
        print("Developer salary:50000")
class Tester(Developer):
    def salary(self):
        print("tester salary: 40000")
ob=Developer()
og=Tester()
ob.salary()
og.salary()"""
#Create a parent class Shape with a method area() that prints "Area of Shape". Create Circle
#and Rectangle classes that inherit from Shape. Circle.area()
#→ print "Circle Area" Rectangle.area() → print "Rectangle Area" Store both objects in a list and use a
class Shape:
    def area(self):
        print("Aera of shape")
class Circle(Shape):
    def area(self):
        print("circle area")
class Reactangle(Shape):
    def area(self):
      print("Reactangle")
ob=[Shape(),Circle(),Reactangle()]
for i in ob:
    i.area()
    
    
