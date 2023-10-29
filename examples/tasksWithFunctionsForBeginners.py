# Task 1 - Zadatak 1 - Feladat 1
# Write a function that accepts a list as a parameter and sorts it
# Napisati funkciju koja prihvata listu kao parametar i sortira je
# Írj egy függvényt, mely paramétere egy lista és rendezi a lista elemeit
list = [2, 15, 5, 28, 9, 30, 4]

def solution(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

print("List before sort : ", list)
result = solution(list)
print("List after sort : ", result)
print();print()


# Task 2 - Zadatak 2 - Feladat 2
# Write a function that receives a list and extracts even numbers and all negative numbers
# Napisati funkciju koja prima listu i izdvaja se parne brojeve i sve negativne brojeve
# Írj egy függvényt, amely paramétere egy lista, és visszaadja a páros számokat és negatív számokat
list2 = [2, -3, 5, -8, 10, 7, -12]

def filter_even_negative_numbers(input_list):
    result = []
    for num in input_list:
        if num % 2 == 0 or num < 0:
            result.append(num)
    return result

print("List :", list2)
filtered_list = filter_even_negative_numbers(list2)
print("Even and negative items in the list : ", filtered_list)
print();print()


# Task 3 - Zadatak 3 - Feladat 3
# Write a function that magnifies each element of a given list by 10, but so that all values remain strings
# Napisati funkciju koja uvećava svaki element date liste za 10, ali tako da sve vrednosti ostanu stringovi
# Írj egy függvényt, amely egy adott lista minden elemét 10-zel növeli, de úgy, hogy minden érték karakterlánc maradjon
list3 = [2, 15, 5.5, -3, "hello"]

def increase_and_convert_to_str(input_list):
    result = []
    for num in input_list:
        if isinstance(num, (int, float)):
            increased_num = num + 10
            result.append(str(increased_num))
    return result

print("List :", list3)
modified_list = increase_and_convert_to_str(list3)
print("List items after incrementing by 10 : ", modified_list)
print();print()


# Task 4 - Zadatak 4 - Feladat 4
# Write a function that has a variable number of parameters, if more than three parameters are passed, the function returns their sum, otherwise returns their product
# Napisati funkciju koja ima promenljiv broj parametara, ako je prosleđeno više od tri parametra, funkcija vraća njihovu sumu, u suprotnom vraća njihov proizvod
# Írj egy függvényt, melynek változó számú paramétere lehet, ha háromnál több van a függvény visszaadja az összegüket, egyébként a szorzatukat
def function_task4(*args):
   if len(args) > 3:
    return sum(args)
   else:
      p = 1
      for arg in args:
         p *= arg
      return p
   
print("Product (2,3) => ", function_task4(2, 3))
print("Sum (2, 3, 7, 13) => ",function_task4(2, 3, 7, 13))
print();print()


# Task 5 - Zadatak 5 - Feladat 5
# Write a function that implements the Pythagorean theorem
# Napisati funkciju koja implementira Pitagorinu teoremu
# Írj egy függvényt, amely megvalósítja a Pitagorasz-tételt
import math

def pythagorean_theorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

kate_a = 3
kate_b = 4
hypotenuse = pythagorean_theorem(kate_a, kate_b)
print(f'The length of the hypotenuse is: {hypotenuse}')