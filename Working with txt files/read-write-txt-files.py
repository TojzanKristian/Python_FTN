# Function to write to txt file - Funkcija za upis u txt fajl - Függvény a txt fájlba írásra
def write_to_file(fileName, text):
    try:
        with open(fileName, 'w') as file:
            file.write(text)
        print(f'Successfully written to {fileName}.')
    except IOError:
        print(f'An error occurred writing the file {fileName}.')

# Function to read txt file - Funkcija za čitanje iz txt fajla - Függvény a txt fájl olvasására
def read_from_file(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            return content
    except IOError:
        print(f'An error occurred reading {fileName}.')
        return None

# Test functions - Testiranje funkcija - Függvények tesztelése
fileName = 'test.txt'
text = input("Please enter some text you want to enter into the txt file : ")
write_to_file(fileName, text)
print()
textToPrint = read_from_file(fileName)
if textToPrint is not None:
    print(f'The {fileName} file contains:\n{textToPrint}')


# Some good tips - Nekoliko dobrih saveta - Néhány jó tipp
# open(fileName, 'w', encoding='utf-8') -> set encoding - podešavanje kodiranja - kódolás beállítása
# In addition to file.read(), there is also file.readline() - Pored file.read() tu je i file.readline() - A file.read() mellett létezik file.readline() is
# In addition to file.readline(), there is also file.readlines() - Pored file.readline() tu je i file.readlines() - A file.readline() mellett létezik file.readlines() is
# If you don't use "with", remember to close the txt file -> file.close()
# Ako ne koristite "with", ne zaboravite da zatvorite txt datoteku -> file.close()
# Ha nem használod a "with" kúlcsszót nem felejtsd el bezárni a txt fájlt -> file.close()