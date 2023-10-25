# Task 1 - Zadatak 1 - 1. Feladat
# Assign the value of the following expression to the variable x: 5^2 + 3/4
# Dodeliti vrednost sledećeg izraza promenljivoj x: 5^2 + 3/4
# Rendeld hozzá a következő kifejezés értékét az x változóhoz: 5^2 + 3/4
print("Task 1 :")
x = 5**2 + 3/4
print(x)
print()
print()


# Task 2 - Zadatak 2 - 2. Feladat
# Let a = 17, and b = 3. Determine the quotient and the rest when dividing
# Neka je a = 17, a b = 3. Odrediti količnik i ostatak pri deljenju
# Legyen a = 17, és b = 3. Határozza meg a hányadost és a maradékot osztáskor
print("Task 2 :")
a = 17
b = 3 
print(a//b)
print(a%b)
print()
print()


# Task 3 - Zadatak 3 - 3. Feladat
# Write a logical expression that will return TRUE if a is between 5 and 10
# Napisati logički izraz koji će vratiti tačno ukoliko se a nalazi između 5 i 10
# Írj egy logikai kifejezést, amely IGAZAT ad vissza, ha a 5 és 10 között van
print("Task 3 :")
a = 8
expression = a >= 5 and a <= 10
print(expression)
print()
print()


# Task 4 - Zadatak 4 - 4. Feladat
# Ask the user to enter two real numbers, add them up and print the result
# Tražiti od korisnika da unese dva realna broja, sabrati ih i ispisati rezultat
# A felhasználó vigyen be két valós számot és az összegüket ki kell írni
print("Task 4 :")
r1 = float(input("Enter a real number : "))
r2 = float(input("Enter a real number : "))
print("Result is :",  r1 + r2)


# Task 5 - Zadatak 5 - 5. Feladat
# Ask the user to enter text, lowercase it, delete all space characters from both ends of that text and divide it by space
# Tražiti od korisnika da unese tekst, prebaciti ga u mala slova, obrisati sve space karaktere sa oba kraja tog teksta i podeliti ga po razmaku
# Kérje meg a felhasználót, hogy írjon be szöveget, minden betű legyen kisbetű, törölje az összes szóköz karaktert a szöveg mindkét végéről, és ossza el szóközzel

tekst = input("Please enter text : ")
result = tekst.strip().lower().split(" ")
print(result)