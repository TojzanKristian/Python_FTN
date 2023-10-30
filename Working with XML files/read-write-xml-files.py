import xml.etree.ElementTree as ET

def write_to_xml(numbers, filename):
    root = ET.Element("numbers")
    for number in numbers:
        number_element = ET.SubElement(root, "number")
        number_element.text = str(number)
    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        xml_file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(xml_file)

def read_from_xml(filename):
    numbers = []
    tree = ET.parse(filename)
    root = tree.getroot()
    for number_element in root.findall("number"):
        number = int(number_element.text)
        numbers.append(number)
    return numbers

# Function testing - Testiranje funkcija - Függvények tesztelése
numbers = [1, 2, 3]

# Writing to an XML file - Pisanje u XML fajl - XML-fájlba írás
write_to_xml(numbers, "numbers.xml")

# Reading from an XML file - Čitanje iz XML fajla - XML-fájl olvasása
new_numbers = read_from_xml("numbers.xml")

for number in new_numbers:
    print(number)
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

    def to_xml(self):
        student_element = ET.Element("student")
        ET.SubElement(student_element, "firstName").text = self.firstName
        ET.SubElement(student_element, "secondName").text = self.secondName
        ET.SubElement(student_element, "indexNumber").text = self.indexNumber
        ET.SubElement(student_element, "average").text = str(self.average)
        return student_element

    @classmethod
    def from_xml(cls, student_element):
        fname = student_element.find("firstName").text
        sname = student_element.find("secondName").text
        index = student_element.find("indexNumber").text
        avg = float(student_element.find("average").text)
        return cls(fname, sname, index, avg)


def write_to_xml_student(student_list, filename):
    root = ET.Element("students")
    for student in student_list:
        root.append(student.to_xml())
    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        xml_file.write(b'<?xml version="1.0"?>\n')
        tree.write(xml_file)

def read_from_xml_student(filename):
    student_list = []
    tree = ET.parse(filename)
    root = tree.getroot()
    for student_element in root.findall("student"):
        student = Student.from_xml(student_element)
        student_list.append(student)
    return student_list

# Function testing - Testiranje funkcija - Függvények tesztelése
students = [
    Student("John", "Doe", "PR100/2020", 8.5),
    Student("Jane", "Smith", "RA2/2021", 9.0),
    Student("Bob", "Johnson", "EE10/2019", 7.5),
]

# Writing to an XML file - Pisanje u XML fajl - XML-fájlba írás
write_to_xml_student(students, "students.xml")

# Reading from an XML file - Čitanje iz XML fajla - XML-fájl olvasása
new_students = read_from_xml_student("students.xml")

for student in new_students:
    print(student)