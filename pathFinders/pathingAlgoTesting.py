import numpy as np
r = 0
board = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [9, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 9, 0, 0, 1]]

WIDTH = 6
HEIGHT = 6
 

    
dest = [5, 2]
start = [0, 1]   
def depthFirst(row, col, board, visited, limiter):
    
    for i in range(WIDTH):
        print(visited[i])
    print("================================================================")
    
    
    if np.array_equal(dest, [row, col]):
        print("found dest!")
        return
    
    
    if row < 0 or col < 0 or row > HEIGHT-1 or col > WIDTH-1 or board[row][col] == 1 or visited[row][col] :
        return
    
    visited[row][col] = True
    
    

    
    # up
    depthFirst(row-1, col, board, visited, limiter)
    # down

    depthFirst(row+1, col, board, visited, limiter)
    # left

    depthFirst(row, col-1, board, visited, limiter)
    # right

    depthFirst(row, col+1, board, visited, limiter)

    
   
       
    # base case

 
    # # up
    # if((board[row-1][col] == 1) and visited[row-1][col] == False):
    #     isNotIsland(row-1, col, board, visited)
    # # down
    # if((board[row+1][col] == 1) and visited[row+1][col] == False):
    #     isNotIsland(row+1, col, board, visited)
    # # left
    # if((board[row][col-1] == 1) and visited[row][col-1] == False):
    #     isNotIsland(row, col-1, board, visited)
    # # right
    # if((board[row][col+1] == 1) and visited[row][col+1] == False):
    #     isNotIsland(row, col+1, board, visited)
 
def main():
    limiter = 10
    # for row in range(0, len(output)):
    #     for col in range(0, len(output)):
    #         if isNotIsland(board[row][col], board):
    #             print()
   
    visited = [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],    
        [False, False, False, False, False, False],  
        [False, False, False, False, False, False],    
        [False, False, False, False, False, False],    
        [False, False, False, False, False, False]            
    ]
    # for i in range(0, 6):
    #     for j in range(0, 6):
    #         isNotIsland(i, j, board, visited)
    
    depthFirst(start[0], start[1], board, visited, limiter)
   
    
               
               
       
    print()
main()

