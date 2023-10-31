import json

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

# Function testing - Testiranje funkcija - Függvények tesztelése
sample_list = [1, 2, 3, 4, 5]

# Writing to JSON file - Pisanje u JSON fajl - JSON-fájlba írás
write_json('sample.json', sample_list)

# Reading from JSON file - Čitanje iz JSON fajla - JSON-fájl olvasása
loaded_data = read_json('sample.json')
print(loaded_data)
print();print()


# A more serious example with a list containing class objects as elements
# Malo ozbiljniji primer sa listom koja sadrži objekte klase kao elemente
# Komolyabb példa egy olyan listával, amely elemi osztály objektumok
class Student:
    def __init__(self, fname, sname, numberOfIndex, average):
        self.firstName = fname
        self.secondName = sname
        self.indexNumber = numberOfIndex
        self.average = average

    def __str__(self):
        return f"{self.indexNumber} {self.secondName} {self.firstName}, {self.average}"


def write_json(filename, data):
    with open(filename, 'w') as file:
        student_data = [{'firstName': student.firstName, 'secondName': student.secondName, 'indexNumber': student.indexNumber, 'average': student.average} for student in data]
        json.dump(student_data, file, default=lambda student: student.__dict__)

def read_json(filename):
    with open(filename, 'r') as file:
        student_data = json.load(file)
        students = [Student(student['firstName'], student['secondName'], student['indexNumber'], student['average']) for student in student_data]
        return students

# Function testing - Testiranje funkcija - Függvények tesztelése
students = [
    Student("John", "Doe", "PR100/2020", 8.5),
    Student("Jane", "Smith", "RA2/2021", 9.0),
    Student("Bob", "Johnson", "EE10/2019", 7.5),
]

# Writing to JSON file - Pisanje u JSON fajl - JSON-fájlba írás
write_json('students.json', students)

# Reading from JSON file - Čitanje iz JSON fajla - JSON-fájl olvasása
loaded_students = read_json('students.json')
for student in loaded_students:
    print(student)