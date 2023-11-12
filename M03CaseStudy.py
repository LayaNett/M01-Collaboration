'''Layla Nettavong
M03Case Study Python
An app that will take user input and organize it using classes
'''

#Super class that stores type of automobile
class Vehicle():
    def __init__(self,type):
        self.type = type

#Class holding the values of a car
class Automobile(Vehicle):
    def __init__(self,year,make,model,doors,roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Asks user for vehicle info
type = input("What type of vehicle do you have (Car, motorcycle, bus, broomstick?)")
year = input("What year is your automobile?")
make = input("What make is your automobile?")
model = input("What model is your automobile?")
doors = input("How many doors for you automobile have?")
roof = input("What kind of roof does your automobile have?")


#Final output and formatting
print ( f"Vehicle:  {type} \nYear:  {year} \nMake:  {make} \nModel:  {model} \nNumber of doors:  {doors} \nType of roof:  {roof}" )