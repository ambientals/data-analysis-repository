"""
-- (Ultimo sviluppo nel 15/06/2023) 
CODICE INCOMPLETO PER I DATASET CON COLONNE RIPETUTE + LUNGHEZZA FISSA, ED ESCLUSIVAMENTE NUMERI AL POSTO DI ALFANUMERICI (PER TUTTE LE COLONNE, INCLUSA LA PRIMA)
NELL'ULTIMA VERSIONE IN SVILUPPO TALI PROBLEMI SONO GIà IN ANALISI.
SI APPLICA PURE LA LOGICA PER IL CONTROLLO DEI CAMPI DI LUNGHEZZA FISSA.
CONDIVISIONE FATTA NON APPENA VENGONO IMPLEMENTATE TUTTE LE LOGICHE IN PIENO FUNZIONAMENTO.
"""

import csv
from datetime import datetime
from dateutil import parser
import tkinter as tk
from tkinter import filedialog

def select_csv_file(title):
    """
    Chiamata da run_data_quality_analysis(), apre una finestra di dialogo per la selezione di un file CSV utilizzando la libreria tkinter, consentendo all'utente di scegliere un file.
    Prende in input un titolo per la finestra di dialogo del file e restituisce il percorso del file CSV selezionato.
    """
    root = tk.Tk()
    root.withdraw()
    csv_file_path = filedialog.askopenfilename(filetypes=[("File CSV", "*.csv")], title=title)
    return csv_file_path

def is_valid_date(date_string, date_format):
    """
    Verifica se una stringa di data specificata è valida secondo un formato di data specificato.
    Utilizza la funzione datetime.strptime per analizzare la stringa di data in base al formato fornito.
    Se l'analisi ha successo, restituisce True; in caso contrario, restituisce False.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def has_non_alphanumeric_chars(value):
    """
    Questa funzione verifica se una stringa specificata contiene caratteri non alfanumerici.
    Confronta ogni carattere nella stringa con un insieme di caratteri consentiti (lettere, numeri, punto, slash, trattino, underscore, parentesi e parentesi quadre).
    Se viene trovato un carattere che non è nell'insieme consentito e non è uno spazio, restituisce True; in caso contrario, restituisce False.
    """
    allowed_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789./-_()[]'
    return any(char not in allowed_characters and not char.isspace() for char in value)

def is_decimal(value, decimal_length):
    """
    Questa funzione verifica se una stringa specificata rappresenta un numero decimale valido. Cerca di convertire la stringa in un float e verifica se il valore convertito ha una parte decimale. Se il valore è un decimale valido e la lunghezza della parte decimale corrisponde alla lunghezza decimale specificata, restituisce True; in caso contrario, restituisce False.
    """
    try:
        float_value = float(value)
        if float_value != int(float_value):
            decimal_part = str(float_value).split('.')[-1]
            if len(decimal_part) != decimal_length:
                return False
        return True
    except ValueError:
        return False

def check_data_anomalies(row, column_rules, header_row, row_idx):
    """
    La funzione viene chiamata da check_csv() per esaminare ogni valore in una riga di dati per anomalie basandosi su un insieme di regole di colonna. 
    Itera sui valori nella riga e li confronta con le regole corrispondenti per ciascuna colonna. 
    Rileva anomalie come superamento della lunghezza massima, presenza di caratteri non alfanumerici in colonne di stringhe, valori di data/ora non validi e valori decimali non validi. 
    Stampa le anomalie rilevate e restituisce True se vengono trovate anomalie; in caso contrario, restituisce False.
    """
    anomalies_found = False

    for i, value in enumerate(row):
        column_rule = column_rules[i]
        expected_datatype = column_rule['datatype']
        expected_length = column_rule['length']
        decimal_length = column_rule.get('formatto_decimale', 0)
        date_format = column_rule['format']

        if len(value) > expected_length:
            print(f"Anomalia: Superata la lunghezza massima nella colonna '{header_row[i]}', riga {row_idx}. Valore: '{value}'")
            anomalies_found = True

        if expected_datatype == "str":
            if not value.isdigit() and has_non_alphanumeric_chars(value):
                print(f"Anomalia: Trovati caratteri non alfanumerici nella colonna di stringa '{header_row[i]}', riga {row_idx}. Valore: '{value}'")
                anomalies_found = True

        elif expected_datatype == "datetime":
            if not is_valid_date(value, date_format):
                print(f"Anomalia: Valore datetime non valido nella colonna '{header_row[i]}', riga {row_idx}. Valore: '{value}'")
                anomalies_found = True

        elif expected_datatype == "float":
            if not is_decimal(value, decimal_length):
                print(f"Anomalia: Trovato un valore decimale non valido nella colonna float '{header_row[i]}', riga {row_idx}. Valore: '{value}'")
                anomalies_found = True
            elif len(value) > expected_length:
                print(f"Anomalia: Superata la lunghezza massima nella colonna float '{header_row[i]}', riga {row_idx}. Valore: '{value}'")
                anomalies_found = True

    return anomalies_found

def check_csv(file_path, column_rules):
    """
    Funzione viene chiamata da run_data_quality_analysis() per eseguire l'analisi della qualità dei dati sul file di dati selezionato. 
    Apre il file specificato da file_path, legge i dati utilizzando csv.reader e confronta i nomi delle colonne nel file con le regole delle colonne specificate, quindi chiamando la funzione check_data_anomalies per ciascuna riga di dati per controllare le anomalie, questa, stampa dei messagi esplicitando caso siano ci trovate delle anomalie o meno.
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Legge la riga di intestazione

        print("--Analisi NOMI:")

        # Ottiene i nomi delle colonne dal file 'Data'
        data_column_names = header

        # Ottiene i nomi delle regole dal file 'Rules'
        rule_names = [rule['name'] for rule in column_rules]

        # Verifica se i nomi delle colonne 'Data' corrispondono ai nomi delle regole 'Rules'
        data_not_in_rules = set(data_column_names) - set(rule_names)
        rules_not_in_data = set(rule_names) - set(data_column_names)

        if data_not_in_rules:
            print("Anomalia: Le seguenti colonne nel file dei DATI non corrispondono a nessun nome di colonna nel file delle REGOLE (tracciato):\n")
            print(f"{data_not_in_rules}")

        if rules_not_in_data:
            print("Anomalia: I seguenti nomi di colonna nel file delle REGOLE (tracciato) non corrispondono a nessuna colonna nel file dei DATI':\n")
            print(f"{rules_not_in_data}")

        if not data_not_in_rules and not rules_not_in_data:
            print("Tutte le colonne nel file dei DATI hanno i nomi di colonna corrispondenti nel file delle REGOLE, e viceversa.")

        print("\n--Analisi DATI - anomalie:")

        anomalies_found = False

        for row_idx, row in enumerate(reader, start=2):
            anomalies_found = check_data_anomalies(row, column_rules, header, row_idx) or anomalies_found

        if not anomalies_found:
            print("Nessuna anomalia trovata nel file.")

        input("\n--Analisi DATA QUALITY completata. Premere qualsiasi tasto per uscire.")

