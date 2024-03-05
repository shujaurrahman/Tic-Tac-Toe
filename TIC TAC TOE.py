import random
'''---------------------------------------------------------------'''
'''Function prints out a boards with numpad as ref.'''
def display_board(board):
    #print board
    print(board[1]+"     | "  +board[2]+" | "  +board[3])
    print('      |   |           ')
    print("-----------------")
    print(board[4]+"     | "  +board[5]+" | "  +board[6])
    print('      |   |           ')
    print("-----------------")
    print(board[7]+"     | "  +board[8]+" | "  +board[9])
    print('      |   |          ')

'''Function for Number position to give ref. to both players
    i.e Number represent positon'''
def ref_board():
    #For player ref.
    print()
    print('\t\t READ THE INSTRUCTION AND MEMORIZE POSITIONS SPECIFIED IN THE REF. BOARD')
    print('\t Number Which player needs to enter(or remember for certain position) \n \t\t To Input their initial at desired Position.')
    print()
    print('\t    1. At First player needs to choose thier intial i.e either (X or O).')
    print('\t    2. First chance will be alloted to any of the player randomly.')
    print('\t    3. Chance is Given to both player one by one.')
    print('\t    4. Chance is in Sequential Order I.E One after the other.')
    print('\t    5. Only One Chance is Given to every of two player not more than that.')
    print()
    print('BOARD FOR PLAYERS REFERANCE' )
    print("  1  |  2 |  3" )
    print('     |    |           ')
    print("-----------------")
    print("  4  |  5 |  6")
    print('     |    |           ')
    print("-----------------")
    print("  7  |  8 |  9")
    print('     |    |          ')
    print()
    print("\t\t\t NOW LETS'S PLAY THE GMAE")

'''Function For Input from user of TIC TAC TOE Intials I.E 'X' or 'O' '''

