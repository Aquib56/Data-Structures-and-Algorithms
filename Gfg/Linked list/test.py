n=24
count=0
for item in str(n):
    print(type(item),item)
    if n%(int(item)):
        count+=1
print(count)