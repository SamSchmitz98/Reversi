#Sam Schmitz
#This program allows the users to play a game of reversi, and will keep track of the amount of games won for each player
def display_board(board, prompt, error):
    '''
    displays the current game board
    '''
    #blank space to make cleaner game space
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")    
    print("Scroll to top for rules!")
    print(error)
    print("    a   b   c   d   e   f   g   h  ")
    for c in range(8):
        print("  _________________________________")
        print(str(8-c)+" |", end='')
        for i in range(8):
            if board[c][i] == 0:
                print("   |", end='')
            elif board[c][i] == 1:
                print(" X |", end='')
            elif board[c][i] == 2:
                print(" 0 |", end='')
        print("")
    print("  _________________________________")
    print(prompt)

def read_move():
    '''
    Recieves and input and translates it to a list
    '''
    output = [-1, -1]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
    move = str(input())
    check = 0
    countl = 0
    countn = 0
    if len(move) != 2:
        return output
    for c in letters:
        if c == move[0]:
            output[1] = countl
            check += 1
        countl += 1
    for c in numbers:
        if c == move[1]:
            output[0] = countn
            check += 1
        countn += 1
    if check == 2:
        return output
    else:
        return [-1, -1]

def is_valid_move(board, player, position):
    '''
    tests the given position to see if it is a valid move
    '''
#sets player
    if player == 1:
        opplayer = 2
    elif player == 2:
        opplayer = 1
#accounts for error
    else:
        return False
    if position[0] == -1:
        return False
#checks if open
    if board[position[0]][position[1]] != 0:
        return False
#up
    if position[0] != 0 and board[position[0]-1][position[1]] == opplayer:
        for c in range(1, position[0]+1):
            if board[position[0]-c][position[1]] == player:
                return True
            if board[position[0]-c][position[1]] == 0:
                break
#down
    if position[0] != 7 and board[position[0]+1][position[1]] == opplayer:
        for c in range(1, 8-position[0]):
            if board[position[0]+c][position[1]] == player:
                return True
            if board[position[0]+c][position[1]] == 0:
                break
#left
    if position[1] != 0 and board[position[0]][position[1]-1] == opplayer:
        for c in range(1, position[1]+1):
            if board[position[0]][position[1]-c] == player:
                return True
            if board[position[0]][position[1]-c] == 0:
                break
#right
    if position[1] != 7 and board[position[0]][position[1]+1] == opplayer:
        for c in range(1, 8-position[1]):
            if board[position[0]][position[1]+c] == player:
                return True
            if board[position[0]][position[1]+c] == 0:
                break    
#ul
    if position[0] != 0 and position[1] != 0 and board[position[0]-1][position[1]-1] == opplayer:
 #closer to top
        if position[0] <= position[1]:
            for c in range(1, position[0]+1):
                if board[position[0]-c][position[1]-c] == player:
                    return True
                if board[position[0]-c][position[1]-c] == 0:
                    break
 #closer to left
        else:
            for c in range(1, position[1]+1):
                if board[position[0]-c][position[1]-c] == player:
                    return True
                if board[position[0]-c][position[1]-c] == 0:
                    break            
#ur
    if position[0] != 0 and position[1] != 7 and board[position[0]-1][position[1]+1] == opplayer:
 #closer to top
        if position[0] <= (8-position[1]):
            for c in range(1, position[0]+1):
                if board[position[0]-c][position[1]+c] == player:
                    return True
                if board[position[0]-c][position[1]+c] == 0:
                    break
 #closer to right
        else:
            for c in range(1, 8-position[1]):
                if board[position[0]-c][position[1]+c] == player:
                    return True
                if board[position[0]-c][position[1]+c] == 0:
                    break
#dl
    if position[0] != 7 and position[1] != 0 and board[position[0]+1][position[1]-1] == opplayer:
 #closer to bottom
        if (7-position[0]) <= position[1]:
            for c in range(1, 8-position[0]):
                if board[position[0]+c][position[1]-c] == player:
                    return True
                if board[position[0]+c][position[1]-c] == 0:
                    break
 #closer to left
        else:
            for c in range(1, position[1]+1):
                if board[position[0]+c][position[1]-c] == player:
                    return True
                if board[position[0]+c][position[1]-c] == 0:
                    break                
