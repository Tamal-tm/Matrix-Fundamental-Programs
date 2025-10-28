A=[[1,2,3,],[4,5,6]]
T=[[0,0],[0,0],[0,0]]

for i in range(len(A)): # First rows into colums then columns into rows
    for j in range(len(A[0])): # Columns
            print("Rows:",i) # For understanding
            print("Columns",j)
            T[j][i]=A[i][j]
for i in T:
      print(i)

print("\n")

# Using List Comprehension

A=[[1,2,3,],[4,5,6]]

T=[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

for i in T:
      print(i)