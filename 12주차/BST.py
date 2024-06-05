class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    
    return root

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print("%2d " % root.key, end='')
        inOrder(root.right)

def display(root, msg):
    print(msg, end='')
    inOrder(root)
    print()

def minkeyNode(root):
    while root is not None and root.left is not None:
        root = root.left
    return root

def delete(root, key):
    if root is None:
        return None
    
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = minkeyNode(root.right)
            root.key = succ.key
            root.right = delete(root.right, succ.key)
    
    return root

if __name__ == '__main__':
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, "[insert %2d] : " % key)

    print()

    root = delete(root, 30)
    display(root, "[delete 30] : ")
    root = delete(root, 26)
    display(root, "[delete 26] : ")

    root = delete(root, 35)
    display(root, "[delete 35] : ")
