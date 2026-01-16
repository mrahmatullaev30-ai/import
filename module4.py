import os
os.system('cls')

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = []

for i in range(2): 
    result = []
    for j in range(2): 
        result.append(A[i][j] + B[i][j])
    C.append(result)

print("C = ", C)