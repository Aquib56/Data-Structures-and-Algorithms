class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self,val):
        self.root=Node(val)

    def reverseLevelOrder(self,root):
        if root==None:
            return None
        queue=[]
        res=[]
        queue.append(root)
        while queue:
            res.append(queue[0].val)
            currentNode=queue.pop(0)
            if currentNode.left :
                queue.append(currentNode.left)  
            if currentNode.right:
                queue.append(currentNode.right)
        res.reverse()
        return res

tree=BinaryTree(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
n5=Node(6)
tree.root.left=n1
tree.root.right=n2
n1.left=n3
n1.right=n4
n2.right=n5
print(tree.reverseLevelOrder(tree.root))

