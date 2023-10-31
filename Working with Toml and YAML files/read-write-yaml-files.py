import yaml

def write_yaml(fileName, sample_list):
    with open(fileName, "w") as file:
        yaml.dump(sample_list, file)

def read_yaml(fileName):
    with open(fileName, "r") as file:
        loaded_data = yaml.load(file, Loader=yaml.FullLoader)
    return loaded_data

# Function testing - Testiranje funkcija - Függvények tesztelése
sample_list = [1, 2, 3, 4, 5]

# Writing to YAML file - Pisanje u YAML fajl - YAML-fájlba írás
write_yaml("numbers.yaml", sample_list)

# Reading from YAML file - Čitanje iz YAML fajla - YAML-fájl olvasása
data = read_yaml("numbers.yaml")
print(data)
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


def write_students_to_yaml(fileName, students):
    student_data = []
    for student in students:
        student_data.append({
            "first_name": student.first_name,
            "last_name": student.last_name,
            "student_id": student.student_id,
            "gpa": student.gpa
        })

    with open(fileName, "w") as file:
        yaml.dump(student_data, file)

def read_students_from_yaml(fileName):
    students = []
    with open(fileName, "r") as file:
        student_data = yaml.load(file, Loader=yaml.FullLoader)
        for data in student_data:
            student = Student(data["first_name"], data["last_name"], data["student_id"], data["gpa"])
            students.append(student)
    return students

# Function testing - Testiranje funkcija - Függvények tesztelése
students = [
    Student("John", "Doe", "PR100/2020", 8.5),
    Student("Jane", "Smith", "RA2/2021", 9.0),
    Student("Bob", "Johnson", "EE10/2019", 7.5),
]

# Writing to YAML file - Pisanje u YAML fajl - YAML-fájlba írás
write_students_to_yaml("students.yaml", students)

# Reading from YAML file - Čitanje iz YAML fajla - YAML-fájl olvasása
loaded_students = read_students_from_yaml("students.yaml")
for student in loaded_students:
    print(f"{student.first_name} {student.last_name} ({student.student_id}): GPA = {student.gpa}")