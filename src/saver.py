import pandas as pd
import math
import os

def save_results(results, filename): 
    """
    Salva i risultati dei test in un file Excel.

    Parameters:
    - results (dict):Dizionario contenente i risultati dei test.
    - filename (str): Il nome del file Excel senza estensione.

    Returns: None
    """

    print(f"Salvo i risultati in '{filename}.xlsx'...")

    # Formatta i risultati dei test
    n = list(results.keys())
    time = list(results.values())

    # Salva i risultati in un file excel
    payload = {
        'n': n,
        'time': time
    }
    df = pd.DataFrame(payload) 

    src = "./outputs/" + filename + '.xlsx'



    fileDirectory = os.path.dirname(src)

    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)

    df.to_excel(src, index=False)

    # Genera una copia riassunta del file
    summarise_file(src)



def load_results(filename): 
    """
    Legge i risultati dei test da un file Excel.

    Parameters:
    - filename (str): Il nome del file Excel senza estensione.
    
    Returns: Il dizionario contenente i risultati dei test.
    """
    
    fileSrc = "./outputs/" + filename + '.xlsx'

    try:
        df = pd.read_excel(fileSrc)
    except FileNotFoundError:
        print(f"File '{filename}.xlsx' non trovato.")
        return None

    # Converte i risultati in un dizionario
    results = df.to_dict()

    # Formatta i risultati
    n = results['n']
    time = results['time']
    results = {n[i]: time[i] for i in range(len(n))}

    return results


def summarise_file(fileSource):
    """
    Funzione che dato il percorso di un file excel, genera una copia con solo un numero
    limitato di righe significative.


    Parameters:
    - fileSource (str): Percorso del file excel da riassumere.
    """

    print(f"Riassumo il file '{fileSource}'...")

    # Carica il file
    try:
        df = pd.read_excel(fileSource)
    except:
        print("Errore nel caricamento del file.")
        return
    
    # Riassumi il file
    MAX_ROWS = 15

    # Se il file è già riassunto, non fare nulla
    if len(df) <= MAX_ROWS:
        return
    
    # Riassumi il file prendendo solo le righe significative
    rows = [0, len(df) - 1] # L'ultima e la prima riga devono essere sempre presenti
    step = (len(df) - 2) // (MAX_ROWS - 2)
    for i in range(1, MAX_ROWS - 1):
        rows.append(i * step)
    rows.sort()
    df = df.iloc[rows] # Aggiorna il dataframe


    # Creazione di un nuovo DataFrame con solo due colonne
    df_summarised = df[['n', 'time']]


    # Formatta i valori
    for column in df.columns:
        if df[column].dtype == "float64":
            df_summarised[column] = df_summarised[column].apply(lambda x: format(x, 2))
  

    # Cambia il nome delle colonne
    df_summarised.columns =["Numero di elementi", "Tempo di esecuzione (s)"]


    # Salva il file
    newFileSource = fileSource.replace(".xlsx", "_summarised.cvs")
    print(f"Salvo il file riassunto in '{newFileSource}'...")
    df_summarised.to_csv(newFileSource, index=False)




# Converte il numero in notazione scientifica con il numero di cifre significative specificato
def format(numero, significant_digits=6):
    formato_stringa = "{:." + str(significant_digits) + "e}"
    numero_in_notazione_scientifica = formato_stringa.format(numero)
    return numero_in_notazione_scientifica



