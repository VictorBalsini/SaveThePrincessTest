def nextMove(n,r,c,grid):
    princess_position = getPrincessPosition(grid)
    m_position = {'row':r , 'col':c}
    
    next_move = ""    

    if(m_position['row'] == princess_position['row']):
        if(m_position['col'] > princess_position['col']):
            next_move = "LEFT"
        else:
            next_move = "RIGHT"
    else:
        if(m_position['row'] > princess_position['row']):
            next_move = "UP"
        else:
            next_move = "DOWN"
    
    return next_move

def getPrincessPosition(grid):
    pos = {'row':0 , 'col':0}
    for row in range(0, len(grid)):                 #Search 'p' on grid
        if ('p' in grid[row]):                      # found 'p' row
            pos['row'] = row
            pos['col'] = grid[row].find('p')        # get 'p' column
    
    return pos    
    
#------------------------------------------------------------------------------------------
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
