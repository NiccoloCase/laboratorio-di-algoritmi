from random import randint


# NODO DI UN ALBERO BINARIO DI RICERCA
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.flag = False

   
        

# ALBERO BINARIO DI RICERCA
class BST_FLAG:
    def __init__(self):
        self.root = None
        self.insert_iterations_count = 0
        self.find_iterations_count = 0


    # Imposta la radice dell'albero
    def setRoot(self, key):
        self.root = Node(key)

    # Inserisce un nodo nell'albero
    def insert(self, key):
        self.insert_iterations_count = 0
        if (self.root is None): self.setRoot(key)
        else: self._insertNode(self.root, key)
        return self.insert_iterations_count

    # Funzione di supporto per l'inserimento di un nodo
    def _insertNode(self, currentNode, key):
        self.insert_iterations_count += 1
        
        if(currentNode.key == key):
            if(currentNode.flag): self._insert_right(currentNode, key)
            else: self._insert_left(currentNode, key)

            currentNode.flag = not currentNode.flag # Alterna il flag
    
        if (key < currentNode.key): self._insert_left (currentNode, key)
        elif (key > currentNode.key): self._insert_right(currentNode, key)

    # Funzione di supporto per l'inserimento di un nodo a sinistra
    def _insert_left(self, currentNode, key):
        if (currentNode.left): self._insertNode(currentNode.left, key)
        else: currentNode.left = Node(key)

    # Funzione di supporto per l'inserimento di un nodo a destra
    def _insert_right(self, currentNode, key):
        if (currentNode.right): self._insertNode(currentNode.right, key)
        else: currentNode.right = Node(key)

    # Restituisce un nodo nell'albero
    def get(self, key):
        found_nodes = []
        self.find_iterations_count = 0
        self._getNode(self.root, found_nodes, key)
        return found_nodes, self.find_iterations_count

    # Funzione ricorsiva di supporto per la ricerca di un nodo
    def _getNode(self, currentNode, found_nodes,  key):
        if (currentNode is None): return
        self.find_iterations_count += 1
        if (key == currentNode.key):
            found_nodes.append(currentNode)
            # Abbiamo trovato il nodo, ma dobbiamo continuare la ricerca nel sottoalbero sinistro
            # per cercare eventuali nodi con lo stesso valore
            if (currentNode.left is not None):
                self._getNode(currentNode.left, found_nodes, key)
            # Continuamo la ricerca anche sottoalbero destro
            if (currentNode.right is not None):
                self._getNode(currentNode.right, found_nodes, key)

        elif (key < currentNode.key): 
            return self._getNode(currentNode.left, found_nodes, key)
        else:
            return self._getNode(currentNode.right, found_nodes, key)  

    # Cerca un nodo nell'albero
    # Restituisce True se lo trova, False altrimenti
    def find(self, key):
        return self._findNode(self.root, key)

    # Funzione ricorsiva di supporto per la ricerca di un nodo
    def _findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self._findNode(currentNode.left, key)
        else:
            return self._findNode(currentNode.right, key)
        
    # Attreversa l'albero in ordine
    def printInorder(self):
        def _inorder(v):
            if(v is None):
                return
            if(v.left is not None):
                _inorder(v.left)
            print(v.key)
            if(v.right is not None):
                _inorder(v.right)
                
        _inorder(self.root)