def load_rules(rules_file_path, default_datetime_format="%Y-%m-%d %H:%M:%S"):
    """
    Funzione chiamata da run_data_quality_analysis() per caricare le regole di colonna dal file di regole specificato. 
    Legge il file delle regole specificato da rules_file_path utilizzando csv.reader e costruisce una lista di dizionari che rappresentano le regole di colonna.    
    Ogni dizionario contiene il nome della colonna, il tipo di dati, la lunghezza, il formato data (se applicabile), il flag fissa_flag e i valori formatto_decimale. 
    La funzione gestisce anche valori opzionali e fornisce valori predefiniti per i valori mancanti. 
    Alla fine restituisce la lista di regole di colonna.
    """
    column_rules = []
    with open(rules_file_path, 'r') as rules_file:
        rules_reader = csv.reader(rules_file)
        next(rules_reader)  # Salta la riga di intestazione
        for row in rules_reader:
            column_name = row[0]
            datatype = row[1]
            length = int(row[2])
            date_format = row[3] if len(row) > 3 and row[3] != '' else default_datetime_format
            fissa_flag = row[4] if len(row) > 4 else ""  # Ottiene il valore della colonna 'Fissa_flag'
            formatto_decimale = int(row[5]) if len(row) > 5 and row[5] != '' else 0  # Ottiene il valore della colonna 'formatto_decimale'

            if datatype == 'datetime' and not date_format:
                print(f"Attenzione: Nessun formato datetime specificato per la colonna '{column_name}'. Utilizzo del formato predefinito '{default_datetime_format}'.")

            column_rules.append({
                'name': column_name,
                'datatype': datatype,
                'length': length,
                'format': date_format,
                'fissa_flag': fissa_flag,
                'formatto_decimale': formatto_decimale
            })

    return column_rules

def run_data_quality_analysis():
    """
    Funzione principale che avvia l'analisi della qualità dei dati. 
    Chiede all'utente di selezionare un file CSV e un file di regole. 
    Carica le regole di colonna dal file di regole e esegue l'analisi della qualità dei dati sul file CSV selezionato.
    """
    print("--REPORT DI ANALISI PER LA DATA QUALITY:\n")

    rules_file_path = select_csv_file("Selezionare il file delle REGOLE (tracciato)")
    column_rules = load_rules(rules_file_path)

    print("--Struttura del TRACCIATO:")
    print("NOMI delle colonne:", [rule['name'] for rule in column_rules])
    print("DATATYPE delle colonne:", [rule['datatype'] for rule in column_rules])
    print("LUNGHEZZA delle colonne:", [rule['length'] for rule in column_rules])
    print()

    data_file_path = select_csv_file("Selezionare il file con i DATI di analisi")
    check_csv(data_file_path, column_rules)

run_data_quality_analysis()