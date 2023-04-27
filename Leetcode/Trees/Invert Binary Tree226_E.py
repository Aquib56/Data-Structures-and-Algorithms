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

    def invertTree(self, root):
        if not root:
            return 
        a=root.left
        root.left=root.right
        root.right=a
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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
tree.levelOrder(tree.root)
tree.levelOrder(tree.invertTree(tree.root))