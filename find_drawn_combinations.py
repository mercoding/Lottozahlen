import csv
import requests

# CSV-Datei von URL laden
def download_csv(url, filename):
    # Sende eine GET-Anfrage an die URL
    response = requests.get(url)

    # Prüfe, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # Speichere den Inhalt der CSV-Datei lokal
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"CSV-Datei erfolgreich heruntergeladen und als '{filename}' gespeichert.")
    else:
        print(f"Fehler beim Herunterladen der Datei. Statuscode: {response.status_code}")


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
    csv_url = "https://lotto-datenbank.de/lotto_misa.csv"  # Ersetze dies mit deiner URL
    local_filename = "./csv/lotto_misa.csv"
    download_csv(csv_url, local_filename)

    # read downloaded CSV file
    drawn_numbers = read_csv(local_filename)
    
    # Beispiel-Kombination, die überprüft werden soll
    combination_to_check = (7, 16, 24, 37, 46, 47) #(1, 18, 20, 33, 34, 49)
    
    if check_combination(drawn_numbers, combination_to_check):
        print(f"Die Kombination {combination_to_check} wurde bereits gezogen.")
    else:
        print(f"Die Kombination {combination_to_check} wurde noch nicht gezogen.")

# Das Skript ausführen
main()