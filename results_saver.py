import pandas as pd

def save_results(results, name): 
    # Formatta i risultati dei test
    n, time = format_results(results)

    # Salva i risultati in un file excel
    payload = {
        'n': n,
        'time': time
    }
    df = pd.DataFrame(payload) 
    timestamp = pd.Timestamp.now()
    filename = name + "_" + timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    src = "./outputs/" + filename + '.xlsx'
    df.to_excel(src, index=False)







def format_results(results):
    # Excel ha un limite di righe, quindi riduciamo il numero di righe
    max_rows = 1000000 - 10

    n = list(results.keys())
    time = list(results.values())


    if len(n) <= max_rows:
        return n, time
    
    else:
        
        step = len(n) // max_rows
        n_short = n[::step]
        time_short = time[::step]

        return n_short, time_short