def player_input():
    marker=''
    while not (marker == 'X' or marker == 'O'):
        print()
        print()
        marker=input("Player 1, Coose X or O: ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

'''Function to put intial at right place where user desired '''   
def place_marker(board,marker,position):
    board[position]=marker

''' Function to define Game winning Condition to declare which player is won'''    
def win_check(board,mark):
    '''check horizontal,vertical,and Diagonals for a win'''
    if (board[1]==board[2]==board[3]== mark) or \
       (board[4]==board[5]==board[6]== mark) or \
       (board[7]==board[8]==board[9]== mark) or \
       (board[1]==board[4]==board[7]== mark) or \
       (board[2]==board[5]==board[8]== mark) or \
       (board[3]==board[6]==board[9]== mark) or \
       (board[1]==board[5]==board[9]== mark) or \
       (board[3]==board[5]==board[7]== mark):
        return True
    else:
        return False

'''Function to choose randomly that which player should Go First'''
def choose_first():
    flip=random.randint(0,1)

    if flip==0:
        return 'Player 1 '
    else:
        return 'Player 2 '

'''Function for defining blank position on the board'''
def space_check(board,position):
   return board[position]==' '


'''Function to check that in board no position is left blank each has to be filled with intials of the players
                               BY MAKING USE OF SPACE CHECK FUNCTION '''
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

'''Function to ask player choice to input number of position as given in ref board so that initial can
                          be located at that Position.'''
def player_choice(board):
    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        print()
        print('\n'*20)
        position=int(input("Choose a Position (1-9): "))
    return position

'''Function for asking from user whether they want to play again'''

def replay():
    print('ENJOYED! While Playing this game.')
    print("Want to play again")
    print('If Yes type (Yes) ')
    choice=input("Play again? Enter Yes or No:: ").lower()

    if (choice=='yes'):
        return replay_game()
    
        
'''____________________________________________________________________________________'''
#########################################################################################
'''------------------------------------------------------------------------------------'''
#Main code

#while Loop to keep running the game
def game_play():
    print("Welcome to TIC TAC TOE")
    print('GAME CODED BY::: SHUJA UR RAHMAN')
    print()
    print(ref_board())
    while True:
        #Play the Game
        ##set Everything up (Board,whos first,choose marker X,O)
        the_board=[' ']*10
        (player1_marker,player2_marker)=player_input()
        ##choose turn
        print()
        print()
        turn=choose_first()
        print()
        print(turn+ "WILL GO FIRST!!")
        print()
        print(turn+ 'WILL TAKE FIRST CHANCE!!!')
        print(turn+ 'TYPE Y TO CONTINUE')
        print()
        play_game=input('Ready to Play? Y or N :: ').lower()
        if play_game=='y':
            game_on =True
        else:
            game_on=False
        while game_on:
            ##player one turn
            if turn=='Player 1':
                #show empty Board
                display_board(the_board)
                print(turn + 'NEEDS TO ENTER DESIRED POSITION NUMBER ')
                #choose a position
                position=player_choice(the_board)
                #place the marker on the position
                place_marker(the_board,player1_marker,position)
                #check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print()
                    print()
                    print()
                    print('HURRAYYYYYYYYYYYY!!!!!!!!!!  PLAYER 1 HAS WON!!')
                    print('WELL PLAYED!')
                    print()
                    game_on=False
                else:
                    #or check if there is a tie
                    if full_board_check(the_board):
                        display_board(the_board)
                        print()
                        print()
                        print()
                        print('GAME TIE!!')
                        print('BRAINYY PLAYERS!! WELL PLAYED GAME BY BOTH PLAYERS')
                        print()
                        game_on=False
                        #No tie And no one ? then next player's turn
                    else:
                        turn ='Player 2'
            else:
                #show empty Board
                display_board(the_board)
                #choose a position
                position=player_choice(the_board)
                #place the marker on the position
                place_marker(the_board,player2_marker,position)
                #check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print()
                    print()
                    print()
                    print('HURRAYYYYYYYYYYYY!!!!!!!!!!   PLAYER 2 HAS WON!!')
                    print('WELL PLAYED!')
                    print()
                    game_on=False
                else:
                    #or check if there is a tie
                    if full_board_check(the_board):
                        display_board(the_board)
                        print()
                        print()
                        print()
                        print('GAME TIE!!')
                        print('BRAINYY PLAYERS!! WELL PLAYED GAME BY BOTH PLAYERS')
                        print()
                        game_on=False
                        #No tie And no one ? then next player's turn
                    else:
                        turn='Player 1'
        if not replay():
            break
        #Breaks out of the loop if not taken yes option at replay() function
#--------------------------------------------------------------------------------#

'''Function for replay'''
def replay_game():
    print('\n'*30)
    print('\t\t WELCOME AGAIN PLAYERS,\n\t\t ENJOYING GAME LETS GO FOR ANOTHER!!!! HURRRAYYYYY ')
    print()
    print("\t\t Ready to play Again! Hold your breath down we are going to begin..")
    print()
    print('\n'*26)
    while True:
        #Play the Game
        ##set Everything up (Board,whos first,choose marker X,O)
        the_board=[' ']*10
        (player1_marker,player2_marker)=player_input()
        ##choose turn
        print()
        print()
        turn=choose_first()
        print()
        print(turn+ "WILL GO FIRST!!")
        print()
        print(turn+ 'WILL TAKE FIRST CHANCE!!!')
        print(turn+ 'TYPE Y TO CONTINUE')
        print()
        play_game=input('Ready to Play? Y or N :: ').lower()
        if play_game=='y':
            game_on =True
        else:
            game_on=False
        while game_on:
            ##player one turn
            if turn=='Player 1':
                #show empty Board
                display_board(the_board)
                print(turn + 'NEEDS TO ENTER DESIRED POSITION NUMBER ')
                #choose a position
                position=player_choice(the_board)
                #place the marker on the position
                place_marker(the_board,player1_marker,position)
                #check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print()
                    print()
                    print()
                    print('HURRAYYYYYYYYYYYY!!!!!!!!!!  PLAYER 1 HAS WON!!')
                    print('WELL PLAYED!')
                    print()
                    game_on=False
                else:
                    #or check if there is a tie
                    if full_board_check(the_board):
                        display_board(the_board)
                        print()
                        print()
                        print()
                        print('GAME TIE!!')
                        print('BRAINYY PLAYERS!! WELL PLAYED GAME BY BOTH PLAYERS')
                        print()
                        game_on=False
                        #No tie And no one ? then next player's turn
                    else:
                        turn ='Player 2'
            else:
                #show empty Board
                display_board(the_board)
                #choose a position
                position=player_choice(the_board)
                #place the marker on the position
                place_marker(the_board,player2_marker,position)
                #check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print()
                    print()
                    print()
                    print('HURRAYYYYYYYYYYYY!!!!!!!!!!   PLAYER 2 HAS WON!!')
                    print('WELL PLAYED!')
                    print()
                    game_on=False
                else:
                    #or check if there is a tie
                    if full_board_check(the_board):
                        display_board(the_board)
                        print()
                        print()
                        print()
                        print('GAME TIE!!')
                        print('BRAINYY PLAYERS!! WELL PLAYED GAME BY BOTH PLAYERS')
                        print()
                        game_on=False
                        #No tie And no one ? then next player's turn
                    else:
                        turn='Player 1'
        if not replay():
            break
        #Breaks out of the loop if not taken yes option at replay() function


'''Running the game by calling Games Main Function'''



#---------------------------------------------------#
print()
print()
print('\t\t\t\t HELLO, Players!')
print()
print()
print('\t To play -TIC TAC TOE- game Press any numbers on numberpad')
numpad_possibilities=[0,1,2,3,4,5,6,7,8,9]
ent_choice=int(input('\t Enter any Number:: '))
while ent_choice in numpad_possibilities:
    print()
    print(game_play())
#----------------------------------------------------#


'''TIC TAC TOE GAME CODED BY SHUJA UR RAHMAN'''
''' REF AND HELP TAKEN BY UDEMY LEC.'''
 
