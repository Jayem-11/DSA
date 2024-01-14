import queue_ll 
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


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue_ll.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)

            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)



# preOrderTraversal(tree)
# inOrderTraversal(tree)
# postOrderTraversal(tree)

levelOrderTraversal(tree)
