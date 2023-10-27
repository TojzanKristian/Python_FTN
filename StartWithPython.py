# Types - Tipovi - Típusok
# Numbers - Brojevi - Számok
print("Types in python :")
print("Numbers :")
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
print("Bool :")
T = True
print(T)
F = False
print(F)
print()

# String - Tekst - Szöveg
print("String :")
name = "James"
print(name)
name1 = 'Amelia'
print(name1)
print()

# List - Lista - Lista
print("List :")
H = [10, 20, 50]
print(H)
X = [1.67 , 3.93, 59.91]
print(X)
Y = X = [1 , 3.95, "Someting", True]
print(Y)
print()

# Tuple - Torka - Tuple
# Tuple is IMMUTABLE - Torka je nepromenljiva - A Tuple megváltoztathatatlan
print("Tuple :")
K = (22, 44)
print(K)
J = (2.99, 4.487)
print(J)
P = (22, 4.44, True, 'OK')
print(P)
print()

# Dictionary - Rečnik - Szótár
print("Dictionary :")
G = {'Tina': 55,'Gina': 65,'Erik': 99,'Helen': 19}
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


# Bitwise operators - Operatori nad bitima - Bitekkel való operálás
print("Bitwise operators in python :")
a = 2 # 00000010
b = 3 # 00000011
print(a&b) # 00000010 -> 2  AND - Logički i - Logikai és
print(a|b) # 00000011 -> 3  OR - Logički ili - Logikai vagy
print(a^b) # 00000001 -> 1  XOR - Ekskluzivno ili - Kizárólag vagy
print(~a) # 11111101 -> –3  NOT - Negacija - Tagadás
print(a << 2) # 0001000 -> 8   Left Shift - Pomeranje u levo - Balra tolás
print(a >> 2) # 0000000 -> 0    Right Shift - Pomeranje u desno - Jobbra tolás
print()
print()


# is/is not - jeste/nije - van/nincs
print("is/is not in python :")
a = 8

if type(a) is str:
    print('True')
else:
    print('False')

if type(a) is int:
    print('True')
else:
    print('False')
print()
print()


# in/not in - u/nije u - benne van/nincs benne
print("in/not in in python :")
a = [1, 2, 3, 4, 5, 10]
if 1 in a:
    print('True')
else:
    print('False')

if 11 in a:
    print('True')
else:
    print('False')
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


# Classes - Klase - Osztályok
print("Classes in python :")
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


# How to comment - Kako dodavati komentare - Hogyan kommenteljünk
# Inline comment - linijski komentar - egy soros komment
"""
More line comment
Više linijski komentar
Több soros komment
"""


# Type function - Funkcija Type - Type függvény
print("Type function in python :")
x = 5
print(type(x))
y = "asd"
print(type(y))
h = []
print(type(h))
print()
print()


# Cast between types - Konverzija tipova - Tipusok konvertálása
print("Cast between types in python :")
a = 1
b = 1.11
x = int(a)
print(x)
y = int(b)
print(y)
k = float(a)
print(k)
j = float(b)
print(j)
t = str(a)
print(t)
i = str("a")
print(i)
p = str(b)
print(p)
print()
print()


# input function - Funkcija za unos preko konzole - Konzolról való olvasás
print("input functionin python :")
txt = input("Enter some text : ")
print(txt)
print()
print()


# A few useful functions for working with lists and tuples - Nekoliko korisnih funkcija za rad sa listama i torkama - Néhány hasznos függvény a listákhoz és a tuplekhez
print("A little more about lists :")
# Indexing a list - Indexiranje liste - Lista indexelése
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
print(lista[0]) # indexes start from 0 - indexi počinju od 0 - az indexek 0-tól indulnak
print(lista[2]) # the second element from the list - drugi element iz liste - a lista második eleme
print(lista[2:5]) # everything between the second and fifth elements - sve između drugog i petog elementa - a második és az ötödik elem közötti elemek
print(lista[:3]) # everything up to the third element - sve do trećeg elementa - minden eleme a harmadik elemig
print(lista[3:]) # everything after the third element - sve posle trećeg elementa - minden elem a harmadik elem után

# append - dodavanje u listu - elem hozzáadása a listához
list = [1, 2, 3]
list.append(4)
print(list)

