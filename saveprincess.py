def displayPathtoPrincess(n,grid):
    border_to_center = int((n-1)/2) #get the center of the grid
    
    col_move = "RIGHT\n"
    row_move = "DOWN\n"
    moves_list = ""
    
    princess_on_first_row = (grid[0].find('p') != -1)   # Check for 'p' on first row
    princess_on_first_column = False
    
    if (princess_on_first_row):
        row_move = "UP\n"
        princess_on_first_column = (grid[0][0]=='p')    # Check for 'p' on first column of first row
    else:
        princess_on_first_column = (grid[n-1][0]=='p')  # Check for 'p' on first column of last row
    
    if (princess_on_first_column):
        col_move = "LEFT\n"
    
    moves_list = (row_move + col_move) * border_to_center
        
    print(moves_list)

#---------------------------------------------------------------------------------------

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)