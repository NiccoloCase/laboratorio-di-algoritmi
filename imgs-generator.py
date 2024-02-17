from bst import BST
from bst_flag import BST_FLAG
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



def generate_normal_implementation_img_3():
    tree = BST()   

    for i in range(1, 17):
        tree.insert(1)

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





def generate_bst_flag_img():
    tree = BST_FLAG()   

    for i in range(1, 100):
        tree.insert(1)

    plot_tree(tree)




if __name__ == "__main__":
   generate_normal_implementation_img_3()