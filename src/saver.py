import pandas as pd
import math

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
    
    src = "./outputs/" + filename + '.xlsx'
    try:
        df = pd.read_excel(src)
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

    # Formatta i valori prendendo solo le prime 2 cifre significative
    for column in df.columns:
        if df[column].dtype == "float64":
            df[column] = df[column].apply(lambda x: truncate_number(x, 3))
  

    # Salva il file
    newFileSource = fileSource.replace(".xlsx", "_summarised.xlsx")
    print(f"Salvo il file riassunto in '{newFileSource}'...")
    df.to_excel(newFileSource, index=False)





def truncate_number(number, significant_digits):
    if number == 0: return 0
    # Log10 del numero
    log10_number = abs(number) and math.log10(abs(number))
    # Calcola la potenza di 10
    power_of_10 = significant_digits - 1 - int(log10_number)
    # Tronca il numero
    truncated_number = round(number * 10 ** power_of_10) / (10 ** power_of_10)
    return truncated_number