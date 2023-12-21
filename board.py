


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

    def is_complete(self, check = None):
        if check == None:
            check = self.game_board
        
        if self.is_full(check):
        
            if self.is_legal(check):
                return True
        
        return False

    def is_full(self, check):
        if check == None:
            check = self.game_board
        
        #The next two lines with go through every square for row i column j
        for i in range(9):
            for j in range(9):
                if check[i][j] == None:
                    return False
        return True
    

    def solve(self, check = None):
        if check == None:
            check = list(self.game_board)
        
        if(self.is_complete(check)):
            return True, check
        
        #The next two lines with go through every square for row i column j
        for i in range(9):
            for j in range(9):
                
                #if the square row i column j is empty
                if check[i][j] == None:
                    
                    #then check if any of the follow values can fill the square
                    for k in range(1, 10):
                       
                       #copy the board
                       check_copy = list(check)
                       #replace the square in question with a value in the copy
                       check_copy[i][j] = str(k)

                       if self.is_legal(check_copy):
                            print(check_copy)
                            #check to see if the copy is legal
                            if self.is_complete(check_copy) == True:
                                return True, check_copy
                            else:
                                solution, answer = self.solve(check_copy)
                                
                                if solution == True:
                                    return True, answer

                           
                           
                        
                           
        return False, "no solution"
                       
    
    def print(self) -> None:
        for i in self.game_board:
            print(i)
        
        return