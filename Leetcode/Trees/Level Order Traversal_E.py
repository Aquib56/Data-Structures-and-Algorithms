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
    def levelOrder2(self,root):
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

    def levelOrder(self, root):
        queue,res,temp=[],[],[]
        queue.append(root)
        res.append([root.val])
        while queue:
            current=queue.pop(0)
            if current.left:
                queue.append(current.left)
                temp.append(current.left.val)
            if current.right:
                queue.append(current.right)
                temp.append(current.right.val)
            if temp:
                res.append(temp)
            temp=[]
        return res
            


tree=BinaryTree(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)


tree.root.left=n1
tree.root.right=n2
n1.left=n3
n2.right=n4
print(tree.levelOrder(tree.root))
print(tree.levelOrder2(tree.root))
