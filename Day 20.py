n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwap=0

for i in range(0,n):
    for j in range(0,n-1-i):
        if(a[j]>a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                numSwap+=1
    if(numSwap==0):
        break
print("Array is sorted in",numSwap,"swaps.")
print("First Element:", a[0])
print("Last Element:", a[n-1])
