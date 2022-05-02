def print_board(board):
    c = 0
    for i in range(3):
        for j in range(3):
            if board[c] == 2:
                print("_", end=" ")
            elif board[c] == 3:
                print("X", end=" ")
            else:
                print("O", end=" ")
            c += 1
        print()
    
def BestMove(board):
    bestscore = 1000
    for i in range(len(board)):
        if board[i] == 2:
            board[i] = 5
            score = minimax(board, 0, True)
            if score < bestscore:
                bestscore = score
                bestmove = i
            board[i]=2
    return bestmove

def product(lst, board):
    pro = 1
    for i in lst:
        pro = pro * board[i]
    return pro

def wincheck(board):
    for i in all_possibilities:
        x = product(i, board)
        if x == 125:
            return 5
        elif x == 27:
            return 3
    for i in range(len(board)):
        if board[i]==2:
            return 0
    return -1
    

def minimax(board, depth, isMaximizing):
    is_win = wincheck(board)
    if is_win==5:
        return -10
    elif is_win == 3:
        return 10
    elif is_win==-1:
        return 0
    if isMaximizing:     
        bestscore = -1000
        for i in range(len(board)):
            if board[i] == 2:
                board[i] = 3
                score = minimax(board, depth+1, False)
                bestscore = max(score, bestscore)
                board[i] = 2
        return bestscore
    else:
        # is_win = wincheck(board)
        # if is_win==5:
        #     return -10
        # elif is_win == 3:
        #     return 10
        # elif is_win == -1:
        #     return 0
        bestscore = 1000
        for i in range(len(board)):
            if board[i] == 2:
                board[i] = 5
                score = minimax(board, depth+1, True)
                bestscore = min(score, bestscore)
                board[i] = 2
        return bestscore
            

board = [2]*9
row1 = [0, 1, 2]
row2 = [3, 4, 5]
row3 = [6, 7, 8]
col1 = [0, 3, 6]
col2 = [1, 4, 7]
col3 = [2, 5, 8]
diag1 = [0, 4, 8]
diag2 = [2, 4, 6]
all_possibilities = [row1, row2, row3, col1, col2, col3, diag1, diag2]
print("Welcome to the AI powered TIC TAC TOE Game")
print_board(board)
for i in range(9):
    if i%2==0:
        print("Players Turn")
        player_turn = int(input("Select the position in the board: "))
        while board[player_turn-1] != 2:
            print("Place already filled")
            player_turn = int(input("Select the position in the board: "))
        board[player_turn-1] = 3
        print_board(board)
        is_win = wincheck(board)
        if is_win == 3:
            print("Player Won")
            break
        elif is_win == -1:
            print("Draw")
            break
    else:
        print("Computer's Turn")
        bestmove = BestMove(board)
        board[bestmove] = 5
        print_board(board)
        is_win = wincheck(board)
        if is_win == 5:
            print("Computer Won")
            break
        elif is_win == -1:
            print("Draw")
            break