

import board as b


def main():
    puzzle = "-2--6----/4-6--51--/----7--3-/-1---2---/8-2-5---7/-9----8--/---4----1/5-8--64--/9--------"
    game = b.board(puzzle)
    print(game.is_legal(game.game_board))
    game.print()
    print("\n")
    print(game.solve())

if __name__ == "__main__":
    main()