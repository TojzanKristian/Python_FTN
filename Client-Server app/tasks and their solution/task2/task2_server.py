# Task 2 - The client specifies an index number to which the server sends it the corresponding student data
# Zadatak 2 - Klijent navodi broj indeksa, za koji mu server šalje odgovarajuće podatke za tog studenta
# Feladat 2 - A kliens megad egy index számot amire a szerver elküldi neki az ahhoz tartozó diák adatait
import socket
from student import Student

studenti = {}
studenti["PR1/2020"] = Student("Petar", "Petrović", "PR1/2020", 10.0)
studenti["PR2/2020"] = Student("Marko", "Marković", "PR2/2020", 9.0)
studenti["PR3/2020"] = Student("Jovan", "Jovanović", "PR3/2020", 8.0)
studenti["PR4/2020"] = Student("Milan", "Milanović", "PR4/2020", 7.0)
studenti["PR5/2020"] = Student("Mirko", "Mirković", "PR5/2020", 6.0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6000))
server.listen()
print("The server is running !!")

channel, address = server.accept()
print(f"The connection from the following address is accepted: {address}")

while True:
    nOfIndex = channel.recv(1024).decode()
    if not nOfIndex:
        break
    print(f"Looking for a student with an index number: {nOfIndex}")

    if nOfIndex in studenti:
        student = studenti[nOfIndex].__str__()
    else:
        student = "Student not found"
    
    print(f"Student: {student}")
    channel.send(student.encode())

print("The server's shutting down !!")
server.close()