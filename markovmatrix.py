#WAP TO CHECK IF ALL THE ROWS AND ALL THE COLUMNS SUM TO 1, IF THEY DO, PRINT "IT IS A MARKOV MATRIX"

arr = []
c = 0

print("Enter the values of the matrix")

for i in range(4):
    temp = []
    for k in range(4):
        temp.append(float(input()))
    arr.append(temp)

for i in range(4):
    for k in range(4):
        print(arr[i][k], end = " ")
    print()


for i in range(4):
    if (arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3] == 1):
        if(arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i] == 1):
            c+=1

if(c == 4):
    print("It is a markov matrix")
else:
    print("It is not a markov matrix")