import sys
sys.stdin=open('../input.txt','r')

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
        self.root = None

    def traverse(self):
        traversal = []
        if self.left: traversal += self.left.traverse()
        traversal.append(self)
        if self.right:traversal += self.right.traverse()
        return traversal

    def inorder(self):
        traversal = []
        if self.left: traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right: traversal += self.right.inorder()
        return traversal
    def preorder(self):
        traverse = []
        traverse.append(self.data)
        if self.left: traverse += self.left.preorder()
        if self.right: traverse += self.right.preorder()
        return traverse
    def postorder(self):
        traverse = []
        if self.left: traverse += self.left.postorder()
        if self.right: traverse += self.right.postorder()
        traverse.append(self.data)
        return traverse

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def traverse(self):
        if self.root:
            return self.root.traverse()

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

n=int(input().strip())
ch=input().strip()
x,y=map(int,input().strip().split())
a=1
ans=BinaryTree(Node(a))
