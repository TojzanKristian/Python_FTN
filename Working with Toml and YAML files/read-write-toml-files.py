import toml

def toml_write(filename, data):
    with open(filename, 'w') as f:
        toml.dump(data, f)

def toml_read(filename):
    with open(filename, 'r') as f:
        data = toml.load(f)
    return data

# Function testing - Testiranje funkcija - Függvények tesztelése
sample_list = [1, 2, 3, 4, 5]

# Writing to Toml file - Pisanje u Toml fajl - Toml-fájlba írás
toml_write('numbers.toml', {'my_list': sample_list})

# Reading from Toml file - Čitanje iz Toml fajla - Toml-fájl olvasása
loaded_data = toml_read('numbers.toml')
print(loaded_data['my_list'])
print();print()


# A more serious example with a list containing class objects as elements
# Malo ozbiljniji primer sa listom koja sadrži objekte klase kao elemente
# Komolyabb példa egy olyan listával, amely elemi osztály objektumok
class Student:
    def __init__(self, first_name, last_name, student_id, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.gpa = gpa


def write_students_to_toml(filename, students):
    student_data = [{'first_name': student.first_name,
                    'last_name': student.last_name,
                    'student_id': student.student_id,
                    'gpa': student.gpa} for student in students]

    data = {'students': student_data}

    with open(filename, 'w') as f:
        toml.dump(data, f)

def read_students_from_toml(filename):
    with open(filename, 'r') as f:
        data = toml.load(f)
    
    student_data = data.get('students', [])
    students = [Student(entry['first_name'], entry['last_name'], entry['student_id'], entry['gpa']) for entry in student_data]
    
    return students

# Function testing - Testiranje funkcija - Függvények tesztelése
students = [
    Student("John", "Doe", "PR100/2020", 8.5),
    Student("Jane", "Smith", "RA2/2021", 9.0),
    Student("Bob", "Johnson", "EE10/2019", 7.5),
]

# Writing to Toml file - Pisanje u Toml fajl - Toml-fájlba írás
write_students_to_toml('students.toml', students)

# Reading from Toml file - Čitanje iz Toml fajla - Toml-fájl olvasása
read_students = read_students_from_toml('students.toml')
for student in read_students:
    print(f"{student.first_name} {student.last_name}, ID: {student.student_id}, GPA: {student.gpa}")