#dr
    if position[0] != 7 and position[1] != 7 and board[position[0]+1][position[1]+1] == opplayer:
 #closer to bottom
        if (7-position[0]) <= (7-position[1]):
            for c in range(1, 8-position[0]):
                if board[position[0]+c][position[1]+c] == player:
                    return True
                if board[position[0]+c][position[1]+c] == 0:
                    break
 #closer to right
        else:
            for c in range(1, 8-position[1]):
                if board[position[0]+c][position[1]+c] == player:
                    return True
                if board[position[0]+c][position[1]+c] == 0:
                    break
    return False

def flip_between(board, player, start, end):
    '''
    swaps the game pieces on a board between two given points
    '''
#vertical
    if start[1] == end[1]:
 #up
        if start[0] > end[0]:
            for c in range(start[0] - end[0]):
                board[start[0]-c][start[1]] = player
 #down
        else:
            for c in range(end[0] - start[0]):
                board[start[0]+c][start[1]] = player
#horizontal
    if start[0] == end[0]:
 #left
        if start[1] > end[1]:
            for c in range(start[1] - end[1]):
                board[start[0]][start[1]-c] = player
 #right
        else:
            for c in range(end[1] - start[1]):
                board[start[0]][start[1]+c] = player
#up diagonal
    if start[0] > end[0]:
 #ul
        if start[1] > end[1]:
            for c in range(start[1] - end[1]):
                board[start[0]-c][start[1]-c] = player
 #ur
        if start[1] < end[1]:
            for c in range(end[1] - start[1]):
                board[start[0]-c][start[1]+c] = player
#down diagonal
    if start[0] < end[0]:
 #dl
        if start[1] > end[1]:
            for c in range(start[1] - end[1]):
                board[start[0]+c][start[1]-c] = player
    #dr
        if start[1] < end[1]:
            for c in range(end[1] - start[1]):
                board[start[0]+c][start[1]+c] = player
    return board

def flip_all(board, player, position):
    '''
    uses the flip between function on all possible positions in the eight directions of a given point
    '''
#up
    for c in range(1, position[0]+1):
        if board[position[0]-c][position[1]] == 0:
            break
        if board[position[0]-c][position[1]] == player:
            flip_between(board, player, position, [position[0]-c, position[1]])
            break
#down
    for c in range(1, 8-position[0]):
        if board[position[0]+c][position[1]] == 0:
            break
        if board[position[0]+c][position[1]] == player:
            flip_between(board, player, position, [position[0]+c, position[1]])
            break
#left
    for c in range(1, position[1]+1):
        if board[position[0]][position[1]-c] == 0:
            break
        if board[position[0]][position[1]-c] == player:
            flip_between(board, player, position, [position[0], position[1]-c])
            break
#right
    for c in range(1, 8-position[1]):
        if board[position[0]][position[1]+c] == 0:
            break
        if board[position[0]][position[1]+c] == player:
            flip_between(board, player, position, [position[0], position[1]+c])
            break
#ul
 #closer to top
    if position[0] <= position[1]:
        for c in range(1, position[0]+1):
            if board[position[0]-c][position[1]-c] == 0:
                break
            if board[position[0]-c][position[1]-c] == player:
                flip_between(board, player, position, [position[0]-c, position[1]-c])
                break
 #closer to left
    else:
        for c in range(1, position[1]+1):
            if board[position[0]-c][position[1]-c] == 0:
                break
            if board[position[0]-c][position[1]-c] == player:
                flip_between(board, player, position, [position[0]-c, position[1]-c])
                break
