T=int(input())
for i in range(0,T):
    S=str(input())

    even_string=''
    odd_string=''

    for j in range(0,len(S)):
        if j%2==0:
            even_string+=S[j]
        else :
             odd_string+=S[j]
    print(even_string,odd_string)
