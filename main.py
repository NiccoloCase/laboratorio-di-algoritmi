from bst import BST
from bst_flag import BST_FLAG
from plot_tree import plot_tree

from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import random


sys.setrecursionlimit(500000)


def random_key(max=20):
    return random.randint(0, max)
    

def test_insertion():
    n = 30000

    tree = BST()

    insert_result = {}
    search_result = {}

    for i in range(n):
        start = timer()

        key = 1
        tree.insert(key)
        end = timer()
        insert_result[i] = end - start

        start = timer()
        tree.get(key)
        end = timer()
        search_result[i] = end - start



    # plot_results(insert_result)
    plot_results(search_result)
    



    



def plot_results(result):
  
    x = list(result.keys())
    y = list(result.values())

    plt.plot(x, y)
    plt.show()



def test_tree_visualization():
    tree = BST()   

    tree.insert(12)
    tree.insert(1)
    tree.insert(3)
    tree.insert(17)
    tree.insert(11)
    tree.insert(10)
    tree.insert(15)
    tree.insert(17)
    tree.insert(15)
    tree.insert(16)
    tree.insert(18)
    tree.insert(17)
    tree.insert(16.5)

    nodes = tree.get(17)
 
    print([node.key for node in nodes])
    
    plot_tree(tree)



    



def main():
    #test_tree_visualization()
    test_insertion()

if __name__ == "__main__":
   main()