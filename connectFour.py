
import random
class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self,height,width):
        '''constructs a board object with height and width'''
        self.height=height
        self.width=width
        self.slots = [[' '] * self.width for row in range(self.height)]
        

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string
        
        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        s+=((self.width*2)+1)*'-'
        s+='\n'
        for i in range(self.width):
            s+= ' '+ str(i%10)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row=0
        while self.slots[row][col]==' ' and row <self.height-1:
            row+=1
        if self.slots[row][col] in 'XO':
            row-=1
        self.slots[row][col]=checker
            

    def reset(self):
        '''resets the board so it is now empty'''
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    
    def can_add_to(self,col):
        '''returns true if it is a valid place to place a checker in col and false 
        otherwise'''
        if col<0 or col>self.width-1:
            return False
        elif self.slots[0][col] in 'XO':
            return False
        else:
            return True
    
    def is_full(self):
        '''checks to see if board is full, returing true if full 
        and false otherwise'''
        for i in range(self.width):
            can_add= self.can_add_to(i)
            if can_add==True:
                return False
        return True
    
    def remove_checker(self,col):
        '''removes the top checker from the col, unless it is empty
        then the method does nothing'''
        row=0
        while self.slots[row][col]==' ' and row <self.height-1:
            row+=1
        self.slots[row][col]=" "
        
        
    def is_up_diagonal_win(self,checker):
        """ Checks for an up diagonal win for the specified checker.
        """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False
                
        
    def is_down_diagonal_win(self,checker):
        """ Checks for a down diagnoal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
        
    def is_vertical_win(self,checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        # if we make it here, there were no horizontal wins
        return False
    
    
    def is_win_for(self, checker):
        """ checks to see if there is a win on the current board
        by checking diagonally veritically and horizontally
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker):
           
            return True
        elif self.is_vertical_win(checker):
            
            return True
        elif self.is_down_diagonal_win(checker):
            
            return True
        elif self.is_up_diagonal_win(checker):
            
            return True
        else:
            return False
    
    def make_board(self):
        self.add_checkers('34334565665')
        self.add_checker('O',0)
        self.add_checkers('050005022223332')
        self.add_checker('O',5)

class Player:
    def __init__(self,checker):
        '''constructs a player object'''
        assert(checker == 'X' or checker == 'O')
        self.checker=checker
        self.num_moves=0
    
    def __repr__(self):
        '''returns a string that represents a player object and which
        checker the player is using'''
        return "Player "+ self.checker
    
    def opponent_checker(self):
        '''returns a string that represents the checker
        of the players opponent'''
        if self.checker=='X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self,b):
        '''gets move from player and determines if the
        move is valid and returns the valid column if 
        invalid it keeps asking'''
        self.num_moves+=1
        while True:
            col=int(input('Enter a column: '))
            if b.can_add_to(col):
                return col
            else:
                print("Try again!")
                
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p,b):
    '''takes in board and a player and performs the steps
    needed for a single move by player p'''
    print('Player',p.checker,'\'s turn' )
    n_move=p.next_move(b)
    b.add_checker(p.checker,n_move)
    print()
    print(b)
    p_win=b.is_win_for(p.checker)
    if p_win:
        print( p, 'wins in ', p.num_moves, ' moves.')
        print("Congratulations!")
        return True
    elif b.is_full():
        print('It\'s a tie!')
        return True
    else:
        return False
    
class RandomPlayer(Player):
    ''' an unintelligent computer player that chooses from columns at
    random'''
    def next_move(self,b):
        '''chooses new column at random from the avalible
        columns and returns the index of that column'''
        aval_col=[x for x in range(b.width) if b.can_add_to(x)]
        self.num_moves+=1
        col= random.choice(aval_col)
        return col


class AIPlayer(Player):
    '''an intelligent computer player that uses techniques from AI to choose its next move'''
    
    def __init__(self,checker,tiebreak,lookahead):
        '''adds two new attributes, tiebreak and lookahead, to AI player in 
        addition to the one defined by the player class
        checker'''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak=tiebreak
        self.lookahead=lookahead
    
    def __repr__(self):
        '''returns a string representing an AI player object'''
        return 'Player '+ self.checker+ ' ('+ self.tiebreak+', '+ str(self.lookahead)+ ')'
    
    def max_score_column(self,scores):
        '''takes a list of scores for each column and returns the index with max score'''
        max_score=max(scores)
        index_max=[]
        for i in range(len(scores)):
            if max_score==scores[i]:
                index_max+=[i]
        if self.tiebreak=='RIGHT':
            return index_max[-1]
        elif self.tiebreak=='LEFT':
            return index_max[0]
        else:
            return random.choice(index_max)
        
    def scores_for(self,b):
        '''takes in board b and determines the AIplayer scores 
        for the columns in b'''
        amt_col=b.width
        scores=[0]*amt_col
        for col in range(b.width):
            if b.can_add_to(col)==False:
                scores[col]=-1
            elif b.is_win_for(self.checker):
                scores[col]=100
            elif b.is_win_for(self.opponent_checker()):
                scores[col]=0
            elif self.lookahead==0:
                scores[col]=50   
            else:
                b.add_checker(self.checker,col)
                opponent=AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
                opp_scores=opponent.scores_for(b)
                if max(opp_scores)==100:
                    scores[col]=0
                elif max(opp_scores)==0:
                    scores[col]=100
                elif opp_scores[col]==-1:
                    scores[col]=50
                else:
                    scores[col]=50
                b.remove_checker(col)
        return scores
    
    def next_move(self,b):
        '''returns the AI players judgement of its next 
        best move'''
        self.num_moves+=1
        return self.max_score_column(self.scores_for(b))
        
                
# Start Game of Player VS Computer with lookahead of 3
X = Player("X")
Y = AIPlayer("O", "RANDOM", 3) 

# Start Game of Player vs Player 
# Y = Player("O")


connect_four(X,Y)    
    
    
        
            
     


        
        
        


        
            
        
        
        