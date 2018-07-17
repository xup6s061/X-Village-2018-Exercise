
# def eight_queens(matrix):
#     a=0
#     for i in range(0,8):
#         for j in range(0,8):
#             if i !=j:
#                 print(i,j)
#                 if matrix[i][0]==matrix[j][0]:
#                     a=1
#                     break
#                 elif matrix[i][1]==matrix[j][1]:
#                     a=1
#                     break
#                 for k in range(0,8):
#                     if (matrix[i][0]+k)==(matrix[j][0]) and (matrix[i][1]+k)==(matrix[j][1]):
#                         a=1
#                         break
#                     elif (matrix[i][0]+k)==(matrix[j][0]) and (matrix[i][1]-k)==(matrix[j][1]):
#                         a=1
#                         break
#     return a
# eight_queens([[0,0],[1,4],[2,7],[3,5],[4,2],[5,6],[6,1],[7,3]])
# print(a)


def caesar_cipher(st,num):
    an=st
    en=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,len(st)):
        for j in range(0,len(en)):
            if an[i]==en[j] and (i+num)<25:
                an[i]=en[j+num]
            elif an[i]==en[j] and (i+num)>25:
                an[i]=en[j+num-26]


caesar_cipher('xvillage',3)
