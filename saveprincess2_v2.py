#solution with less if statements
def nextMove(n,r,c,grid):
    princess_position = getPrincessPosition(grid)
    m_position = {'row':r , 'col':c}
    
    col_moves = ['', 'LEFT', 'RIGHT'] 
    row_moves = ['', 'UP', 'DOWN']
    next_move = ""
        
    if(m_position['row'] == princess_position['row']):
        next_move = col_moves[getIndex(m_position['col'], princess_position['col'])]
    else:
        next_move = row_moves[getIndex(m_position['row'], princess_position['row'])]
        
    return next_move

def getPrincessPosition(grid):
    pos = {'row':0 , 'col':0}
    for row in range(0, len(grid)):                 #Search 'p' on grid
        if ('p' in grid[row]):                      # found 'p' row
            pos['row'] = row
            pos['col'] = grid[row].find('p')        # get 'p' column
    return pos

def getIndex(m, p): 
    #if m > p return 1, else return -1
    diference = m - p
    index = int((diference/abs(diference))) 
    return index
        
#------------------------------------------------------------------------------------------
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))