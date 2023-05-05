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
    
    def bottomView(self, root):
        q=[[root,0,0]]
        res=[]
        map={}
        while q:
            node,depth,level=q.pop(0)
            res.append([node.val,depth,level])
            if node.left:
                q.append([node.left,depth+1,level-1])
            if node.right:
                q.append([node.right,depth+1,level+1])
        print(res)
        for item in res:
            if item[2] not in map:
                map[item[2]]=[item[0],item[1]]
            elif(map[item[2]][1]<item[1]):
                map[item[2]]=[item[0],item[1]]
            
        return [map[level][0] for level in sorted(map.keys())]
tree=BinaryTree(20)
n1=Node(8)
n2=Node(22)
n3=Node(5)
n4=Node(3)
n5=Node(10)
n6=Node(14)
n7=Node(25)
n8=Node(50)
tree.root.left=n1
tree.root.right=n2
n1.left=n3
n1.right=n4
n4.left=n5
n4.right=n6
n2.right=n7
print(tree.levelOrder(tree.root))
print(tree.bottomView(tree.root))


