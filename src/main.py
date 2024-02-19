from bst.bst import BST
from bst.bst_flag import BST_FLAG
from bst.bst_list import BST_LIST
from plot_tree import plot_tree
from timeit import default_timer as timer
import sys
import matplotlib.pyplot as plt
import random
from results_saver import save_results


sys.setrecursionlimit(500000000)


def random_key(max=20):
    return random.randint(0, max)
    

def test_bst():
    n = 5000

    tree = BST()

    insert_result = {}
    search_result = {}
    insert_iterations = {}

    for i in range(n):
        start = timer()

        key = 1
        iterations = tree.insert(key)
        end = timer()
        insert_result[i] = end - start

        # start = timer()
        # tree.get(key)
        # end = timer()
        # search_result[i] = end - start

        insert_iterations[i] = iterations

    #plot_tree(tree)
    plot_results(insert_result)
    plot_results(insert_iterations)
    #plot_results(search_result)
    


def test_bst_flag():
    n = 10000

    tree = BST_FLAG()

    insert_result = {}
    insert_iterations = {}
    search_result = {}

    for i in range(n):
        start = timer()

        key = 1
        iterations = tree.insert(key)
        end = timer()
        insert_result[i] = end - start
        insert_iterations[i] = iterations

        # start = timer()
        # tree.get(key)
        # end = timer()
        # search_result[i] = end - start



    #plot_tree(tree)
    plot_results(insert_iterations)
    plot_bst_flag_insertion_results(insert_result)






def test_bst_list():
    n = 5000

    tree = BST_LIST()

    insert_result = {}
    search_result = {}
    insert_iterations = {}

    for i in range(n):
        start = timer()

        key = 1
        iterations = tree.insert(key)
        end = timer()
        insert_result[i] = end - start

        # start = timer()
        # tree.get(key)
        # end = timer()
        # search_result[i] = end - start

        insert_iterations[i] = iterations

    #plot_tree(tree)
    plot_results(insert_result)
    plot_results(insert_iterations)
    #plot_results(search_result)
    





def plot_bst_flag_insertion_results(result):
    x = list(result.keys())
    y = list(result.values())


    plt.plot(x, y, 'o', color='blue', markersize=2.5)

    plt.ylim(0, 0.01)

    plt.savefig("../outputs/test_bst_flag_insertion.png")
    plt.show()


def plot_results(result):
    x = list(result.keys())
    y = list(result.values())

    plt.plot(x, y, 'o', color='blue', markersize=2.5)

    plt.savefig("outputs/test_bst_flag_insertion.png")
    plt.show()
  





def main():
    test_bst_list()
    #test_bst_flag()
    #save_results()


if __name__ == "__main__":
   main()