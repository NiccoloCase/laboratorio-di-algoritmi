import pandas as pd
import os
from shared import get_insertion_filename, get_insertion_iterations_filename, get_search_filename

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
    limitato di righe significative. Genera un file con estensione .cvs per imporarlo in latex

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
def format(numberString, significant_digits=6):
    myNumber = numberString
    # Controlla che il numero sia un numero  
    if not isinstance(numberString, (int, float)):
        # Se non è un numero, prova a convertirlo
        try:
            myNumber = float(numberString)
        except:
            return numberString

    stringNumber = "{:." + str(significant_digits) + "e}"
    return stringNumber.format(myNumber)



def create_joined_file():
    """
    Funzione che genera per i tre tipi di alberi binari di ricerca, un file excel con i risultati combinati di ricerca e inserimento
    """

    for tree in ["BST", "BST_FLAG", "BST_LIST"]:
        bst_insertion = load_results(get_insertion_filename(tree))
        bst_insertion_iterations = load_results(get_insertion_iterations_filename(tree))
        bst_search = load_results(get_search_filename(tree))

        # Se gli array non sono dela stessa lunghezza, aggiungi valori nulli
        max_length = max(len(bst_insertion), len(bst_insertion_iterations), len(bst_search))
        for results in [bst_insertion, bst_insertion_iterations, bst_search]:
            if results != None:
                while len(results) < max_length:
                    results[max(results.keys()) + 1] = None

        # Formatta i valori in notazione scientifica
        for results in [bst_insertion, bst_search]:
            if results != None:
                for key in results:
                    results[key] = format(results[key],2)
        
        # Salva i risultati in un file excel
        payload = {
            'n': list(bst_insertion.keys()),
            f'Inserimento {tree}': list(bst_insertion.values()),
            f'Iterazioni inserimento {tree}': list(bst_insertion_iterations.values()),
            f'Ricerca {tree}': list(bst_search.values())
        }

        df = pd.DataFrame(payload)
        df.to_excel(f"./outputs/risultati_{tree}.xlsx", index=False)