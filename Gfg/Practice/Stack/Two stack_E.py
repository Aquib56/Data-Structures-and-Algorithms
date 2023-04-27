class Twostack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*self.size
        self.top1=-1
        self.top2=self.size

    def push1(self,val):
        self.top1+=1
        self.arr[self.top1]=val

    def push2(self,val):
        self.top2-=1
        self.arr[self.top2]=val
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.arr.remove(x)
            return x
        else:
            print("Stack1 is empty")

    def pop2(self):
        if self.top<=self.size:
            x=self.arr[self.top2]
            self.arr.remove(x)
            self.top1+=1
            return x
        else:
            print("Stack1 is empty")

s1=Twostack(10)
s1.push1(5)
s1.push1(6)
s1.push2(1)
s1.push2(2)
s1.pop1()
print(s1.arr)    
