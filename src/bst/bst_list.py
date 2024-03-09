# ALBERO BINARIO DI RICERCA CON GESTIONE DEI DUPLICATI CON LISTA CONCATENATA
from bst.bst import Node


class NodeList(Node):
    def __init__(self, key, parent=None):
        super().__init__(key, parent)
        self.next = None
        self.duplicates = 0


class BST_LIST:
    def __init__(self):
        self.root = None
        # Contatore interazioni per l'inserimento (per eseguire i test)
        self.insert_iterations_count = 0
        # Contatore interazioni per la ricerca (per eseguire i test)
        self.find_iterations_count = 0

    # Imposta la radice dell'albero
    def setRoot(self, key):
        self.root = NodeList(key)

    # Inserisce un nodo nell'albero
    def insert(self, key):
        self.insert_iterations_count = 0
        if (self.root is None): self.setRoot(key)
        else: self._insertNode(self.root, key)
        return self.insert_iterations_count

    # Funzione di supporto per l'inserimento di un nodo
    def _insertNode(self, currentNode, key):
        self.insert_iterations_count += 1

        # Gestione con lista concatenata dei duplicati
        if (key == currentNode.key):
            # Inserisce in testa alla lista 
            newNode = NodeList(key, currentNode)
            newNode.next = currentNode.next
            if(currentNode.next): currentNode.next.p = newNode
            currentNode.next = newNode
            currentNode.duplicates += 1

        
        if (key < currentNode.key):
            if (currentNode.left):
                self._insertNode(currentNode.left, key)
            else:
                currentNode.left = NodeList(key, currentNode)
        elif (key > currentNode.key):
            if (currentNode.right):
                self._insertNode(currentNode.right, key)
            else:
                currentNode.right = NodeList(key, currentNode)

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
            self.find_iterations_count -= 1
            # Scorriamo la lista dei duplicati
            while(currentNode is not None):
                found_nodes.append(currentNode)
                currentNode = currentNode.next
                self.find_iterations_count += 1

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
