import socket

# 1. Step - 1. Korak - 1. Lépés :
# Creating socket - Kreiranje soketa - Socket létrehozása
klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Step - 2. Korak - 2. Lépés :
# Establishing a connection to the server - Uspostava konekcije sa serverom - Kapcsolat létrehozása a szerverrel
klijent.connect(('localhost', 6000))
print("A connection to the server has been established !!!")

# 2. Step - 2. Korak - 2. Lépés :
# Entering and sending data - Unos i slanje podataka - Adatok bevitele és küldése
while True: 
    poruka = input("Please enter a message : ")
    if not poruka : break
    klijent.send(poruka.encode())

print("The connection closes !!!")

# 3. Step - 3. Korak - 3. Lépés :
klijent.close() # Zatvaranje komunikacionog kanala sa klijentske strane