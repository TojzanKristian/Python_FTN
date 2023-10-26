# Task 1 - The user enters 2 numbers, which are sent to the server, and the server returns their sum and product
# Zadatak 1 - Korisnik unosi 2 broja, koji se šalju serveru, a server vraća njihov zbir i proizvod
# Feladat 1 - A felhasználó megad 2 számot amit elküldünk a szerverre és a szerver vissza küldi az összegüket és szorzatukat
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 6000))
print("A connection to the server has been established !!!")

while True: 
    n1 = input("Please enter first number : ")
    n2 = input("Please enter second number : ")
    if not n1 and n2 : break
    client.send(n1.encode())
    client.send(n2.encode())
    result = client.recv(1024).decode()
    print(f"The server returned : {result}")

print("The connection closes !!!")
client.close()