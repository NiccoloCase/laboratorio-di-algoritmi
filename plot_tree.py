import matplotlib.pyplot as plt

def plot_tree(tree):
    fig, ax = plt.subplots()
    _plot_tree(ax, tree.root, x=0, y=0, level=1)
    ax.axis('off')
    # bg color grey
    fig.set_facecolor('#202020')

    plt.show()

def _plot_tree(ax, node, x, y, level):
    if node is not None:
        ax.annotate(node.key, (x, y), xytext=(x, y),
                ha='center', va='center', bbox=dict(boxstyle='circle', fc='w'))

    xfactor = 1/2
    y_new = level * -2

    if node.left is not None:
        x_new = x - xfactor ** level
        ax.plot([x, x_new], [y, y_new], color="white", linewidth=.7)
        _plot_tree(ax, node.left, x_new, y_new, level + 1)

    if node.right is not None:
        x_new = x + xfactor ** level
        ax.plot([x, x_new], [y, y_new], color="white", linewidth=.7)
        _plot_tree(ax, node.right, x_new, y_new, level + 1)