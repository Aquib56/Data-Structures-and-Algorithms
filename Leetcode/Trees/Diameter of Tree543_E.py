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
    
    def diameterOfBinaryTree(self, root):
        res=[0]
        def helper(root):
            if not root:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            res[0]=max(res[0],left+right+2)

            return max(left,right)+1
        helper(root)
        return res[0]


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
# print(tree.levelOrder2(tree.root))
print(tree.diameterOfBinaryTree(tree.root))

