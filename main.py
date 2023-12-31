""""
Given a sudoku puzzle in the form of a string (space = "-", numbers, next row = "/")
this program will return the solution to the puzzle
"""

import game as g


def main():
    puzzle = "-2--6----/4-6--51--/----7--3-/-1---2---/8-2-5---7/-9----8--/---4----1/5-8--64--/9--------"
    puzzle = "-9-6---85/3---54962/5---8-3--/---8----3/75-9-3---/--3--14-6/--8---5--/2-53186-9/63--9-827"
    #solution
    #puzzle = "492637185/387154962/516289374/169842753/754963218/823571496/948726531/275318649/631495827"
    game = g.board(puzzle)
    #print(game.is_legal(game.game_board))
    game.print_board()
    print("\n")
    game.print_board(game.solve()[1])

if __name__ == "__main__":
    main()