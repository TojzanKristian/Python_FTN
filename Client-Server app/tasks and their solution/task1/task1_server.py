# Task 1 - The user enters 2 numbers, which are sent to the server, and the server returns their sum and product
# Zadatak 1 - Korisnik unosi 2 broja, koji se šalju serveru, a server vraća njihov zbir i proizvod
# Feladat 1 - A felhasználó megad 2 számot amit elküldünk a szerverre és a szerver vissza küldi az összegüket és szorzatukat
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 6000))
server.listen(1)
print("Server is listening for incoming connections...")

while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")

    n1 = client_socket.recv(1024).decode()
    n2 = client_socket.recv(1024).decode()

    if not n1 or not n2:
        client_socket.close()
        break

    n1 = float(n1)
    n2 = float(n2)
    sum_result = n1 + n2
    product_result = n1 * n2

    result = f"Sum: {sum_result}, Product: {product_result}"
    client_socket.send(result.encode())

    client_socket.close()

server.close()