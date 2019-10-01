def hourglass(arr):
    max_sum = -9999
    Sum=0
    for i in range (0,4):

        for j in range (0,4):
            Sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

            if Sum>max_sum:
                max_sum=Sum
    return max_sum



arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

hourGlass_sum=hourglass(arr)

print(hourGlass_sum)
