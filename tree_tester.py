from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    # Mean to go down -> 5.5 sec

    """i = 0
    with Chronometer() as t:
        while i < 10000:
            tree_control.insert_in_tree(rdn.randint(1,1000000))
            i = i + 1
    print('To insert spend {:.5f} seconds'.format(float(t)))"""

    """with Chronometer() as t:
        print('\nin order: ', end='')
        tree_control.in_order()
    print('To print spend {:.5f} seconds'.format(float(t)))"""

    """tree_control.insert_in_tree(20)
    tree_control.insert_in_tree(25)
    tree_control.insert_in_tree(19)
    tree_control.insert_in_tree(15)
    tree_control.insert_in_tree(14)
    tree_control.insert_in_tree(16)
    tree_control.insert_in_tree(17)"""

    tree_control.insert_in_tree(20)
    tree_control.insert_in_tree(21)
    tree_control.insert_in_tree(22)
    tree_control.insert_in_tree(18)
    tree_control.insert_in_tree(19)
    tree_control.insert_in_tree(15)
    tree_control.insert_in_tree(17)
    tree_control.insert_in_tree(10)
    tree_control.insert_in_tree(9)
    tree_control.insert_in_tree(8)
    tree_control.insert_in_tree(7)

    tree_control.in_order()
    print('\n\n root: ', tree_control.root.info)

    print('\n left: ', tree_control.left_height)

    print('\n right: ', tree_control.right_height)