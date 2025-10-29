A=[[2,8,6],  # 3 x 3
   [7,12,5],
   [3,1,9]]

B=[[4,9,15,1], # 3 x 4
   [7,8,1,5],
   [10,6,2,3]]

Result=[[0,0,0,0], # 3 x 4
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(A)): # Will go inside A rows. 
    for j in range(len(B[0])): # Will go inside B columns.
        for k in range(len(B)): # A's columns and B's rows.  len(B) or len(A[0])
            Result[i][j] += A[i][k] * B[k][j]


for i in Result:

    print(i)







