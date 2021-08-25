board = [' ']
for x in range(10):
    board.append(' ')

def insertLetter(letter,pos):
    board[pos] = letter

def spaceisFree(pos):
    return board[pos] == ' '

def printBoard():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def isBoardFull(board):

  if board.count(' ') > 1:
      return False 
  else:
      return True

def playerMove():
   run = True
   while run:
       move = input("Plese insert a number between 1 and 9: ")
#try:
       move = int(move)
       if move > 0 and move < 10:
            if spaceisFree(move):
                run = False
                insertLetter('X', move)
            else:
                print("Space is occupied")
       else:
            print("Please insert a number between the range")
#except:
#    print("Please insert valid input")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0 
    
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i 
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7 ,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)

    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6 ,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("PC WON")

        if not(isWinner(board, 'X')):

            move = compMove()

            if move == 0:
                print("TIE")
            else:
                insertLetter("O", move)
                print("PC PLACE: " + str(move))
                printBoard()
        else:
            print("HAMON WOON!")


    if isBoardFull(board):
        print("TIE")
        
main()
