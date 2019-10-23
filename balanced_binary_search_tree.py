class Node(object):
    def __init__(self, info):
        self.info = info
        self.left_node = None
        self.right_node = None
        print("Node Inserted")

    """def __str__(self):
        return self.info"""

    def create_node(self, info):
        if info > self.info:
            if self.right_node is None:
                self.right_node = Node(info)
            else:
                self.right_node.create_node(info)
        elif info < self.info:
            if self.left_node is None:
                self.left_node = Node(info)
            else:
                self.left_node.create_node(info)
        else:
            print('Node ', info, ' is already on tree')


class Tree(object):
    def __init__(self):
        self.root = None

    def insert_in_tree(self, info):
        if type(info) == int:
            if self.root is not None:
                self.root.create_node(info)
            else:
                self.root = Node(info)
        else:
            print('Int expected, but ', info, ' are ', type(info), ' type variable')

    def in_order(self):
        self.in_order_run(self.root)

    def in_order_run(self, node):
        if node is None:
            return

        self.in_order_run(node.left_node)
        print(node.info, ' ', end='')
        self.in_order_run(node.right_node)

    def right_tree_height(self):
        return self.right_tree_height_run(self.root)

    def right_tree_height_run(self, node):
        if node is None:
            return + 0
        else:
            return + 1 + self.right_tree_height_run(node.right_node)

    def left_tree_height(self):
        return self.right_tree_height_run(self.root)

    def left_tree_height_run(self, node):
        if node is None:
            return + 0
        else:
            return + 1 + self.left_tree_height_run(node.left_node)