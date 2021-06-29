import json
import random


def fill_board_ai(height, width):
    board = {}
    for y in range(height):
        for x in range(width):
            if x == 0 or y == 0 or y == 5 or x == 5:
                board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 10}
            elif x == 1 or y == 1 or y == 4 or x == 4:
                board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 20}
            else:
                board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 40}
    print("{")
    for item, key in board.items():
        print(f"\t{item}: {key}")
    print("}")


if __name__ == '__main__':
    main(6, 6)
