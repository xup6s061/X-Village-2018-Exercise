def eight_queens(matrix):
    a=True
    for i in range(0,8):
        for j in range(0,8):
            if i !=j:
                if matrix[i][0]==matrix[j][0]:
                    a=False
                elif matrix[i][1]==matrix[j][1]:
                    a=False
                for k in range(0,8):
                    if (matrix[i][0]+k)==(matrix[j][0]) and (matrix[i][1]+k)==(matrix[j][1]):
                        a=False
                    elif (matrix[i][0]+k)==(matrix[j][0]) and (matrix[i][1]-k)==(matrix[j][1]):
                        a=False
    print(a)
eight_queens([[0,0],[1,4],[2,7],[3,5],[4,2],[5,6],[6,1],[7,3]])