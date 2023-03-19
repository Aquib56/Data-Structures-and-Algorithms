def maxArea(height):
    tempArea=0
    perArea=0
    i=0
    j=len(height)-1
    while(i<=j):
        if(height[i]>height[j]):
                tempArea=(height[j])*(j-i)
                j-=1
        else:
                tempArea=height[i]*(j-i)
                i+=1
        if(abs(tempArea)>abs(perArea)):
                perArea=abs(tempArea)              
    return(perArea)
if __name__=="__main__":
    height = [1,3,2,1,5,2]
    print(maxArea(height))