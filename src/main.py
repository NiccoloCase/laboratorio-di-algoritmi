from bst.bst import BST
from bst.bst_flag import BST_FLAG
from bst.bst_list import BST_LIST
from timeit import default_timer as timer
import sys
from tests import run_tree_test, plot_saved_results, plot_results
from plot_tree import plot_tree, plot_list_tree
from saver import summarise_file,create_joined_file
from progressbar import ProgressBar
from time import sleep


sys.setrecursionlimit(500000000)



# Valori con cui ho eseguito i test:
# BST_INSERTION_N = 200000
# BST_FLAG_INSERTION_N = 1000000
# BST_LIST_INSERTION_N = 1000000
# SEARCH_N = 1000

BST_INSERTION_N = 200000
BST_FLAG_INSERTION_N = 1000000
BST_LIST_INSERTION_N = 1000000
SEARCH_N = 1000

def main():
   # run_tree_test(BST, "BST", BST_INSERTION_N, SEARCH_N)
    # run_tree_test(BST_FLAG, "BST FLAG", BST_FLAG_INSERTION_N, SEARCH_N)
    # run_tree_test(BST_LIST, "BST LIST", BST_LIST_INSERTION_N, SEARCH_N)
    
    #plot_saved_results(["BST", "BST FLAG", "BST LIST"])
   create_joined_file()


if __name__ == "__main__":
   main()