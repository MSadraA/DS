BLOCK = '#'

n , m = map(int, input().split())

matrix = []
row = []
col = [[0] for _ in range(m)]
for i in range(n):
    row_ = input()
    matrix.append(row_)
    row.append([0])
    
    for j in range(m):
        if(row_[j] == BLOCK):
            row[i] += [0]
            col[j] += [0]
            continue
        row[i][-1] += 1
        col[j][-1] += 1

max_points = 0
sum = 0
for i in range(n):
    for j in range(m):
        if(matrix[i][j] == BLOCK):
            row[i].pop(0)
            col[j].pop(0)
            continue
        sum = row[i][0] + col[j][0] - 1 
        if(sum > max_points):
            max_points = sum

print(max_points)

