def divisors(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum
def funct(N):
    res=0
    for i in range(1,N+1):
        res+=divisors(i)
    return res
print(funct(4))