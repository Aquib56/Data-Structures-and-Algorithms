import test
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        res=[]
        maxdepth=[0]
        def helper(root,depth):
            if not root:
                return
            if depth>maxdepth[0]:
                res.append(root.val)
                maxdepth[0]=depth
            helper(root.right,depth+1)
            helper(root.left,depth+1)
        helper(root,1)
        return res
a=Solution()
b=test.BinaryTree(1)
b.levelOrder(b.root)
print(a.rightView(b.root))