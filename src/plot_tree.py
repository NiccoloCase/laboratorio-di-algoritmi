import matplotlib.pyplot as plt

def plot_tree(tree, filename=None):
    """
    Disegna un Albero Binario di Ricerca.

    Parameters:
    - tree (BST): L'albero da disegnare.
    - filename (str): Nome del file in cui salvare il plot.
    """

    fig, ax = plt.subplots()
    _plot_tree(ax, tree.root, x=0, y=0, level=1)
    ax.axis('off') # Nasconde gli assi

    if filename:
        plt.savefig(filename, format='png', dpi=300)
        plt.close()
    else: plt.show()


# Funzione ricorsiva per disegnare i nodi dell'albero
def _plot_tree(ax, node, x, y, level):
    if node is not None:
        # Disegna il nodo
        ax.annotate(node.key, (x, y), xytext=(x, y),
                color="white",    
                ha='center',
                va='center', 
                bbox=dict(boxstyle='circle', fc='#505050')
        )

    xfactor = 1/2 # Fattore di scala per la coordinata x
    y_new = level * -2 # Calcola la nuova coordinata y in base al livello

    if node.left is not None:
        x_new = x - xfactor ** level # Se è figlio sinistro, si sposta a sinistra il prossimo nodo
        ax.plot([x, x_new], [y, y_new], linewidth=.8,color="#404040")
        _plot_tree(ax, node.left, x_new, y_new, level + 1)

    if node.right is not None:
        x_new = x + xfactor ** level
        ax.plot([x, x_new], [y, y_new],  linewidth=.8, color="#404040")
        _plot_tree(ax, node.right, x_new, y_new, level + 1)



def plot_list_tree(tree, filename=None):

    """
    Disegna un Albero Binario di Ricerca con Lista concatenata per chiavi duplicate.
    Tra parentesi viene indicato il numero di duplicati per ogni chiave.

    Parameters:
    - tree (BST): L'albero da disegnare.
    - filename (str): Nome del file in cui salvare il plot.
    """

    fig, ax = plt.subplots()
    _plot_list_tree(ax, tree.root, x=0, y=0, level=1)
    ax.axis('off')

    if filename:
        plt.savefig(filename, format='png', dpi=300)
        plt.close()
    else: plt.show()


def _plot_list_tree(ax, node, x, y, level):
    if node is not None:

        text = str(node.key) + "(" + str(node.duplicates + 1) + ")"

        ax.annotate(text, (x, y), xytext=(x, y),
                color="white",    
                ha='center',
                va='center', 
                bbox=dict(boxstyle='circle', fc='#505050')
        )

    xfactor = 1/2
    y_new = level * -2

    if node.left is not None:
        x_new = x - xfactor ** level
        ax.plot([x, x_new], [y, y_new], linewidth=.8,color="#404040")
        _plot_list_tree(ax, node.left, x_new, y_new, level + 1)

    if node.right is not None:
        x_new = x + xfactor ** level
        ax.plot([x, x_new], [y, y_new],  linewidth=.8, color="#404040")
        _plot_list_tree(ax, node.right, x_new, y_new, level + 1)



