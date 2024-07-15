def GetMatrix(n, m, value):
    matrix = []
    List = []
    for i in range(n):
        matrix.append(List)
    for j in range(m):
        List.append(value)
    return matrix


result1 = GetMatrix(2, 2, 58)
result2 = GetMatrix(2, 5, 23)
result3 = GetMatrix(3, 2, 13)
print(result1)
print(result2)
print(result3)
