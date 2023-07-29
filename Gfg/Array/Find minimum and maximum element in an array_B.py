def getMinMax( a, n):
    max,min=a[0],a[0]
    for item in a:
        if item>=max:
            max=item
        if item<=min:
            min=item
    return max,min
arr=[3, 2, 1, 56, 10000, 167]
print(getMinMax(arr,5))