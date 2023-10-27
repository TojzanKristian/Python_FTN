# Working with lists - Rad sa listama - Listákkal való munka
print("Working with lists :");print()
list = [1, 11, 21, 33, 55, 99]

# Task 1 - Add 111 to the list
# Zadatak 1 - U listu dodati 111
# Feladat 1 - A listához add hozzá a 111-et
list.append(111)
print(list);print()

# Task 2 - Display the third item in the list
# Zadatak 2 - Ispis trećeg elementa iz liste
# Feladat 2 - A lista harmadik elemének kiírása
print(list[2]);print()

# Task 3 - Add element 8 to position 1
# Zadatak 3 - Dodati element 8 na poziciju jedan
# Feladat 3 - A 8 számot helyezd el az első pozíción
list.insert(1, 8)
print(list);print()

# Task 4 - Print all the elements between the second and fifth
# Zadatak 4 - Ispis svih elemenata između drugog do petog
# Feladat 4 - Nyomtassa ki az összes elemet a második és az ötödik között
print(list[2:5]);print()

# Task 5 - Delete the fourth element from the list and then and the entire list
# Zadatak 5 - Obrisati četvrti element iz liste i posle i celu listu
# Feladat 5 - Törölje a negyedik elemet a listából, majd a teljes listát
list.remove(list[3])
print(list);print()
del list
print(list);print();print()


# Working with dictionaries - Rad sa rečnicima - Szótárakkal való munka
print("Working with dictionaries :");print()
dict = {
 "mark": "Ford",
 "model": "Mustang",
 "age": 1964
}

# Task 1 - Print value under key model
# Zadatak 1 - Ispiši vrednost pod ključem model
# Feladat 1 - A model kulcshoz tartozó érték kiírása
print(dict["model"])
print(dict.get("model"));print()

# Task 2 - Add a new key-value pair that will define the color as yellow
# Zadatak 2 - Dodaj novi par ključ-vrednost koji će definisati da je boja žuta
# Feladat 2 - Adjon hozzá egy új kulcs-érték párt, amely a sárgát adja meg a szín értékeként
dict["color"] = "yellow"
print(dict);print()

# Task 3 - Change value under key years to 2003
# Zadatak 3 - Promeni vrednost pod ključem godina na 2003
# Feladat 3 - Az év kulcs értékét állítsd be 2003-ra
dict["age"] = 2003
print(dict)
dict.update({"age": 2003})
print(dict);print()

# Task 4 - Check if there is a value of 5 in the dictionary
# Zadatak 4 - Proveriti da li postoji vrednost 5 u rečniku
# Feladat 4 - Ellenőrizze, hogy az 5 ott van-e a szótár értékei között
if 5 in dict.values():
    print("True");print()
else:
    print("False");print()

# Task 5 - Delete the mark key from the dictionary and then everything from the dictionary
# Zadatak 5 - Obrisati ključ marka iz rečnika i posle sve iz rečnika
# Feladat 5 - Törölje a márka kulcsot a szótárból, majd mindent a szótárból
del dict["mark"]
print(dict)
dict.clear()
print(dict)