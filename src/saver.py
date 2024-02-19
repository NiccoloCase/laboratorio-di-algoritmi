import pandas as pd

def save_results(results, filename): 
    """
    Salva i risultati dei test in un file Excel.

    Parameters:
    - results (dict):Dizionario contenente i risultati dei test.
    - filename (str): Il nome del file Excel senza estensione.

    Returns: None
    """

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
