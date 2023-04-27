class Solution:
    
    def height(self,root):
        if not root:
            return 0
        leftHeight=self.height(root.left)
        rightHeight=self.height(root.right)
        return max(leftHeight,rightHeight) +1
        
    def diameter(self,root):
        if not root:
            return 0
        leftHeight=self.height(root.left)
        rightHeight=self.height(root.right)
        return max(leftHeight+rightHeight +1,self.diameter(root.left),self.diameter(root.right))