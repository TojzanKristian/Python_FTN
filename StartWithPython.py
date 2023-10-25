# Types - Tipovi - Tipusok
# Numbers - Brojevi - Számok
print("Types in python :")
a = 5
print(a)
b = 3.14
print(b)
c = 5 + 56j
print(c)
d = 32.3e18
print(d)
print()

# Bool - Tačno/Netačno - Igaz/Hamis
T = True
print(T)
F = False
print(F)
print()

# String - Tekst - Szöveg
name = "Kristof"
print(name)
name1 = 'Helga'
print(name1)
print()

# List - Lista - Lista
H = [10, 20, 50]
print(H)
X = [1.67 , 3.93, 59.91]
print(X)
Y = X = [1 , 3.95, "Someting", True]
print(Y)
print()

# Tuple - Torka - Tuple
K = (22, 44)
print(K)
J = (2.99, 4.487)
print(J)
P = (22, 4.44, True, 'OK')
print(P)
print()

# Dictionary - Rečnik - Szótár
G = {'Tina':55,'Gina':65,'Erik':99,'Helen':19}
print(G)
print()
print()


# Arithmetic operators - Aritmetički operatori - Aritmetikai operátorok
# +, - , *, /, //, **, %
print("Arithmetic operators in python :")
a = 2
b = 5
print(a+b) # Sum - Sabiranje - Összeadás
print(b-a) # Subtraction - Oduzimanje - Kivonás
print(a*b) # Multiplication - Množenje - Szorzás
print(b/a) # Division - Deljenje - Osztás
print(b//a) # Integer division - Celebrojno deljenje - Egész számú osztás
print(a**b) # Power - Kvadrat - Hatvány
print(b % a) # Modulus - Moduo - Modulus
print()
print()


# Value assignment operators - Operatori dodele vrednosti - Értékadó operátorok
# =, +=, -=, *=, /=, **=, //=, %=
print("Value assignment operators in python :")
a = 6
print(a)

a += 1
print(a)

a = 6
a -= 1
print(a)

a = 6
a *= 2
print(a)

a = 6
a /= 2
print(a)

a = 6
a **= 2
print(a)

a = 6
a //= 2
print(a)

a = 6
a %= 8
print(a)
print()
print()


# Comparison operators - Operatori upoređivanja - Összehasonlító operátorok
# <, >, <=, >=, !=, ==
print("Comparison operators in python :")
a = 15
b = 5

print(a < b) # Smaller - Manje - Kisebb
print(a > b) # Greater - Veće - Nagyobb
print(a <= b) # Less equal to - Manje jednako - Kisebb egyenlő
print(a >= b) # Greater equal to - Veće jednako - Nagyobb egyenlő
print(a != b) # Different - Različito - Különböző
print(a == b) # Equal - Jednako - Egyenlő
print()
print()


# Logical operators - Logički operatori - Logikai operátorok
# and, or, not
print("Logical operators in python :")
a = 5
b = 15
c = True

print(a < b and a != 8) # And - Logičko i - Logikai és
print(a < b or a == 5) # Or - Logičko ili - Logikai vagy
print(not c) # Not - Logičko ne - Logikai tagadás
print()
print()


# If branchings - If grananja - If elágazások
print("If branchings in python :")
a = 10
b = 5
if a > b:
    print(a)
else:
    print(b)

# If ternary
a = input("Please enter 'HUN' or 'ENG' : ")
print("Hungarian") if a == "HUN" else (print("English") if a == "ENG" else print("Other"))
print()
print()


# For - For petlja - For ciklus
print("For in python :")
for i in range(5):
     print(i)

a2 = [1, 2, 3, 4, 5]
print(len(a2))

for i in range(len(a2)):
     print(a2[i])

for i in a2:
    print(i)
print()
print()


# While - While petlja - While ciklus
print("While in python :")
a = 0
while a < 5:
     a += 1
     print(a)
print()
print()


# Functions - Funkcije - Függvények
print("Functions in python :")
a = 10
b = 20

def add0():
    print(a + b)

def add_1(c, d):
    return c + d

def k_2(*args):
    return sum(args)

add0()
h = (add_1(50, 5))
print(h)
print(k_2(10, 20, 30, 40))

# Recursive Function - Rekurzivne funkcije - Rekurzív függvények
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fib(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

for n in range(1,15):
    print(fib(n))

# Anonymous Functions, Lambda expressions - Lambda funkcije - Lambda (névtelen) függvények, képletek
add = lambda t, k: t + k
print(add(55,21))
print()
print()


# Try-except - Pokušaj-osim - Próbád ki-kivéve
print("Try-except in python :")
a = [1, 2, 3]
try:
    print()
except NameError as i:
    print(i)

try:
    print(a[5])
except IndexError as i:
    print(i)

try:
    print(1/0)
except ZeroDivisionError as i:
    print(i)
print()
print()


# Modules in python - Moduli/biblioteke - Modulok
print("How to import and use modules in python :")
import math
from math import sin
from math import cos, tan

print(math.pi)
print(math.sqrt(9))
print(sin(math.pi))
print(cos(math.pi))
print(tan(math.pi))
print()
print()


# Class - Klase - Osztályok
print("Class in python :")
class Person:
    name = ""
    age = None
    sex = ""

# Methods - Metode - Metódusok
    def set_name(self, value):
        self.name = value

    def set_age(self, value):
        self.age = value

    def set_sex(self, value):
        self.sex = value

p = Person()
p.name = 'Nikolas'
p.age = 25
p.sex = "M"
print(p.name, "\n",p.age, "\n",p.sex)

p1 = Person()
p1.set_name('Katrin')
p1.set_age(22)
p1.set_sex('W')
print(p1.name, "\n",p1.age, "\n",p1.sex)
print()

# __init__ method - __init__ metoda - __init__ metódus
class Person1:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.hello()

    def hello(self):
        print("Hi!", self.name, "your age is ", self.age ,"and your sex is ", self.sex)

k = Person1("Kimi", 22, 'M')
g = Person1("Nina", 44, 'W')
print()

# Inheritance - Nasleđivanje - Öröklődés
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Employee(Person):
    def __init__(self, name, age, sex, experience, reliability, education):
        super().__init__(name, age, sex)
        self.experience = experience
        self.reliability = reliability
        self.education = education
        self.hello()

    def hello(self):
        print("Hi!", self.name, ", your age is ", self.age, ", your sex is ", self.sex, ", your experience is ", self.experience, ", your reliability is ", self.reliability, ", your education is ", self.education)

employee = Employee("John Doe", 30, "Male", 5, 9.5, "Master's")
print()
print()