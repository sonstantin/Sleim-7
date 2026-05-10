def uebersetze_buchstabe(buchstabe, sprache):
    # Wörterbuch für Buchstabenübersetzungen in der ersten Sprache
    buchstaben_uebersetzungen_sued = {
        'a': 'u',
        'b': 'g',
        'c': 'z',
        'd': 'p',
        'e': 'o',
        'f': 'm',
        'g': 'b',
        'h': 'h',
        'i': 'i',
        'j': 's',
        'k': 'x',
        'l': 'n',
        'm': 'c',
        'n': 'r',
        'o': 'e',
        'p': 'd',
        'q': 'q',
        'r': 'f',
        's': 'm',
        't': 'd',
        'u': 'a',
        'v': 'v',
        'w': 'v',
        'x': 'p',
        'y': 'i',
        'z': 'c',
        'ä': 'ue',
        'ö': 'oe',
        'ü': 'ae',
        'ß': 'ss',
        # ... (Ihre Übersetzungen für die erste Sprache hier)
    }
    
    # Wörterbuch für Buchstabenübersetzungen in der zweiten Sprache
    buchstaben_uebersetzungen_ost = {
        "a": "i",
        "b": "p",
        "c": "k",
        "d": "t",
        "e": "ä",
        "f": "v",
        "g": "q",
        "h": "h",
        "i": "y",
        "j": "i",
        "k": "c",
        "l": "w",
        "m": "n",
        "n": "m",
        "o": "u",
        "p": "b",
        "q": "g",
        "r": "x",
        "s": "ß",
        "t": "d",
        "u": "o",
        "v": "f",
        "w": "v",
        "x": "ks",
        "y": "ü",
        "z": "ts",
        "ä": "e",
        "ö": "ü",
        "ü": "ö",
        "ß": "skh",
        # ... (Ihre Übersetzungen für die zweite Sprache hier)
    }
    
    # Je nach ausgewählter Sprache das entsprechende Wörterbuch verwenden

    if sprache == "Südsleimisch" or sprache == "S":
        uebersetzungen = buchstaben_uebersetzungen_sued
    elif sprache == "Ostsleimisch" or sprache == "O":
        uebersetzungen = buchstaben_uebersetzungen_ost
    else:
        # Wenn die ausgewählte Sprache nicht erkannt wird, verwende die erste Sprache als Standard
        uebersetzungen = buchstaben_uebersetzungen_sued
    
    return uebersetzungen.get(buchstabe, buchstabe)

def uebersetze_wort(wort, sprache):
    wort = wort.lower()  # Konvertiere das Wort in Kleinbuchstaben, um Groß- und Kleinschreibung zu behandeln
    modifizierte_buchstaben = []
    
    in_klammern = False  # Eine Variable, um zu verfolgen, ob wir uns innerhalb von Klammern befinden
    inhalt_klammern = []  # Eine Liste, um den Inhalt der Klammern zu speichern
    
    for buchstabe in wort:
        if buchstabe == '(':
            in_klammern = True
        elif buchstabe == ')':
            in_klammern = False
            # Füge den Inhalt der Klammern zur Ausgabe hinzu
            modifizierte_buchstaben.extend(inhalt_klammern)
            # Lösche den Inhalt der Klammern
            inhalt_klammern = []
        elif in_klammern:
            inhalt_klammern.append(buchstabe)  # Füge den Buchstaben zum Inhalt der Klammern hinzu
        else:
            modifizierte_buchstaben.append(uebersetze_buchstabe(buchstabe, sprache))
    
    return ''.join(modifizierte_buchstaben)

# Abfrage, ob Anleitung ausgegeben werden soll
anleitung_anzeigen = input("Möchten Sie eine Anleitung sehen? (ja/nein): ")
if anleitung_anzeigen.lower() == "ja":
    print("Dies ist ein Übersetzungsprogramm, das Buchstaben in einem Wort oder Satz gemäß einer bestimmten Übersetzungstabelle ersetzt.")
    print("Klammern in Ihrem Eingabe bleiben unverändert, und der Inhalt von Klammern wird nicht übersetzt.")
    print("Geben Sie 'ja' ein, um den Vorgang erneut auszuführen, oder 'nein', um das Programm zu beenden.")
    print("Geben Sie Ihre Übersetzung ein und drücken Sie Enter:")

while True:
    # Abfrage der ausgewählten Sprache
    ausgewaehlte_sprache = input("Wählen Sie die Sprache aus ('Südsleimisch' oder 'Ostsleimisch'): ")
    
    eingabe = input("Hier kommt das zu übersetzende rein: ")
    uebersetzt = uebersetze_wort(eingabe, ausgewaehlte_sprache)
    
    # Entferne Klammern aus der Ausgabe
    uebersetzt = uebersetzt.replace('(', '').replace(')', '')
    
    print("Übersetzt:", uebersetzt)

    wiederholen = input("Möchtest du den Code erneut ausführen? (ja/nein): ")
    if wiederholen.lower() != "ja":
        ende = input("Wollst du das Pogramm wirklich beenden ???ja/nein ")
        if ende == "j" or ende == "ja":
            break  # Beendet die Schleife, wenn die Antwort nicht "ja" ist
