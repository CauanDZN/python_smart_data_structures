class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def inorder_traversal(self, root):
        return (self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)) if root else []

tree = BinaryTree()
tree.root = tree.insert(tree.root, 50)
tree.insert(tree.root, 30)
tree.insert(tree.root, 20)
tree.insert(tree.root, 40)
tree.insert(tree.root, 70)
tree.insert(tree.root, 60)
tree.insert(tree.root, 80)
print("Binary Tree Inorder Traversal:", tree.inorder_traversal(tree.root))
