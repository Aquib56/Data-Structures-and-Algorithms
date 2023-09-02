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

    def tree_width(self,root):
        if not root:
            return 0
        
        max_width = 0
        queue = [(root, 0)]
        
        while queue:
            level_size = len(queue)
            _, first_index = queue[0]  
            for _ in range(level_size):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            
            level_width = index - first_index + 1
            max_width = max(max_width, level_width)
        
        return max_width
                    
        

tree=BinaryTree(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
n5=Node(6)


tree.root.left=n1
tree.root.right=n2
n1.left=n3
# n1.right=n4
n2.right=n5
tree.levelOrder(tree.root)
print(tree.tree_width(tree.root))