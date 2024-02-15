from bst import BST
from plot_tree import plot_tree


def generate_normal_implementation_img_1():
    tree = BST()   

    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(2)
    tree.insert(2)
    tree.insert(4)

    plot_tree(tree)



def generate_normal_implementation_img_2():
    tree = BST()   

    tree.insert(3)
    tree.insert(2)
    tree.insert(2)
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    



    plot_tree(tree)


def generate_generic_bst_img():
    tree = BST()   

    tree.insert(12)
    tree.insert(1)
    tree.insert(3)
    tree.insert(17)
    tree.insert(11)
    tree.insert(0)
    tree.insert(3)
    tree.insert(20)

    plot_tree(tree)



if __name__ == "__main__":
   generate_normal_implementation_img_1()