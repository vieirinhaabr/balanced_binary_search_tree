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
                return 1
            else:
                return 1 + self.right_node.create_node(info)
        elif info < self.info:
            if self.left_node is None:
                self.left_node = Node(info)
                return 1
            else:
                return 1 + self.left_node.create_node(info)
        else:
            print('Node ', info, ' is already on tree')
            return 0


class Tree(object):
    def __init__(self):
        self.root = None
        self.left_height = 0
        self.right_height = 0

    def insert_in_tree(self, info):
        if type(info) == int:
            if self.root is not None:
                height = self.root.create_node(info)
                if height != 0:
                    if info > self.root.info:
                        if height > self.right_height:
                            self.right_height = height
                    elif info < self.root.info:
                        if height > self.left_height:
                            self.left_height = height
                    #need_balance(self.root)
            else:
                self.left_height = 1
                self.right_height = 1
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