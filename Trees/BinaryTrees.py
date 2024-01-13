class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


tree = Tree("Drinks")
hot = Tree("Hot")
cold = Tree("Cold")

tree.left = hot
tree.right = cold


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)


# preOrderTraversal(tree)
# inOrderTraversal(tree)
postOrderTraversal(tree)