#ur
 #closer to top
    if position[0] <= 7-position[1]:
        for c in range(1, position[0]+1):
            if board[position[0]-c][position[1]+c] == 0:
                break
            if board[position[0]-c][position[1]+c] == player:
                flip_between(board, player, position, [position[0]-c, position[1]+c])
                break
 #closer to right
    else:
        for c in range(1, 8-position[1]):
            if board[position[0]-c][position[1]+c] == 0:
                break
            if board[position[0]-c][position[1]+c] == player:
                flip_between(board, player, position, [position[0]-c, position[1]+c])
                break
#dl
 #closer to top
    if 7-position[0] <= position[1]:
        for c in range(1, 8-position[0]):
            if board[position[0]+c][position[1]-c] == 0:
                break
            if board[position[0]+c][position[1]-c] == player:
                flip_between(board, player, position, [position[0]+c, position[1]-c])
                break
 #closer to left
    else:
        for c in range(1, position[1]+1):
            if board[position[0]+c][position[1]-c] == 0:
                break
            if board[position[0]+c][position[1]-c] == player:
                flip_between(board, player, position, [position[0]+c, position[1]-c])
                break 
#dr
#closer to top
    if 7-position[0] <= 7-position[1]:
        for c in range(1, 8-position[0]):
            if board[position[0]+c][position[1]+c] == 0:
                break
            if board[position[0]+c][position[1]+c] == player:
                flip_between(board, player, position, [position[0]+c, position[1]+c])
                break
 #closer to right
    else:
        for c in range(1, 8-position[1]):
            if board[position[0]+c][position[1]+c] == 0:
                break
            if board[position[0]+c][position[1]+c] == player:
                flip_between(board, player, position, [position[0]+c, position[1]+c])
                break
    return board

def has_valid_move(board, player):
    '''
    checks the entire board to see if a player has any valid moves
    '''
    for c in range(8):
        for i in range(8):
            if is_valid_move(board, player, [c, i]) == True:
                return True
    return False

def tabulate_score(board):
    '''
    checks the board and returns a list off the current scores
    '''
    scores = [0, 0, 0]
    #When p1 is X
    if (wins[0] + wins[1] + wins[2]) % 2 == 0:
        for c in range(8):
            for i in range(8):
                scores[board[c][i]] += 1
    #When p2 is X
    else:
        for c in range(8):
            for i in range(8):
                if board[c][i] == 0:
                    scores[0] += 1
                elif board[c][i] == 1:
                    scores[2] += 1
                elif board[c][i] == 2:
                    scores[1] += 1
    return scores

def new_game(board):
    '''
    resets the board for a new game
    '''
    board = [[0, 0, 0, 0, 0, 0, 0, 0]for c in range(8)]
    board[4][4] = 1
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    return board

def end_game(board):
    '''
    ends the game and returns the winner
    '''
    scores = tabulate_score(board)
    if scores[1] > scores[2]:
        print("Congrats Player 1! You won " + str(scores[1]) + " to " + str(scores[2]) + "!")
        wins[1] += 1
    elif scores[2] > scores[1]:
        print("Congrats Player 2! You won " + str(scores[2]) + " to " + str(scores[1]) + "!")
        wins[2] += 1
    else:
        print("This game was a draw. The final score was " + str(scores[1]) + " to " + str(scores[2]) + ".")
        wins[0] += 1
    print("Player 1 has " + str(wins[1]) + " wins. Player 2 has " + str(wins[2]) + " wins. There have been " + str(wins[0]) + " draws.")
    return wins

def play_again():
    '''
    asks the user if they want to play again
    '''
    yn = input("Play again? y or n: ")
    if yn == "y":
        return True
    elif yn == "n":
        return False
    else:
        return play_again()

def p1turn():
    '''
    the process of the 1st players turn
    '''
    output = read_move()
    if is_valid_move(board, 1, output) == True:
        flip_all(board, 1, output)
        if has_valid_move(board, 2) == True:
            display_board(board, "Player 2(0), it is your turn:", "")
            p2turn()
        else:
            display_board(board, "Player 1(X), it is your turn:", "Player 2 has no moves, turn forfeited")
            if has_valid_move(board, 1) == True:
                p1turn()
    else:
        if output == [-1, -1]:
            display_board(board, "Player 1(X), try again:", "Invalid format: Must be 'letter''number'")
            p1turn()
        else:
            display_board(board, "Player 1(X), try again:", "Invalid move: Must result in opponent flipping")
            p1turn()            

