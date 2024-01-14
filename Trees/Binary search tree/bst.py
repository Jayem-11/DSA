import queue_ll 

class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftchild == None:
            rootNode.leftchild = BST(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild == None:
            rootNode.rightchild = BST(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)
    
    return "Node has been inserted"


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
        
def minValueNode(bstNode):
    current = bstNode
    while (current.leftchild is not None):
        current = current.leftchild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild , nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild , nodeValue)

    else:
        if rootNode.leftchild is None:
            temp =  rootNode.rightchild
            rootNode = None
            return temp

        if rootNode.rightchild is None:
            temp =  rootNode.leftchild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BST has been succcessfully deleted"



        

newBST = BST(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
deleteNode(newBST, 20)
levelOrderTraversal(newBST)