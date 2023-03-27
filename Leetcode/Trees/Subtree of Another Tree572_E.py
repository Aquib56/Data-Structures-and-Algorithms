class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot:return True
        if not root: return False
        if self.sametree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
    def sametree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val==subRoot.val:
            return self.sametree(root.left,subRoot.left) and self.sametree(root.right,subRoot.right)
        return False