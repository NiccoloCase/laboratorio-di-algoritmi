from bst.bst import BST
from bst.bst_flag import BST_FLAG
from bst.bst_list import BST_LIST
from timeit import default_timer as timer
import sys
from tests import run_tree_test, plot_saved_results, plot_results
from plot_tree import plot_tree, plot_list_tree
from saver import summarise_file
from progressbar import ProgressBar
from time import sleep


sys.setrecursionlimit(500000000)


def test_search_bst():
    tree = BST_LIST()
    results ={}
    iterations = {}
     
    for i in range(20000):
        tree.insert(1)


        start = timer()
        x, iteractionsCount = tree.get(1)
        end = timer()

        results[i] = end - start
        iterations[i] = iteractionsCount


        print("Numero risultati: ", len(x))




    plot_results(results, "BST", "ricerca", "x", False)
    plot_results(iterations, "BST", "ricerca", "x", True)
    

    def search():
        tree = BST_LIST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(2)
        tree.insert(2)
        tree.insert(2)
        tree.insert(3)
        tree.insert(3)

        foundNodes, iterations = tree.get(2)

        print("Risultati: ")
        for i in foundNodes:
            print(i.key)

        print("Iterazioni: ", iterations)

        plot_list_tree(tree)



def main():

    # run_tree_test(BST, "BST", 10000, 10000)
    run_tree_test(BST_FLAG, "BST FLAG", 1000000, 10000)
    # run_tree_test(BST_LIST, "BST LIST", 1000000, 10000)
    
    # plot_saved_results(["BST", "BST FLAG", "BST LIST"])



if __name__ == "__main__":
   main()