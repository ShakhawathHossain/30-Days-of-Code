n = int(input())
array = list(map(int, input().rstrip().split()))
array.reverse()
for num in array:
  print(num,end=" ")
