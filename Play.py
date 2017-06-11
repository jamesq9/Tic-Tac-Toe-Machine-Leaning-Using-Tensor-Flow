## Under Construciton

import numpy as np 

def new_board(size):
    board = np.full((size,size), ord('-') )
    return board

def displayBoard(board):
    rows, cols = board.shape
    print()
    print('   ' ,end=' ')
    for i in range(0,rows):
        print('{0}'.format(i),end=' ')
    print()
    for i in range(0,rows):
        print('{}   '.format(i) ,end='')
        for j in range(0, cols):
            print('{0}'.format( chr(board[i,j]) ) ,end=' ')
        print()
    print()

def place(pos,value,board):
    x,y = pos
    rows,cols = board.shape
    if(x >= rows or y >= cols ):
        return 0
    value = value.upper()
    actual_val = 0
    if value == 'X' or value == 'O':
        board[x,y] = ord(value)
    else:
        return 0
    
    return 1
        

if __name__ == "__main__":
    x = ['X','O','-']
    for i in x:
        print("{0} is {1}".format(i, ord(i)))
    board = new_board(3)
    place((4,2) , 'o' , board)
    displayBoard(board)

