class Tree:

    def __init__(self, data, children = []):
        self.data = data
        self.children = []


    def __str__(self, level= 0):
        ret = "   " * level + str(self.data) + "\n"
        for child in self.children:
            ret+= child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = Tree("Drinks", [])
hot = Tree("Hot", [])
cold = Tree("Cold", [])

tree.addChild(hot)
tree.addChild(cold)

fanta = Tree("Fanta", [])
cola = Tree("cola", [])

cold.addChild(fanta)
cold.addChild(cola)

coffee = Tree("Coffee", [])
tea = Tree("Tea", [])

hot.addChild(coffee)
hot.addChild(tea)

print(tree)