# insert - dodavanje u listu na određeno mesto - elem hozzáadása a listához a megadott pozícióra
list.insert(2, 3)
print(list)

# remove - brisanje elementa iz liste - elem eltávolitása a listából
list.remove(3)
print(list)

# pop - preuzimanje elementa iz liste - elem eltávolitása a listából
popped_element = list.pop(2)
print(list)
print(popped_element)

# index - pozicija/index elementa u listi - elem pozíciójának meghatározása
index = list.index(4)
print(index)

# count - broji koliko ima zadatog elementa u listi - megszámolja hányszor fordul elő az adott elem a listában
count = list.count(1)
print(count)

# sort - sortiranje liste - elemek sorbarakása
list.sort()
print(list)

# reverse - obrtanje liste - lista invertálása
list.reverse()
print(list)

# extend - spajanje više listi u jednu - listák összekapcsolása
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1.extend(list2)
print(list3)

# clear - prazni listu - listák tartalmának törlése
list.clear()
print(list)
print()

print("A little more about tuples :")
# Indexing of the tuple - Indexiranje torke - Tuple indexelése
tuple = (1, 2, 3, 4)
element = tuple[2]
print(element)

# count - broji koliko ima zadatog elementa u listi - megszámolja hányszor fordul elő az adott elem a listában
tuple1 = (1, 2, 2, 3, 2, 4)
count = tuple1.count(2)
print(count)

# index - pozicija/index elementa u listi - elem pozíciójának meghatározása
index = tuple.index(3)
print(index)

# len - dužina/broj elemenata liste - lista hossza/elemeinek száma
lenght = len(tuple) 
print(lenght)
print()
print()


# A few useful functions for working with the dictionaries - Nekoliko korisnih funkcija za rad sa rečnikom - Néhány hasznos függvény a szótárakkal való munkához
print("A little more about dictionaries :")
dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing Values - Pristup vrednostima u rečniku - Szótárak értékeihez való hozzáférés
name = dict['name']
print(name)
age = dict['age']
print(age)

# Adding and modifying items - Dodavanje i modofikacija elemenata - Elemek hozzáadása és módisítása
dict['job'] = 'Engineer' 
print(dict)
dict['age'] = 31
print(dict)

# Removing items - Brisanje elemenata - Elemek eltávolítása/törlése
del dict['city']
print(dict)
dict.pop('job')
print(dict)

#  Return all the keys in the dictionary - Vraće sve ključeve iz rečnika - A szótárban lévő kulcsokat adja vissza
print(dict.keys())

#  Return all the values in the dictionary - Vraće sve vrednosti iz rečnika - A szótárban lévő elemek értékét adja vissza
print(dict.values())

# Returns all key-value pairs - Vraće sve parove ključ-vrednost iz rečnika - Kulcs-érték párok kiolvasása a szótárból
print(dict.items())

# Removes all items from the dictionary - Brisanje svih vrednosti iz rečnika - Minden elem törlése a szótárból
print(dict.clear())

# Copy dictionary to another - Kopiranje celog rečnika u drugi - Szótár másolása egy másikba
dict = {'name': 'John', 'age': 30, 'city': 'New York'}
dict1 = dict.copy()
print(dict1)
print()
print()


# Some useful functions for strings - Neke korisne funkcije za stringove - Néhány hasznos függvény a stringekhez/szöveghez
print("A little more about strings :")
string = "Hi Alex !"

# Indexing strings - Indexiranje stringova - Stringek szeletelés/indexelése
print(string[0])
print(string[0:5])
print(string[-1])

# Specifies the position of the specified character - Određuje index navedenog znaka - A megadott karakter pozícióját adja meg
print(string.index("!"))

# Specifies the length of the string - Određuje dužinu stringa - A megadott szöveg hosszát adja meg
print(len(string))

# Tells you if the string starts with that word - Govori nam da li string počinje na zadatu reč - Megmondja hogy az adott szóval kezdődik-e a string
print(string.startswith("Helo"))
print(string.startswith("Hi"))

# Tells you if the string ends with that word - Govori nam da li se string završava na zadatu reč - Megmondja hogy az adott szóval végződik-e a string
print(string.endswith("Nope"))
print(string.endswith("!"))

