import socket

# 1. Step - 1. Korak - 1. Lépés :
# Creating socket - Kreiranje soketa - Socket létrehozása
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Step - 2. Korak - 2. Lépés :
# Address Configuration - Konfiguracija adrese - Címkonfiguráció
server.bind(('localhost', 6000))

# 3. Step - 3. Korak - 3. Lépés :
# Creating a "listening" socket - Kreiranje "slušajućeg" soketa - "Hallgató" socket létrehozása
server.listen()
print("The server has been successfully started !!!")

# 4. Step - 4. Korak - 4. Lépés :
# Acceptance of the connection by the client - Prihvatanje konekcije od strane klijenta - A klijensel való kapcsolat fogadása
channel, address = server.accept()
print(f"The connection from the following address is accepted: {address}")

# 5. Step - 5. Korak - 5. Lépés :
# Data acceptance and processing - Prihvatanje podataka i obrada - Adatok fogadása és feldolgozása
while True:
    message = channel.recv(1024).decode()
    if not message : break
    print(f"Received message: {message}")

print("The server is shutting down !!!")

# 6. Step - 6. Korak - 6. Lépés :
# The closure of the communication channel - Zatvaranje komunikacionog kanala - A kommunikációs csatorna bezárása
server.close()