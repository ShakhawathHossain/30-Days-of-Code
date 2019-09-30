num=int(input())
count=0
maximum=0

while num>0:
    if num % 2 == 1:
        count+=1

        if count>maximum:
            maximum=count

    else:
        count=0

    num=num//2

print(maximum)
