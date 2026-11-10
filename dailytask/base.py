"""Create a Python program for a *Ride Booking System*.
A customer can book different types of rides such as *Bike* or *Car*.
### Requirements:
1. Create an abstract class Ride with an abstract method calculate_fare().
2. Create two child classes:
        * Bike
        * Car
3. Both classes should implement calculate_fare() differently.
4. Store the distance as a *private attribute* and provide methods to set and get the distance.
5. Create a Customer class to store the customer's name and pickup location.
6. Ask the user to select the ride type and enter the required details.
7. Display the customer details and calculated fare.
### Example Input:
Enter customer name: Ravi
Enter pickup location: Madhapur
Enter distance: 10
Enter ride type: Bike
### Expected Output:
Customer: Ravi
Pickup Location: Madhapur
Ride Type: Bike
Distance: 10 km
Fare: 100
Ride booked successfully
*Assume:*
* Bike fare = ₹10 per km
* Car fare = ₹20 per km"""
#from abc import ABC,abstractmethod
user=input("choice the Ride (1.bike/2.car)")
class Ride:
    #@absractmethod
    def calculate_fare(self,d):
        self.dist=d

class Bike(Ride):
        #@abstractmethod
        def calculate_fare(self,d):
            self.dist=d
            print("Bike fare",self.d*10)
class Car(Ride):
       # @abstractmethod
    def calculate_fare(self,d):
            self.dist=d
            print("car fare",slef.dist*20)
class Customer:
    def __init__(self,name,pick):
        self.name=name
        self.location=pick
        print("customer:",self.name)
        print("Pickup Location:",self.location)
        
og=Ride()
og.calculate_fare(50)
ob=Customer("vignesh","madper")


        
    
    
