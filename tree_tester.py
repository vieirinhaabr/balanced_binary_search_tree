from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer

if __name__ == "__main__":
    tree_control = Tree()

    # Mean to go down -> 5.5 sec

    with Chronometer() as time:
        i = 0
        count = 50
        with Chronometer() as t:
            while i < count:
                info = rdn.randint(1,100)
                tree_control.insert_in_tree(info)
                if i == count/2:
                    temp = info
                i = i + 1
        print('To insert spend {:.5f} seconds'.format(float(t)))

        with Chronometer() as t:
            print('\nin order: ', end='')
            tree_control.in_order()
        print('\n\nTo print spend {:.5f} seconds'.format(float(t)))

        print('\nTree Info: ')
        print('      root -> ', tree_control.root.info)

        print('      Left height -> ', tree_control.root.left_height)
        print('      Right height -> ', tree_control.root.right_height)

        with Chronometer() as t:
            print('\nTrying to find ', temp, '...')
            tree_control.search_node(temp)
        print('    Was spend {:.5f} seconds on this search'.format(float(t)))
        print('\n')

        with Chronometer() as t:
            print('Getting Tree on tuple format...')
            tuple_tree = tree_control.print_tree_on_tuple()
            print(tuple_tree)
        print('    Was spend {:.5f} seconds in this operation'.format(float(t)))
        print('\n')

        with Chronometer() as t:
            tree_control.print_tree()
        print('\nWas spend {:.5f} seconds in this operation'.format(float(t)))

    print('\n\nWas spend {:.5f} seconds to execute all operations/commands'.format(float(time)))