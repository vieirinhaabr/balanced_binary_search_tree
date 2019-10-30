from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    # Mean to go down -> 5.5 sec

    i = 0
    with Chronometer() as t:
        while i < 10000:
            info = rdn.randint(1,1000000)
            tree_control.insert_in_tree(info)
            if i == 5000:
                temp = info
            i = i + 1
    print('To insert spend {:.5f} seconds'.format(float(t)))

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

    """tree_control.insert_in_tree(20)
    tree_control.insert_in_tree(21)
    tree_control.insert_in_tree(22)
    tree_control.insert_in_tree(18)
    tree_control.insert_in_tree(19)
    tree_control.insert_in_tree(15)
    tree_control.insert_in_tree(17)
    tree_control.insert_in_tree(10)
    tree_control.insert_in_tree(9)
    tree_control.insert_in_tree(8)
    tree_control.insert_in_tree(7)"""

    """tree_control.insert_in_tree(50)
    tree_control.insert_in_tree(45)
    tree_control.insert_in_tree(55)
    tree_control.insert_in_tree(60)
    tree_control.insert_in_tree(57)
    tree_control.insert_in_tree(65)
    tree_control.insert_in_tree(46)
    tree_control.insert_in_tree(47)
    tree_control.insert_in_tree(48)
    tree_control.insert_in_tree(40)
    tree_control.insert_in_tree(43)
    tree_control.insert_in_tree(35)
    tree_control.insert_in_tree(37)
    tree_control.insert_in_tree(30)
    tree_control.insert_in_tree(25)
    tree_control.insert_in_tree(20)"""

    """tree_control.insert_in_tree(55)
    tree_control.insert_in_tree(50)
    tree_control.insert_in_tree(60)
    tree_control.insert_in_tree(51)
    tree_control.insert_in_tree(45)
    tree_control.insert_in_tree(54)
    tree_control.insert_in_tree(52)
    tree_control.insert_in_tree(53)"""

    tree_control.in_order()
    print('\n\n root: ', tree_control.root.info)

    print('\n Left height: ', tree_control.root.left_height)
    print(' Right height: ', tree_control.root.right_height)

    tree_control.search_node(temp)

    """print('\n', tree_control.root.right_height)

    print('\n', tree_control.root.left_height)

    print('\n', tree_control.root.right_node.right_height)

    print('\n', tree_control.root.right_node.right_node.right_height)
    print('', tree_control.root.right_node.right_node.left_height)

    print('\n', tree_control.root.right_node.right_node.right_node.right_height)

    print('\n', tree_control.root.left_node.left_height)
    print('', tree_control.root.left_node.right_height)"""