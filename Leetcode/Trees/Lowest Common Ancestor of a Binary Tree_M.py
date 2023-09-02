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
                    
    def lowestCommonAncestor(self, root, p, q):
        Ap,Aq=[],[]
        def dfs(root,p,q,track):
            if not root:
                return
            if root.val==p:
                Ap.extend(track)
                Ap.append(root.val)
                
            if root.val==q:
                Aq.extend(track)
                Aq.append(root.val)
                
            track.append(root.val)
            dfs(root.left,p,q,track)
            dfs(root.right,p,q,track)
            track.remove(root.val)
        dfs(root,p,q,[])
        print(Ap,Aq)
        for i in range(len(Aq)-1,-1 ,-1):
            
            if Aq[i] in Ap:
                return Aq[i]
    def path(self,root,p,track):
        if not root:
            return
        if root.val==p:
            print(track)
            return 
        track.append(root.val)
        self.path(root.left,p,track)
        self.path(root.right,p,track)
        track.remove(root.val)
    def lowestCommonAncestor_better(self, root, p, q):
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor_better(root.left,p,q)
        right=self.lowestCommonAncestor_better(root.right,p,q)
        if left:
            print(left.val)
        if right:
            print(right.val)
        if not left:
            return right
        if not right:
            return left
        else:
            return root
        

# tree=BinaryTree(1)
# n1=Node(2)
# n2=Node(3)
# n3=Node(4)
# n4=Node(5)
# n5=Node(6)


# tree.root.left=n1
# tree.root.right=n2
# n1.left=n3
# n1.right=n4
# n2.right=n5
tree = BinaryTree(3)
n1 = Node(5)
n2 = Node(1)
n3 = Node(6)
n4 = Node(2)
n5 = Node(0)
n6 = Node(8)
n7 = Node(7)
n8 = Node(4)

# Build the tree structure
tree.root.left = n1
tree.root.right = n2
n1.left = n3
n1.right = n4
n2.right = n6
n4.left = n5
n4.right = n7
n5.left = n8
# tree.levelOrder(tree.root)
r=tree.lowestCommonAncestor_better(tree.root,n1,n8)
print(r.val)
# print(tree.path(tree.root,6,[]))