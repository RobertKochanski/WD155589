A = [[1,2,3,4],
     [4,3,2,1],
     [2,3,4,1],
     [1,4,2,3]]

B = [A[i][i] for i in range(4)]

print(A)
print(B)