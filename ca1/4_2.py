import sys
BLOCK = '#'

max_points = 0

n , m = map(int, input().split())
matrix = [input() for _ in range(n)]

def points_per_rows(matrix):
    counter = 0
    l = []
    tmp = []
    for i in matrix:
        for j in i:
            if (j == BLOCK):
                tmp.append(counter)
                counter = 0
                continue
            counter += 1
        tmp.append(counter)
        l.append(tmp)
        tmp = []
        counter = 0
    return l

def points_per_columns(matrix):
    counter = 0
    l = []
    tmp = []
    for i in range(m):
        for j in range(n):
            if (matrix[j][i] == BLOCK):
                tmp.append(counter)
                counter = 0
                continue
            counter += 1
        tmp.append(counter)
        l.append(tmp)
        tmp = []
        counter = 0
    return l

row = points_per_rows(matrix)
col = points_per_columns(matrix)

def find_max_points(row , col , matrix):
    max_points = 0
    sum = 0

    col_index = [0]*m
    row_index = 0

    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == BLOCK):
                row_index += 1
                col_index[j] += 1
                continue
            sum = row[i][row_index] + col[j][col_index[j]] - 1 
            if(sum > max_points):
                max_points = sum
        row_index = 0
    return max_points

print(find_max_points(row , col , matrix))
