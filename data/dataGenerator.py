import numpy as np 
import random
import time


mode = 'a'
myknownstates = {}

## Occupying a poistion [x,y] on the board is profitable
## if [x,y] is a position that occurs in the list of all winning sequences 
## more number of times

Profitable_Positions = [[3,2,3],
                        [2,4,2],
                        [3,2,3]]

def getRandomTurn():
    return random.choice([1,-1])

def getRandomPlace(board):
    row,col = board.shape
    empty_places = []
    for r in range(row):
        for c in range(col):
            if(board[r,c] == 0):
                empty_places.append(row * r + c)
    if len(empty_places) == 0:
        print(board)
    random_place = random.choice(empty_places)
    awesome_place = calculateReward(board,True)
    returnable_palce =  random.choice([random_place,awesome_place])
    return int(returnable_palce/3) , returnable_palce%3

def InverseBoard(board):
    temp_board = np.copy(board)
    rows, cols = temp_board.shape
    for r in range(rows):
        for c in range(cols):
            temp_board[r,c] *= -1
    return temp_board



def generateData(size=3):
    board = np.full((size,size), 0 )
    recursiveBaord(board,1)
    recursiveBaord(board,-1)
    

def recursiveBaord(board,turn):
    if(isGameOver(board)):
        return
    writeData(board,calculateReward(board))
    rows, cols = board.shape
    for r in range(rows):
        for c in range(cols):
            if board[r,c] == 0:
                board[r,c] = turn
                recursiveBaord(board , turn * -1)
                board[r,c] = 0

def writeData(board,rewards):
    temp_board = np.copy(board)
    temp_board = temp_board.reshape([-1])
    temp_board = temp_board.tolist()
    res = temp_board + rewards
    wline = " ".join(str(e) for e in res)
    if wline in myknownstates:
        return
    myknownstates[wline] = True



def calculateReward(board, returnPostion = False):
    win_reward = 100
    block_reward = 40
    fork_reward = 30
    block_fork_reward = 20
    extend_reward = 10 
    no_reward = 0
    negative_reward = -1
    rewards = [negative_reward] * 9
    rows , cols = board.shape
    ## MAIN LOGIC
    for r in range(rows):
        for c in range(cols):
            if board[r,c] == 0:
                row_sum = col_sum = left_dig_sum = right_dig_sum = 0
                row_sum = getRowSum(board, r)
                col_sum = getColSum(board, c) 
                if r - c == 0:
                    left_dig_sum = getLeftDig(board)
                if  c + r == rows - 1 :
                    right_dig_sum = getRightDig(board)
                index = rows * r + c
                rewards[index] = 0
                ## WIN REWARD CHECK
                if row_sum == 2: rewards[index] += win_reward
                if col_sum == 2: rewards[index] += win_reward
                if left_dig_sum == 2: rewards[index] += win_reward
                if right_dig_sum == 2: rewards[index] += win_reward
                
                ## BLOCK REWARD CHECK
                if row_sum == -2: rewards[index] += block_reward
                if col_sum == -2: rewards[index] += block_reward
                if left_dig_sum == -2: rewards[index] += win_reward
                if right_dig_sum == -2: rewards[index] += win_reward
                

                ## FORK REWARD CHECK
                temp = 0
                if row_sum == 1: temp += 1
                if col_sum == 1: temp += 1
                if left_dig_sum == 1: temp += 1
                if right_dig_sum == 1: temp += 1
                if temp >= 2:
                    rewards[index] += fork_reward
                
                ## BLOCK FORK REWARD CHECK
                temp = 0
                if row_sum == -1: temp += 1
                if col_sum == -1: temp += 1
                if left_dig_sum == -1: temp += 1
                if right_dig_sum == -1: temp += 1
                if temp >= 2:
                    rewards[index] += block_fork_reward
                
                ## Positional Reward
                rewards[index] += Profitable_Positions[r][c]
                
                ## Done
    max_reward = max(rewards)
    #print(rewards)
    indexs = []
    for index,value in enumerate(rewards):
        if value == max_reward: indexs.append(index)
    rewards = [0] * 9
    rewards[indexs[0]] = 1
    if returnPostion == True:
        return indexs[0]
    else:
        return rewards

def isGameOver(board):
    temp = None
    rows , cols = board.shape
    
    ## ROWS
    for i in range(rows):
        temp = getRowSum(board, i)
        if checkValue(temp):
            return True
    ## COLS
    for i in range(cols):
        temp = getColSum(board, i)
        if checkValue(temp):
            return True
    
    ## Diagonals
    temp = getRightDig(board)
    if checkValue(temp):
        return True
    
    temp = getLeftDig(board)
    if checkValue(temp):
        return True
    
    ## Does not contain empty places
    empty_place_exist = False
    for r in range(rows):
        for c in range(cols):
            if(board[r,c] == 0):
                empty_place_exist = True
    if not empty_place_exist:
        return True

    return False


def getRowSum(board , r):
    rows , cols = board.shape
    sum = 0
    for c in range(cols):
        sum = sum + board[r,c]
    return sum

def getColSum(board , c):
    rows , cols = board.shape
    sum = 0
    for r in range(rows):
        sum = sum + board[r,c]
    return sum

def getLeftDig(board):
    rows , cols = board.shape
    sum = 0
    for i in range(rows):
        sum = sum + board[i,i]
    return sum

def getRightDig(board):
    rows , cols = board.shape
    sum = 0
    i = rows - 1
    j = 0
    while i >= 0:
        sum += board[i,j]
        i = i - 1
        j = j + 1
    return sum

def checkValue(sum):
    if sum == -3 or sum == 3:
        return True





if __name__ == "__main__":
    # board = np.copy([   -1,0,1,
    #                     0,1,0,
    #                     0,0,0 ]).reshape(3,3)
    # print(board)
    # print(calculateReward(board))
    
    print("Started Generating Data")

    start_time = time.time()
    myknownstates = {}
    f_training = open("training.txt",mode)
    f_testing = open("test.txt",mode)
    generateData()
    print("Completed data generation ", len(myknownstates))
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print("preparing test and training data")
    for key in myknownstates:
        if random.choice([False,True,False,False,False,False,False,False]): # sleect to write in testing
            f_testing.write(key+"\n")
        f_training.write(key+"\n")
    f_testing.close()
    f_training.close()
    print("Done")
    

    # --- 1184.1137273311615 seconds ---
    # 4710