def p2turn():
    '''
    the process of the second players turn
    '''
    output = read_move()
    if is_valid_move(board, 2, output) == True:
        flip_all(board, 2, output)
    else:
        if output == [-1, -1]:
            display_board(board, "Player 2(0), try again:", "Invalid format: Must be 'letter''number'")
            p2turn()
        else:
            display_board(board, "Player 2(0), try again:", "Invalid move: Must result in opponent flipping")
            p2turn() 
        
#flipped functions for switching "colors"
def p21turn():
    '''
    the process of the second player when playing with the X
    '''
    output = read_move()
    if is_valid_move(board, 1, output) == True:
        flip_all(board, 1, output)
        if has_valid_move(board, 2) == True:
            display_board(board, "Player 1(0), it is your turn:", "")
            p11turn()
        else:
            display_board(board, "Player 2(X), it is your turn:", "Player 1 has no moves, turn forfeited")
            if has_valid_move(board, 1) == True:
                p21turn()
    else:
        if output == [-1, -1]:
            display_board(board, "Player 2(X), try again:", "Invalid format: Must be 'letter''number'")
            p21turn()
        else:
            display_board(board, "Player 2(X), try again:", "Invalid move: Must result in opponent flipping")
            p21turn() 

def p11turn():
    '''
    the process of the first player when playing with the 0
    '''
    output = read_move()
    if is_valid_move(board, 2, output) == True:
        flip_all(board, 2, output)
    else:
        if output == [-1, -1]:
            display_board(board, "Player 1(0), try again:", "Invalid format: Must be 'letter''number'")
            p11turn()
        else:
            display_board(board, "Player 1(0), try again:", "Invalid move: Must result in opponent flipping")
            p11turn() 
'''
Actual Game
'''
wins = [0, 0, 0]
play_another_game = True
board = [[0, 0, 0, 0, 0, 0, 0, 0]for c in range(8)]
board[3][3] = 1
board[4][4] = 1
board[3][4] = 2
board[4][3] = 2

print("Welcome to Reversi!")
print("")
print("Rules:")
print("Player 1 = X")
print("Player 2 = 0")
print("X will always go first. Play begins")
print("by entering the coordinate of where")
print("each piece is wanted. It is entered")
print("as a letter followed by a number")
print("(e.g. a1 or f3). Whenever a player's")
print("piece is placed on both sides of an")
print("opponent's piece or row of pieces,")
print("said piece or row switches to the")
print("original player's shape. Each move")
print("must flip at least one piece. If a")
print("move cannot be made, the turn is")
print("forfeited. Play goes until no more")
print("moves can be made. The player with")
print("the most pieces wins. Players swap")
print("shapes each game.")
print("Good luck and have fun!")
print("")
print("Press enter to play!")
input()
while play_another_game == True:
    if (wins[0] + wins[1] + wins[2]) % 2 == 0:
        if has_valid_move(board, 1) == True:
            display_board(board, "Player 1(X), it is your turn:", "")
            p1turn()
        else:
            if has_valid_move(board, 2) == True:
                display_board(board, "Player 2(0), it is your turn:", "Player 1 has no moves, turn forfeited")
                p2turn()
            else:
                display_board(board, "", "")
                end_game(board)
                play_another_game = play_again()
                board = new_game(board)
    else:
        if has_valid_move(board, 1) == True:
            display_board(board, "Player 2(X), it is your turn:", "")
            p21turn()
        else:
            if has_valid_move(board, 2) == True:
                display_board(board, "Player 1(0), it is your turn:", "Player 2 has no moves, turn forfeited")
                p11turn()
            else:
                display_board(board, "", "")
                end_game(board)
                play_another_game = play_again()
                board = new_game(board)
print("Thanks for playing!")
input("Press 'enter' to close")
