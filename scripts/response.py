import requests

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

# Beispielaufruf
csv_url = "https://lotto-datenbank.de/lotto_misa.csv"  # Ersetze dies mit deiner URL
local_filename = "lotto_misa.csv"

download_csv(csv_url, local_filename)
