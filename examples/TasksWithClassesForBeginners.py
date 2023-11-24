# Task 1 - Zadatak 1 - Feladat 1
# Write a class triangle
# Napiši klasu trougao
# Írj egy háromszög osztály
class Triangle:
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
      
T1 = Triangle(3, 4, 5)
print("Length of a : " + str(T1.a) +"\n" + "Length of b : " + str(T1.b) + "\n" + "Length of c : " + str(T1.c) + "\n");print()


# Task 2 - Zadatak 2 - Feladat 2
# Write a circle class with a method that calculates area
# Napiši klasu krug sa metodom izračunaj površinu 
# Írj egy kör osztályt egy metódussal, mely területet számít
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.radius, 2)

circle1 = Circle(5)
area1 = circle1.calculate_area()
print(f"Circle 1 Area: {area1}")
print();print()


# Task 3 - Zadatak 3 - Feladat 3
# Write a shape class inherited by a circle class and a square class
# Napisati klasu oblik koju nasleđuju klase krug i kvadrat
# Írj egy alakzat osztályt, melyet egy kör osztály és egy négyzet osztály örökölnek
class Shape:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def get_area(self):
        return  math.pow(self.side_length, 2)

c1 = Circle("Circle 2", 5)
a1 = c1.get_area()
print(f"{c1.name} Area: {a1}")

square1 = Square("Square 1", 4)
a2 = square1.get_area()
print(f"{square1.name} Area: {a2}")
print();print()


# Task 4 - Zadatak 4 - Feladat 4
# Write a student class
# Napiši klasu student
# Írj egy tanuló osztályt
class Student:
    def __init__(self, firstName, secondName, numberOfIndex):
      self.firstName = firstName
      self.secondName = secondName
      self.numberOfIndex = numberOfIndex
    
    def __str__(self):
       return f"{self.numberOfIndex} {self.firstName} {self.secondName}"
    
s1 = Student("Kris", "Kirinski", "PA100/2018")
print(s1)
s2 = Student(firstName="Nikolas", secondName= "Nikson", numberOfIndex="IN1/2019")
print(s2)
print();print()


# Task 5 - Zadatak 5 - Feladat 5
# Write a class describing height measurements by cities in Serbia
# Napisati klasu koja opisuje merenja visine po gradovima u Srbiji
# Írj egy osztályt, amely leírja a magasságméréseket városok szerint Szerbiában
class Measurement:
    def __init__(self, city, measurements):
       self.state = "Serbia"
       self.city = city
       self.measurements = measurements

    def __str__(self):
       return f"{self.state}, {self.city}, {self.measurements}"
    
    def averageOfHeight(self):
       return sum(self.measurements)/len(self.measurements)
    
novi_sad = Measurement("Novi Sad", [1.75, 1.80, 1.65, 2.02, 1.90, 1.68, 1.73])
sombor = Measurement("Sombor", [1.85, 1.80, 1.75, 2.02, 1.95, 1.78, 1.83])
zrenjanin = Measurement("Zrenjanin", [1.75, 1.70, 1.67, 2.00, 1.80, 1.78, 1.73])

print("Average height in the city : ")
print(f"{novi_sad.city}, average height: {novi_sad.averageOfHeight()}")
print(f"{sombor.city}, average height: {sombor.averageOfHeight()}")
print(f"{zrenjanin.city}, average height: {zrenjanin.averageOfHeight()}")