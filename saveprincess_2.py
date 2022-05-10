def nextMove(n,r,c,grid):
    princess = [0,0]
    m = [r, c]
    move = ""
    for line in range(0,n):
        for column in range(0,n):
            if (grid[line][column] == "p"):
                princess = [line, column]
    
    if(m[0] == princess[0]):
        if(m[1] > princess[1]):
            move = "LEFT"
        else:
            move = "RIGHT"
    else:
        if(m[0] > princess[0]):
            move = "UP"
        else:
            move = "DOWN"
    
    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))