

class board():
    
    def __init__(self, b = None):
        if b == None:
            pass
        else:
            self.create_board(b)

        return

    def create_board(self, b) -> None:
        game_board = [[] for _ in range(9)]
        index = 0
        for i in b:
            if i == "/":
                index += 1
            elif i == "-":
                game_board[index].append(0)
            else:
                game_board[index].append(int(i))
        
        self.game_board = game_board
        
        return                


    #checks to see if an addition is safe
    #given a board, row, col, and a number to add
    #This function will check if the addtion is legal
    def isSafe(self, board, row, col, num):
        
        #checking if duplicate num in row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        #checking if duplicates in col
        for j in range(9):
            if board[j][col] == num:
                return False

        #finds the boarder to the box of the number    
        startR = row - row % 3
        startC = col - col % 3

        #ching if duplicats in the box
        for i in range(3):
            for j in range(3):
                if board[i + startR][j+ startC] == num:
                    return False
        

        #no rule violation was found
        return True
    

    def solve(self, board = None, row = 0, col = 0):
        if board == None:
            board = self.game_board

        #check if the puzzle is complete
        #col is 9 because on recursion the col is
        #incremented by 1
        if ( row == 8 and col == 9):
            return True


        #if last col reset to the next row
        if col == 9:
            row += 1
            col = 0

        #spot is already filled
        #move to next avaible spot
        if board[row][col] > 0:
            return self.solve(board, row, col + 1)
        
        for n in range(1, 10, 1):

            #is n a legal num to add:
            if self.isSafe(board, row, col, n):

                #assign the n to the spot
                board[row][col] = n

                #recursion
                if self.solve(board, row, col + 1):
                    print(board)
                    return True
            
            #reset board
            board[row][col] = 0
 
    
    def print(self) -> None:
        for i in self.game_board:
            print(str(i))
        
        pass