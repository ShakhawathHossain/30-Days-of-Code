def factorial(n):
    if(n==1):
        n=1
    else:
        n=n*factorial(n-1)
    return n


n = int(input())
result = factorial(n)
print(result)
