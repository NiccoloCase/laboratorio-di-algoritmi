from random import randint


# NODO DI UN ALBERO BINARIO DI RICERCA
class Node:
   def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
   def get(self):
      return self.key
   def set(self, key):
      self.key = key
   def getChildren(self):
      children = []
      if (self.left != None):
         children.append(self.left)
      if (self.right != None):
         children.append(self.right)
      return children
        

# ALBERO BINARIO DI RICERCA
class BST_FLAG:
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
    # Presuppone che l'albero non sia vuoto (no inserimento nella radice)
    def _insertNode(self, currentNode, key):
        if(currentNode.key == key):
            # decide casualmente se inserire a sinistra o a destra
            if(randint(0, 1) == 0):
                if (currentNode.left):
                    self._insertNode(currentNode.left, key)
                else:
                    currentNode.left = Node(key)
            else:
                if (currentNode.right):
                    self._insertNode(currentNode.right, key)
                else:
                    currentNode.right = Node(key)
        

        if (key < currentNode.key):
            if (currentNode.left):
                self._insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if (currentNode.right):
                self._insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)
                
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


