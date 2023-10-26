import socket

# 1. Step - 1. Korak - 1. Lépés :
# Creating socket - Kreiranje soketa - Socket létrehozása
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Step - 2. Korak - 2. Lépés :
# Establishing a connection to the server - Uspostava konekcije sa serverom - Kapcsolat létrehozása a szerverrel
client.connect(('localhost', 6000))
print("A connection to the server has been established !!!")

# 3. Step - 3. Korak - 3. Lépés :
# Entering and sending data - Unos i slanje podataka - Adatok bevitele és küldése
while True: 
    poruka = input("Please enter a message : ")
    if not poruka : break
    client.send(poruka.encode())

print("The connection closes !!!")

# 4. Step - 4. Korak - 4. Lépés :
client.close()