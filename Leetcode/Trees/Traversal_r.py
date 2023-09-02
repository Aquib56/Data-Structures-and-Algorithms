class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
class BinaryTree:
    def __init__(self,val):
        self.root=Node(val)
    def levelOrder(self,root):
        if root==None:
            return None
        queue=[]
        queue.append(root)
        queue.append(None)
        while queue:
            currentNode=queue.pop(0)
            print(currentNode.val,end="")
            if currentNode.left :
                queue.append(currentNode.left)  
            if currentNode.right:
                queue.append(currentNode.right)
            if queue[0]==None:
                a=queue.pop(0)
                print("")
                if queue:
                    queue.append(None)

    def preorderTraversal(self, root):
        if not root:
            return []
        stack,res=[root],[]
        while stack:
            currNode=stack.pop()
            res.append(currNode.val)
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return res


tree=BinaryTree(1)
n1=Node(2)
n2=Node(3)
# n3=Node(4)
# n4=Node(5)
# n5=Node(6)


tree.root.right=n1
n1.left=n2
# n1.right=n4
# n2.right=n5
tree.levelOrder(tree.root)
print(tree.preorderTraversal(tree.root))
