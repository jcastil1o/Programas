class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def print_tree(node, level=0):
    print("  " * level + node.value)
    for child in node.children:
        print_tree(child, level + 1)

# Ejemplo de árbol de derivación para 'aabb'
root = TreeNode('S')
child1 = TreeNode('a')
child2 = TreeNode('S')
child3 = TreeNode('b')

root.add_child(child1)
root.add_child(child2)