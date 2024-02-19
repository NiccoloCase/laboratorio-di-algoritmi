from plot_tree import plot_tree
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from saver import save_results, load_results

def run_tree_test(TreeClass, name, N=10000):
    """
    Esegue i test su una classe di albero.

    Parameters:
    - TreeClass (class): Classe dell'albero su cui eseguire i test.
    - name (str): Nome dell'albero.
    """
        

    # -----------------------------------------------------------
    # CONFIGURAZIONE TEST
    key = 1 # Chiave da inserire
    n = N # Numero di chiavi da inserire
    maxRecords = 100000 # Massimo numero di records da salvare
    # ----------------------------------------------------------

    tree = TreeClass()
    insert_result = {}

    # Evita di salvare troppi risultati
    step =  1 if n <= maxRecords else  n // maxRecords # Calcola il passo con cui salvare i risultati
    savedCount = 0   # Tiene traccia del passo corrente

    for i in range(n):
        start = timer()
        tree.insert(key)
        end = timer()

        # Salva i risultati solo se i è multiplo di step
        if i == savedCount * step:
            insert_result[i] = end - start
            savedCount += 1

    # Salva i risultati dell'inserimento in un file excel
    insertion_filename = get_insertion_filename(name)
    save_results(insert_result, insertion_filename)
    
   # plot_results(insert_result, "Inserimento in un BST", "inserimento", insertion_filename)
    
        

def plot_saved_results(names):
    """
    Esegue il plot dei risultati salvati in precedenza.

    Parameters:
    - names (list): Lista contenente i nomi dei test da plottare.
    """
    
    tests = {
        "insertion": {}
    }

    # Carica tutti i risultati 
    for name in names:

        insertion_filename = get_insertion_filename(name)
        insertion_results = load_results(insertion_filename)

        if insertion_results != None:
            tests["insertion"][name] = insertion_results
    


    # Plotta i risultati dell'inserimento singolarmente 
    for name in tests["insertion"].keys():
        if tests["insertion"][name] != None:
            plot_results(tests["insertion"][name], "Inserimento in un " + name, "inserimento", get_insertion_filename(name))
        else:
            print("Nessun risultato per " + name)


    # Plotta i risultati dell'inserimento tutti insieme     
    plot_muliple_results(tests["insertion"], "Confronto BST, BST FLAG e BST LIST nell'inserimento", "inserimento", "comparison_insertion")


        
    #plot_results(insertion_results, "Inserimento in un " + name, "inserimento", insertion_filename)



def get_insertion_filename(name):
    """
    Restituisce il nome del file excel in cui salvare i risultati dell'inserimento.

    Parameters:
    - name (dict): Nome del test.
    """
    name = name.lower().replace(" ", "_")
    return name + "_insertion"



def plot_results(result, title, operationName, filename):
    """
    Esegue il plot dei risultati di un test.

    Parameters:
    - results (dict): Dizionario contenente i risultati del test.
    - title (str): Titolo del plot.
    - operationName (str): Nome dell'operazione. 
    - filename (str): Nome del file in cui salvare il plot.
    """
        

    x = list(result.keys())
    y = list(result.values())
    plt.plot(x, y, 'o', color='blue', markersize=2.5)
    plt.xlabel('Numero di chiavi inserite')
    plt.ylabel('Tempo di ' + operationName + " (s)")
    plt.title(title)


    # Limita l'asse y per concentrare il plot nella regione con la media dei tempi
    mean = sum(y) / len(y)
    plt.ylim(0, mean * 2)



    # Salva l'immagine
    source = "./outputs/" + filename
    plt.savefig(source)

    plt.close()




def plot_muliple_results(results, title, operationName, filename):
    """
    Esegue il plot di più risultati di test contemporaneamente.

    Parameters:
    - results (dict): Dizionario contenente i risultati dei test.
                      Come chiave ha il nome del test e come valore
                      un dizionario contenente i risultati del test.
    - title (str): Titolo del plot.
    - operationName (str): Nome dell'operazione. 
    - filename (str): Nome del file in cui salvare il plot.
    """

    

    for name in results.keys():
        result = results[name]
        x = list(result.keys())
        y = list(result.values())
        plt.plot(x, y, "o", markersize=2.5, label=name)

    plt.xlabel('Numero di chiavi inserite')
    plt.ylabel('Tempo di ' + operationName + " (s)")
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

    