# Replace - Zameni prvu reč sa drugom - Az első szót kicseréli a másodikra
s = string.replace("Alex", "Nikole")
print(s)

b = "        Nothing          "

# Delete empty characters (spaces) - Izbacivanje praznina - Üres karakterek törlése
print(b.strip())
print(b.lstrip())
print(b.rstrip())

c = "1,2,3,4,5,6,7,8,9,10"
# Split - Podela po određenom znaku - Feldarabolja a szöveget a megadott karakter pozícióin
c1 = c.split(",")
print(c1)

# Formatting strings - Formatiranje ispisa - Stringek formázása
# First method - Prvi način - Első módszer
t = "Your name is %s and %d are years old" % ("Edit",32)
print(t);print()

# Second method - Drugi način - Második módszer
j = "Your name is {} and you are {} years old".format("Jani",25)
print(j);print()

name = input("Please enter your name : ")
age = input("Please enter your age : ")
k = f"Your name is {name} and you are {age}"
print(k)
print()
print()


# Keywords - Ključne reči - Kulcsszavak

# None - Nijedan - Egyik sem
# True - Tačno - Igaz
# False - Netačno - Hamis
# and - Ligičko i - Logikai ÉS művelet
# or - Ligičko ili - Logikai VAGY művelet
# not - Negacija - Logikai NEM művelet
# is - Jeste - Van
# is not - Nije - Nincs
# in - U - Benne van
# not in - Nije u - Nincs benne
# if - If grananje - If elágazások
# else - Sledi posle if - Az if után következik
# elif - Skraćenica od else if - Az else if rövidítése
# for - Petlja - Ciklus
# while - Petlja - Ciklus
# def - Označavenje funkcije - Függvény definícióját jelenti
# return - Povratna vrednost - A függvény visszatérési értékét adja vissza
# class - Označava klasu - Osztály definícióját jelenti
# import - Za upotrebu modula/biblioteka - Modulok vagy fájlok importálására szolgál
# from - Sledi posle import da označi šta iz tog modula hoćemo - Az import-nál jelzi, hogy csak bizonyos elemeket importálunk a modulból
# as - Kod importa, da promeni naziv - Az import-nál használható, hogy átnevezzük az importált elemeket
# try - Za obradu izuzetaka - Hiba lekezelő blokk kezdeményezése
# except - Osim - Kivéve
# raise - Da se označi mogući izuztak - Kivétel kiemelése
# finally - Sledi posle try-except i uvek se izvršava - A try-except blokkok után következik, és mindig végrehajtódik


# Most used modules - Najčešće korišćeni moduli/biblioteke - Leghasználtabb modulok

# math - Matematičke operacije - Matematikai műveletek
# os - Za rad sa operativnim sisteamom - Operációs rendszer-szintű műveletek
# sys - Za informacije o interpretaru i sistemu - Interpreterrel és a rendszerrel kapcsolatos információkat tartalmazza
# random - Random brojevi - Véletlenszámok generálásához
# datetime - Datumi i vreme - Dátum- és időkezeléshez
# requests - Za obradu HTTP zahteva - HTTP kérések küldésére és fogadására használható
# json - Rad sa JSON objektima - JSON (JavaScript Object Notation) adatok olvasására és írására
# csv - Rad sa CSV fajlovima - CSV (Comma-Separated Values) fájlok olvasására és írására
# sqlite3 - Rad sa bazama podataka - Adatbáziskezelésre használható, különösen SQLite adatbázisokhoz.
# numpy - Matematički i naunči računi - Matematikai és tudományos számításokhoz
# pandas - Rad sa tabelama podataka -  Adattáblák létrehozása, manipulálása és elemzése
# matplotlib - Crtanje grafikona - Adatvizualizációhoz és grafikonok készítéséhez
# seaborn - Isto za crtanje grafikona - Adatvizualizációhoz és grafikonok készítéséhez
# flask, Django - Za rad sa web aplikacija - Webalkalmazások fejlesztésére szolgálnak
# tensorflow, pytorch - Mašinsko učenje i neuronske mreže - Gépi tanulás és neurális hálózatok fejlesztéséhez

print("Good luck working with python")