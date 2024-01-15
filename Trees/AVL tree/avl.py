import queue_ll 

class avlNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

 
def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
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
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)

def searchNode(rootNode, NodeValue):
    if rootNode == NodeValue:
        print("The value is found")

    elif NodeValue < rootNode.data:
        if rootNode.leftchild.data == NodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftchild, NodeValue)
    else:
        if rootNode.rightchild.data == NodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightchild, NodeValue)


            
newAVL  = avlNode(10)
