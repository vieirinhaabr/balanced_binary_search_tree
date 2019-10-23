class Node(object):
    def __init__(self, info):
        self.info = info
        self.LeftNode = None
        self.RightNode = None

    """def __str__(self):
        return self.info"""

    def insert_node(self, info):
        try:
            if info > self.info:
                if self.RightNode is None:
                    self.RightNode = Node(info)
                else:
                    self.RightNode.insert_node(info)
            if info < self.info:
                if self.LeftNode is None:
                    self.LeftNode = Node(info)
                else:
                    self.LeftNode.insert_node(info)