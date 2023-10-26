# Task 2 - The client specifies an index number to which the server sends it the corresponding student data
# Zadatak 2 - Klijent navodi broj indeksa, za koji mu server šalje odgovarajuće podatke za tog studenta
# Feladat 2 - A kliens megad egy index számot amire a szerver elküldi neki az ahhoz tartozó diák adatait
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6000))
print("A connection to the server has been established !!")

while True: 
    nOfIndexes = input("Enter the index number of the student whose data you want, in format -> PR1/2020 : ")
    if not nOfIndexes : break 
    client.send(nOfIndexes.encode()) 
    student = client.recv(1024).decode()
    print(f"Information about the requested student -> {student}")

print("The connection is closing !!")
client.close()