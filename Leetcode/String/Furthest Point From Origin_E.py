class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        left,right,stop=0,0,0
        for item in moves:
            if item =="L":
                left+=1
            elif item=="R":
                right+=1
            else:
                stop+=1
        if left>right:
            return left-right+stop
        else:
            return right-left+stop
s=Solution()
moves = "L_RL__R"
print(s.furthestDistanceFromOrigin(moves))