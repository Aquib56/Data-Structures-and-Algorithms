class Solution(object):
    def isValidBST(self, root):
        def helper(root,min=float("-inf"),max=float("inf")):
            if not root:
                return True
            if root.val <min or root.val>max:
                return False
            return helper(root.left,min,root.val-1) and helper(root.right,root.val+1,max)
        return helper(root)



