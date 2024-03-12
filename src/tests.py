from timeit import default_timer as timer
import matplotlib.pyplot as plt
from saver import save_results, load_results
from progressbar import ProgressBar
from shared import get_insertion_filename, get_insertion_iterations_filename, get_search_filename

def run_tree_test(TreeClass, name, insertionN=10000, searchN=10000):
    """
    Esegue i test su una classe di albero.

    Parameters:
    - TreeClass (class): Classe dell'albero su cui eseguire i test.
    - name (str): Nome dell'albero.
    """
        

    # -----------------------------------------------------------
    # CONFIGURAZIONE TEST
    key = 1 # Chiave da inserire
    insertion_n = insertionN # Numero di chiavi da inserire
    search_n = searchN # Numero di chiavi da cercare
    maxRecords = 100000 # Massimo numero di records da salvare
    # ----------------------------------------------------------

    tree = TreeClass()
    insert_result = {}
    insert_iterations_result = {}
    search_result = {}

    # Evita di salvare troppi risultati
    step_insertion =  1 if insertion_n <= maxRecords else  insertion_n // maxRecords # Calcola il passo con cui salvare i risultati
    savedCountInsertion = 0   # Tiene traccia del passo corrente

    step_search =  1 if search_n <= maxRecords else  search_n // maxRecords 
    savedCountSearch = 0


    N = max(insertion_n, search_n)+1

    
    # Print
    print("INIZIO TEST SU " + name.upper() + " (N=" + str(N) + ")")
    
    # Barra di progresso
    # progress_bar = ProgressBar(N)

    testStart = timer()

    for i in range(N):


        # Testa l'inserimento
        if i < insertion_n:
            insert_start = timer()
            insert_iterations = tree.insert(key)
            insert_end = timer()

        # Testa la ricerca
        if i < search_n:
            search_start = timer()
            tree.get(key)
            search_end = timer()

        # Salva i risultati solo se i è multiplo di step
        if i == savedCountInsertion * step_insertion and i < insertion_n:
            savedCountInsertion += 1
            insert_result[i] = insert_end - insert_start
            insert_iterations_result[i] = insert_iterations

        if i == savedCountSearch * step_search and i < search_n:
            savedCountSearch += 1
            search_result[i] = search_end - search_start


        # Aggiorna la barra di progresso
        # progress_bar.update(i)

    # Print
    print("FINE TEST SU " + name.upper() + " (N=" + str(N) + ")")
    print("Tempo totale: ", timer() - testStart)
           

    # Salva i risultati dell'inserimento in un file excel
    insertion_filename = get_insertion_filename(name)
    save_results(insert_result, insertion_filename)

    # Salva i risultati delle iterazioni dell'inserimento in un file excel
    insertion_iterations_filename = get_insertion_iterations_filename(name)
    save_results(insert_iterations_result, insertion_iterations_filename)

    # Salva i risultati della ricerca in un file excel
    find_filename = get_search_filename(name)
    save_results(search_result, find_filename)

    
   
        
def plot_saved_results(names):
    """
    Esegue il plot dei risultati salvati in precedenza.
    Disegna: 
        - singolarmente le prestazioni dell'inserimento 
        - singolarmente le iterazioni dell'inserimento
        - tutti i risultati dell'inserimento insieme
        - singolarmente le prestazioni della ricerca

    Parameters:
    - names (list): Lista contenente i nomi dei test da plottare.
    """
    
    tests = {
        "insertion": {},
        "insertion_iterations": {},
        "search": {}
    }

    # Carica tutti i risultati 
    for name in names:
        insertion_results = load_results( get_insertion_filename(name))
        insertion_iterations = load_results(get_insertion_iterations_filename(name))
        search_results = load_results(get_search_filename(name))

        if insertion_results != None:
            tests["insertion"][name] = insertion_results

        if insertion_iterations != None:
            tests["insertion_iterations"][name] = insertion_iterations

        if search_results != None:
            tests["search"][name] = search_results
    

    # Plotta i risultati dell'inserimento singolarmente 
    for name in tests["insertion"].keys():
        if tests["insertion"][name] != None:
            plot_results(tests["insertion"][name], "Inserimento in un " + name, get_insertion_filename(name), "Dimensione dell'albero", "Tempo di inserimento (s)")
        else:
            print("Nessun risultato per " + name)


    # Plotta i risultati dell'inserimento tutti insieme     
    plot_muliple_results(tests["insertion"], "Confronto BST, BST FLAG e BST LIST nell'inserimento", "comparison_insertion", "Dimensione dell'albero", "Tempo di inserimento (s)")


    # Plotta i risultati delle iterazioni dell'inserimento singolarmente
    for name in tests["insertion_iterations"].keys():
        if tests["insertion_iterations"][name] != None:
            plot_results(tests["insertion_iterations"][name], "Iterazioni nell'inserimento in un " + name, get_insertion_iterations_filename(name), "Dimensione dell'albero", "Numero di iterazioni")
        else:
            print("Nessun risultato per " + name)
    
    # Plotta i risultati della ricerca singolarmente    
    for name in tests["search"].keys():
        if tests["search"][name] != None:
            plot_results(tests["search"][name], "Ricerca in un " + name, get_search_filename(name), "Dimensione dell'albero", "Tempo di ricerca (s)", False)
        else:
            print("Nessun risultato per " + name)




def plot_results(result, title, filename,  xLabel, yLabel, zoom=True):
    """
    Esegue il plot dei risultati di un test.

    Parameters:
    - results (dict): Dizionario contenente i risultati del test.
    - title (str): Titolo del plot.
    - filename (str): Nome del file in cui salvare il plot.
    - xLabel (str): Nome dell'asse x.
    - yLabel (str): Nome dell'asse y.
    - zoom (bool): Se True, limita l'asse y per concentrare il plot nella regione con la media dei tempi.
    """
        
    x = list(result.keys())
    y = list(result.values())
    plt.plot(x, y, 'o', color='blue', markersize=2.5)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)


    # Limita l'asse y per concentrare il plot nella regione con la media dei tempi
    if zoom:
        mean = sum(y) / len(y)
        plt.ylim(0, mean * 2)


    # Salva l'immagine
    source = "./outputs/" + filename
    plt.savefig(source)

    plt.close()




def plot_muliple_results(results, title, filename, xLabel, yLabel):
    """
    Esegue il plot di più risultati di test contemporaneamente.

    Parameters:
    - results (dict): Dizionario contenente i risultati dei test.
                      Come chiave ha il nome del test e come valore
                      un dizionario contenente i risultati del test.
    - title (str): Titolo del plot.
    - filename (str): Nome del file in cui salvare il plot.
    - xLabel (str): Nome dell'asse x.
    - yLabel (str): Nome dell'asse y.
    """


    for name in results.keys():
        result = results[name]
        x = list(result.keys())
        y = list(result.values())
        plt.plot(x, y, "o", markersize=2.5, label=name)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()

    # Limita l'asse x al plot con meno chiavi inserite
    min_x = min([max(result.keys()) for result in results.values()])
    plt.xlim(0, min_x)
    
    # Limita l'asse y per concentrare il plot nella regione con la media dei tempi
    y_values = [list(result.values()) for result in results.values()]
    y_values = [item for sublist in y_values for item in sublist]
    mean = sum(y_values) / len(y_values)
    plt.ylim(0, mean * 2)



    # Salva l'immagine
    source = "./outputs/" + filename
    plt.savefig(source)

    plt.close()

    