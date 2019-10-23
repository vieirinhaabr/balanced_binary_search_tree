from balanced_binary_search_tree import Tree

if __name__ == "__main__":
    tree_control = Tree()

    tree_control.insert_in_tree(10)
    tree_control.insert_in_tree(50)
    tree_control.insert_in_tree('25')
    tree_control.insert_in_tree(5)
    tree_control.insert_in_tree(1)
    tree_control.insert_in_tree(3)
    tree_control.insert_in_tree(7)
    tree_control.insert_in_tree(75)
    tree_control.insert_in_tree(4)
    tree_control.insert_in_tree(5)

    print('\nin order: ', end='')
    tree_control.in_order()

    print('\nRight height of tree: ', tree_control.right_tree_height())
    print('\nLeft height of tree: ', tree_control.left_tree_height())