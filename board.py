


class board():
    
    def __init__(self, b = None):
        if b == None:
            pass
        else:
            self.create_board(b)
        
        self.count = 0
        return

    def create_board(self, b) -> None:
        game_board = [[] for _ in range(9)]
        index = 0
        for i in b:
            if i == "/":
                index += 1
            elif i == "-":
                game_board[index].append(None)
            else:
                game_board[index].append(i)
        
        self.game_board = game_board
        
        return

    def is_legal(self, check = None) -> bool:
        if check == None:
            check = self.game_board

        #check rows
        for i in check:
            for j in range(1, 10):
                exist = False
                for k in i:
                    if k == str(j):
                        if exist == True:
                            return False
                        else:
                            exist = True

        #check columns
        for i in range(9):
            for j in range(9):
                for k in range(1,10):
                    exist = False
                    if check[j][i] == str(k):
                        if exist:
                            return False
                        else:
                            exist = True

        #check squares
        sq = [[0,1,2],[3,4,5],[6,7,8]]
        for i in sq:
            for j in sq:
                for k in range(1,9):
                    exist = False
                    for l in i:
                        for m in j:
                            if check[l][m] == str(k):
                                if exist:
                                    return False
                                else:
                                    exist = True


        return True


    #returns true if the puzzle is solved
    def is_complete(self, check = None) -> bool:
        if check == None:
            check = self.game_board
        
        if self.is_full(check):
        
            if self.is_legal(check):
                return True
        
        return False

    #check to see if the board has any empty spaces
    def is_full(self, check) -> bool:
        
        #The next two lines with go through every square for row i column j
        for i in range(9):
            for j in range(9):
                if check[i][j] == None:
                    return False
                
        return True
    
    def find_empty(self, check):
        #The next two lines with go through every square for row i column j
        for i in range(9):
            for j in range(9):
                
                #if the square row i column j is empty
                if check[i][j] == None:
                    return (i,j)
        return None
        
    def solve(self, check = None):
        
        if check == None:
            check = list(self.game_board)

        
        if(self.is_complete(check)):
            print(check)
            return True, check
        
        
        #copy the board
        check_copy = list(check)
        row_col = self.find_empty(check_copy)
        
        if row_col == None:
            
            if self.is_complete(check_copy):
                return True, check_copy
            else:
                return False, check_copy

        for num in range(1, 10):
            self.count += 1
            print(self.count)
            #replace the square in question with a value in the copy
            check_copy[row_col[0]][row_col[1]] = str(num)

            if check_copy == [['4', '9', '2', '6', '3', '7', '1', '8', '5'], ['3', '8', '7', '1', '5', '4', '9', '6', '2'], ['5', '1', '6', '2', '8', '9', '3', '7', '4'], ['1', '6', '9', '8', '4', '2', '7', '5', '3'], ['7', '5', '4', '9', '6', '3', '2', '1', '8'], ['8', '2', '3', '5', '7', '1', '4', '9', '6'], ['9', '4', '8', '7', '2', '6', '5', '3', '1'], ['2', '7', '5', '3', '1', '8', '6', '4', '9'], ['6', '3', '1', '4', '9', '5', '8', '2', '7']]:
                print("answer found")
                return True, check_copy
            
            if self.is_legal(check_copy):

                solution, answer = self.solve(check_copy)

                if solution:
                    return True, answer
        
        return False, check_copy
    """
        #The next two lines with go through every square for row i column j
        for i in range(9):
            for j in range(9):
                
                #if the square row i column j is empty
                if check[i][j] == None:
                    
                    #copy the board
                    check_copy = list(check)

                    #then check if any of the follow values can fill the square
                    for k in range(1, 10):
                       
                       

                       #replace the square in question with a value in the copy
                       check_copy[i][j] = str(k)

                       solution, answer = self.solve(check_copy)

                       
                       if solution == True:
                           return solution, answer
                       
        return False, check
        """

                       
                       
                       
    
    def print(self) -> None:
        for i in self.game_board:
            print(i)
        
        pass