import queue

class TreeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

class BainaryTree:
    def __init__(self):
        self.root = None
    
    def preOrder(self,root):
        if root != None:
            print('[%s] '%root.data,end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def inOrder(self,root):
        if root != None:
            self.inOrder(root.left)
            print('[%s] '%root.data,end=' ')
            self.inOrder(root.right)

    def postOrder(self,root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print('[%s] '%root.data,end=' ')
    
    def levelOrder(self,root):
        Q = queue.Queue()
        Q.put(root)
        while not Q.empty():
            node = Q.get()
            print('[%s] '%node.data,end=' ')
            if node.left != None:
                Q.put(node.left)
            if node.right != None:
                Q.put(node.right)
    
    def getNodeCount(self,node):
        count = 0
        if node != None:
            count = 1 + self.getNodeCount(node.left) + self.getNodeCount(node.right)
        return count
    
    def isExternal(self,node):
        return node.left == None and node.right == None
    
    def getLeafCount(self,node):
        count = 0
        if node != None:
            if self.isExternal(node):
                count = 1
            else:
                count = self.getLeafCount(node.left) + self.getLeafCount(node.right)
        return count
    
    def getHeight(self,node):
        if node == None:
            return 0
        else:
            return 1 + max(self.getHeight(node.left),self.getHeight(node.right))


if __name__ == "__main__":
    T = BainaryTree()

    N4 = TreeNode('D',None,None)  
    N5 = TreeNode('E',None,None)
    N6 = TreeNode('F',None,None)
    N2 = TreeNode('B',N4,N5)
    N3 = TreeNode('C',N6,None)
    N1 = TreeNode('A',N2,N3)

    print('Pre : ',end='');T.preOrder(N1);print()
    print('In : ',end='');T.inOrder(N1);print()
    print('Post : ',end='');T.postOrder(N1);print()
    print('Level : ',end='');T.levelOrder(N1);print()

    print("Num of Nodes : ",T.getNodeCount(N1))
    print("Num of Leaf Nodes : ",T.getLeafCount(N1))

    print("Height of Tree : ",T.getHeight(N1))