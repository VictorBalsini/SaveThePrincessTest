def displayPathtoPrincess(n,grid):
    moves = ''
    princess = [0,0]
    for line in range(0,n):
        for column in range(0,n):
            if (grid[line][column] == "p"):
                princess = [line, column]
    
    m = [int((n-1)/2), int((n-1)/2)]
    for l in range(0,abs(m[0] - princess[0])):
        if (m[0] > princess[0]):
            moves += "UP\n"
        elif(m[0] < princess[0]):
            moves += "DOWN\n"
            
    for c in range(0,abs(m[1] - princess[1])):
        if (m[1] > princess[1]):
            moves += "LEFT\n"
        elif(m[1] < princess[1]):
            moves += "RIGHT\n"
    
    print(moves)
            
            
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)