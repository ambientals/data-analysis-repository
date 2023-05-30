"""
Codice che effettua la verifica di un file CSV rispetto a determinati tipi di dati predefiniti da un tracciato, e avvisa all'utente se sono trovate delle anomalie in rispetto a questo.

Viene richiesto all'utente di selezionare un file CSV tramite una finestra di dialogo. Successivamente, il codice legge il file CSV e confronta i valori nelle colonne con i tipi di dati specificati.

In caso di anomalie, vengono stampati messaggi di avviso che indicano il tipo di anomalia e la posizione del valore nel file CSV.

Futuramente nella versione di uso le N colonne del csv verrano passate tramite un'altra finestra di dialogo, tale csv conterrà le colonne Campo, Datatype e Lunghezza.
"""

import csv
from datetime import datetime
from dateutil import parser
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_csv_file():
    root = tk.Tk()
    root.withdraw()
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    return csv_file_path                                            

def is_date(string, formats):
    for format in formats:
        try:
            datetime.strptime(string, format)
            return True
        except ValueError:
            pass
    return False

def contains_non_alphanumeric(string):
    return not string.isalnum() and not is_date(string, ["%Y-%m-%d %H:%M:%S"])

def check_data_length(row, types):
    min_length = 1
    max_length = 25
    for col_num, (value, data_type) in enumerate(zip(row, types), start=1):
        if not (min_length <= len(str(value)) <= max_length):
            print(f"Anomalia: La lunghezza del valore '{value}' nella colonna {col_num} non è corretta")

def check_data_type(value, data_type):
    if data_type == str:
        if value.isalnum():
            return True
        else:
            return False
    elif data_type == datetime:
        try:
            datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False
    else:
        try:
            if data_type == int:
                return value.isdigit()
            else:
                return isinstance(float(value), data_type)
        except (ValueError, TypeError):
            return False

def check_csv(column_types):
    csv_file_path = select_csv_file()
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Legge la riga di intestazione

        for row_idx, row in enumerate(reader, start=2):  # Parte dal 2 con l'indice di righe (L'intestazione è la riga 1)
            for col_idx, (field, column_type) in enumerate(zip(row, column_types), start=1):  # Parte da 1 con l'indice di colonne 
                column_name = header[col_idx - 1]
                if column_type == str:
                    if field.isdigit():
                        print(f"Anomalia: Number trovato in una colonna string '{column_name}', riga {row_idx}. Valore: '{field}'")
                    elif is_date(field, ["%Y-%m-%d %H:%M:%S"]):
                        print(f"Anomalia: Data trovata in una colonna string '{column_name}', riga {row_idx}. Valore: '{field}'")
                    elif contains_non_alphanumeric(field):
                        print(f"Anomalia nella colonna string '{column_name}', riga {row_idx}. Valore: '{field}'")
                elif column_type == datetime:
                    if not is_date(field, ["%Y-%m-%d %H:%M:%S"]):
                        print(f"Anomalia: Data in formato incorretto nella colonna '{column_name}', riga {row_idx}. Valore: '{field}'")
                elif column_type == int:
                    if not field.isdigit():
                        print(f"Anomalia: Integer con valore incorretto nella colonna '{column_name}', riga {row_idx}. Valore: '{field}'")
                check_data_length(row, column_types)

column_types = [str, datetime, str]  # Viene passato dall'utente dell'applicazione (la versione di uso avrà un prompt, e N colonne, passate da un csv con colonne Campo, Datatype e Lunghezza) 

check_csv(column_types)

input("Premere Invio per uscire")