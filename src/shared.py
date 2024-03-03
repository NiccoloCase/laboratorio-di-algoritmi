
def get_insertion_filename(name):
    """
    Restituisce il nome del file excel in cui salvare i risultati dell'inserimento.

    Parameters:
    - name (dict): Nome del test.
    """
    name = name.lower().replace(" ", "_")
    return name + "/insertion"

def get_insertion_iterations_filename(name):
    """
    Restituisce il nome del file excel in cui salvare la iterazioni dell'inserimento.

    Parameters:
    - name (dict): Nome del test.
    """
    name = name.lower().replace(" ", "_")
    return name + "/insertion_iterations"

def get_search_filename(name):
    """
    Restituisce il nome del file excel in cui salvare i risultati della ricerca.

    Parameters:
    - name (dict): Nome del test.
    """
    name = name.lower().replace(" ", "_")
    return name + "/search"