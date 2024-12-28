import csv

# CSV-Datei einlesen
def read_csv(file_path):
    drawn_numbers = []
    with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        #next(reader)  # Kopfzeile überspringen
        for row in reader:
            # Gewinnzahlen einlesen (angenommen, sie befinden sich in den ersten 6 Spalten)
            try:
                numbers = tuple(map(int, filter(None,row[2:51])))  # Lottozahlen in den ersten 6 Spalten
                drawn_numbers.append(numbers)
            except ValueError:
                continue  # Überspringe Zeilen mit ungültigen Werten
    return drawn_numbers

# Prüfen, ob die gegebene Kombination bereits gezogen wurde
def check_combination(drawn_numbers, combination):
    return combination in drawn_numbers

# Hauptfunktion
def main():
    # https://lotto-datenbank.de/lotto_misa.csv
    file_path = 'lotto_misa.csv'  # Pfad zur CSV-Datei
    drawn_numbers = read_csv(file_path)
    
    # Beispiel-Kombination, die überprüft werden soll
    combination_to_check = (1, 18, 20, 33, 34, 49)
    
    if check_combination(drawn_numbers, combination_to_check):
        print(f"Die Kombination {combination_to_check} wurde bereits gezogen.")
    else:
        print(f"Die Kombination {combination_to_check} wurde noch nicht gezogen.")

# Das Skript ausführen
main()