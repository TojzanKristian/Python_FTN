# Function to write to txt file - Funkcija za upis u txt fajl - Függvény a txt fájlba írásra
def write_to_file(fileName, text):
    try:
        with open(fileName, 'w') as file:
            file.write(text)
        print(f'Successfully written to {fileName}.\n')
    except IOError:
        print(f'An error occurred writing the file {fileName}.\n')

# Function to read txt file - Funkcija za čitanje iz txt fajla - Függvény a txt fájl olvasására
def read_from_file(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            return content
    except IOError:
        print(f'An error occurred reading {fileName}.\n')
        return None

# Test functions - Testiranje funkcija - Függvények tesztelése
fileName = 'test.txt'
text = input("Please enter some text you want to enter into the txt file : ")
write_to_file(fileName, text)
print()
textToPrint = read_from_file(fileName)
if textToPrint is not None:
    print(f'The {fileName} file contains:\n{textToPrint}')
print();print()

# Some good tips - Nekoliko dobrih saveta - Néhány jó tipp
# open(fileName, 'w', encoding='utf-8') -> set encoding - podešavanje kodiranja - kódolás beállítása
# In addition to file.read(), there is also file.readline() - Pored file.read() tu je i file.readline() - A file.read() mellett létezik file.readline() is
# In addition to file.readline(), there is also file.readlines() - Pored file.readline() tu je i file.readlines() - A file.readline() mellett létezik file.readlines() is
# If you don't use "with", remember to close the txt file -> file.close()
# Ako ne koristite "with", ne zaboravite da zatvorite txt datoteku -> file.close()
# Ha nem használod a "with" kúlcsszót nem felejtsd el bezárni a txt fájlt -> file.close()


# Examples - Primeri - Példák
# 1) The user should enter 2 numbers, their sum, multiplication, difference and quotient must be written in a txt file
# 1) Korisnik treba da unese 2 broja, njihov zbir, proizvod, razlika i količnik moraju biti upisani u txt datoteku
# 1) A felhasználó vigyen be 2 számot ezek összegét, szorzatát, különbségét és hányadosát txt fájlbe kell írni
n1 = input("Please enter the first number : ")
n2 = input("Please enter the second number : ")

s = int(n1)+int(n2)
m = int(n1)*int(n2)
d = int(n1)-int(n2)
q = int(n1)/int(n2)

result_string = f"Sum = {s}, Product = {m}, Difference = {d}, Quotient = {q}"
ex1fileName = 'example1.txt';print()
write_to_file(ex1fileName, result_string)
print()


# 2) Enter a list of students objects in the txt file
# 2) Upis liste studenata u txt fajl
# 2) Tanuló objektumokból álló lista beírása a txt fájlba
class Student:
    def __init__(self, fname, sname, numberOfIndex, average):
        self.firstName = fname
        self.secondName = sname
        self.indexNumber = numberOfIndex
        self.average = average

    def __str__(self) -> str:
        return f"{self.indexNumber} {self.secondName} {self.firstName}, {self.average}"

def list_to_string(student_list):
    result = ""
    for student in student_list:
        result += str(student) + "\n"
    return result

students = [
    Student("John", "Doe", "PR100/2020", 8.5),
    Student("Jane", "Smith", "RA2/2021", 9.0),
    Student("Bob", "Johnson", "EE10/2019", 7.5),
]

students_str = list_to_string(students)

ex2fileName = 'example2.txt'
write_to_file(ex2fileName, students_str)