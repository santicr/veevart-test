from sys import stdin

def func(mat, row, col, num):
    ans = True

    for i in range(9):
        if mat[row][i] == num:
            ans = False
    
    for i in range(9):
        if mat[i][col] == num:
            ans = False

    nr = row - (row % 3)
    nc = col - (col % 3)

    for i in range(nr, nr + 3):
        for j in range(nc, nc + 3):
            if mat[i][j] == num:
                ans = False

    return ans

def solve(mat, i, j):
    if i >= 8 and j >= 8:
        for row in mat:
            print(row)
        print()

    elif j < 8:
        if mat[i][j] == 0:
            for num in range(10):
                if func(mat, i, j, num):
                    mat[i][j] = num
                    solve(mat, i, j + 1)
                    mat[i][j] = 0
        else:
            solve(mat, i, j + 1)

    elif j == 8:
        if mat[i][j] == 0:
            for num in range(10):
                if func(mat, i, j, num):
                    mat[i][j] = num
                    solve(mat, i + 1, 0)
                    mat[i][j] = 0
        else:
            solve(mat, i + 1, 0)

def main():
    global all_ans
    mat = []
    
    for _ in range(9):
        line = list(map(int, stdin.readline().strip().split()))
        mat.append(line)

    solve(mat, 0, 0)

main()