mat = [[5,1,1,20],
        [1,3,30,1],
        [1,40,2,1],
        [50,1,1,6]]
mat2 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(mat)
class Solution(object):
    def diagonalSum(self, mat): 
        sum=0
        for i in range(len(mat)):
            j=i
            sum+=mat[i][j]
        print(sum)
        for i in range(len(mat)-1,-1,-1):
            j=(len(mat)-1)-i
            if i==j:
                continue
            print(mat[i][j])
            sum+=mat[i][j]
        
        return sum
s1=Solution()
print(s1.diagonalSum(mat2))
