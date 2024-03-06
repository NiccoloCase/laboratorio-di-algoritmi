from bst.bst import BST
from bst.bst_flag import BST_FLAG
from bst.bst_list import BST_LIST
import sys
from tests import run_tree_test, plot_saved_results
from saver import create_joined_file
from imgs_generator import generateAllImgs



# Aumento il limite di ricorsione per poter eseguire i test con un numero di nodi maggiore
sys.setrecursionlimit(500000000)

# ------------------------------------------
# Valori con cui ho eseguito i test:
# BST_INSERTION_N = 200000
# BST_FLAG_INSERTION_N = 1000000
# BST_LIST_INSERTION_N = 1000000
# SEARCH_N = 1000
# ------------------------------------------

BST_INSERTION_N = 10000
BST_FLAG_INSERTION_N = 10000
BST_LIST_INSERTION_N = 10000
SEARCH_N = 1000

def main():
   run_tree_test(BST, "BST", BST_INSERTION_N, SEARCH_N)
   run_tree_test(BST_FLAG, "BST FLAG", BST_FLAG_INSERTION_N, SEARCH_N)
   run_tree_test(BST_LIST, "BST LIST", BST_LIST_INSERTION_N, SEARCH_N)
   plot_saved_results(["BST", "BST FLAG", "BST LIST"])
   create_joined_file()
   generateAllImgs()


if __name__ == "__main__":
   main()