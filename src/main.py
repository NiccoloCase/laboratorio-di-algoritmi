from bst.bst import BST
from bst.bst_flag import BST_FLAG
from bst.bst_list import BST_LIST
from plot_tree import plot_tree
from timeit import default_timer as timer
import sys
from tests import run_tree_test, plot_saved_results

sys.setrecursionlimit(500000000)


def main():
    #test_bst_list()
    #test_bst_flag()
    #save_results()



    # run_tree_test(BST, "BST", 10000)
    # run_tree_test(BST_FLAG, "BST FLAG", 1000000)
    # run_tree_test(BST_LIST, "BST LIST", 1000000)
    plot_saved_results(["BST", "BST FLAG", "BST LIST"])


if __name__ == "__main__":
   main()