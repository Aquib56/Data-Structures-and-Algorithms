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
    def findSpiral(self,root):
        q=[root]
        level=2
        res=[]
        while q:
            size=len(q)
            for i in range(size):
                node=q.pop(0)
                res.append(node.val)
                if level%2!=0:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
            level+=1
            q=q[::-1]
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
print(tree.levelOrder(tree.root))
print(tree.findSpiral(tree.root))

