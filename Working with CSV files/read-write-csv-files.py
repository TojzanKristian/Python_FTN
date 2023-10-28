import csv

def read_the_CSV(fileName):
    data = []
    with open(fileName, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for line in csv_reader:
            x = int(line['x'])
            y = float(line['y'])
            red = int(line['red'])
            blue = int(line['blue'])
            green = int(line['green'])
            data.append((x, y, red, blue, green))
    return data

def write_to_CSV(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['x/y', 'red', 'blue', 'green'])
        for line in data:
            csv_writer.writerow(line)

def calculate_x_over_y(data):
    for i in range(len(data)):
        x, y, red, blue, green = data[i]
        x_over_y = x / y
        data[i] = (x_over_y, red, blue, green)
    return data

fileName = 'colors.csv'
output_fileName = 'colorsAfterCalculate.csv'

# Read data from CSV - Čitanje podataka iz CSV fajla - Adatok olvasása a CSV fájlból
data = read_the_CSV(fileName)

# Print data - Ispis pročitanih podataka - A kiolvasott adatok kiírása
print("Print data :")
for line in data:
    print(line)

# Calculate x/y - Računanje x/y - Kiszámítjuk az x/y
newData = calculate_x_over_y(data)

# Print data after calculate - Ispis podataka nakun izračunavanja - Adatok kiírása a számítások után
print(); print("Print data after calculate x/y :")
for line in newData:
    print(line)

# Write data to CSV - Upis podataka u CSV fajl - Adatok beírása a CSV fájlba
write_to_CSV(newData, output_fileName)