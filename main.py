from window import Window
# from point import Point
# from line import Line
# from cell import Cell
from maze import Maze

def main():
    win = Window(900, 900)
    grid = Maze(50, 50, 20, 20, 40, 40, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
