# Implementazione di un albero binario di ricerca (BST) senza duplicati
# (Non usato, codice solo per la relazione)


class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = parent

class BST:
    def __init__(self):
        self.root = None

    # Imposta la radice dell'albero
    def setRoot(self, key):
        self.root = Node(key)

    # Inserisce un nodo nell'albero
    def insert(self, key):
        if (self.root is None):
            self.setRoot(key)
        else:
            self._insertNode(self.root, key)

    # Funzione di supporto per l'inserimento di un nodo
    def _insertNode(self, currentNode, key):
        if (key < currentNode.key):
            if (currentNode.left):
                self._insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key, currentNode)
        elif (key > currentNode.key):
            if (currentNode.right):
                self._insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key, currentNode)


    def get(self, key):
        return self._getNode(self.root, key)

    def _getNode(self, currentNode, key):
        if (currentNode is None): return None
        if (key == currentNode.key): return currentNode
        if (key < currentNode.key):
            return self._getNode(currentNode.left, key)
        else:
            return self._getNode(currentNode.right, key)