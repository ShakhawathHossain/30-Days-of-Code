n=int(input())
phoneBook={}
for i in range(0,n):
    name,number=input().split(" ")
    phoneBook[name]=number

for j in range(0,n):
    name=str(input())

    if name in phoneBook:
        print(name+'='+phoneBook[name])
    else:
        print('Not found')
