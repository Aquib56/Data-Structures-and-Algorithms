class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
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

    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q=[root]
        res=[]
        leftToright=True
        while q:
            levelNodes=[]
            levelLenght=len(q)
            for i in range(levelLenght):
                currNode=q.pop(0)
                levelNodes.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            if not leftToright:
                levelNodes.reverse()
            res.append(levelNodes)
            leftToright=not leftToright
        return res

    def zigzagtraversal(self,root):
            level=1
            if not root:
                return None
            queue=[]
            queue.append(root)
            while queue:
                currentNode=queue.pop(0)
                print(currentNode.val,end=" ")
                if level%2!=0:
                    if currentNode.right:
                        queue.append(currentNode.right)
                    if currentNode.left:
                        queue.append(currentNode.left)
                    level+=1
                else:
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)

tree=BinaryTree(1)
n1=Node(9)
n2=Node(20)
n3=Node(4)
n4=Node(15)
n5=Node(7)


tree.root.left=n1
tree.root.right=n2
n1.left=n3
n2.left=n4
n2.right=n5
tree.levelOrder(tree.root)
print(tree.zigzagLevelOrder(tree.root))    
print(tree.zigzagtraversal(tree.root))    
