A=[[1,5,8],
   [6,9,0],
   [2,1,8]]
B=[[2,8,1],
   [9,7,4],
   [8,1,3]]
Result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])): # Row Wise Addition.
        Result[i][j]=A[i][j] + B[i][j] 
        print(Result)
        
for i in Result:
    print(i)

print(Result[1])
