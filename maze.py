import time
import random

from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed:
            random.seed(seed)

        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_cols - 2:
            return True

        # Left
        if (
            i > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            result = self.__solve_r(i - 1, j)
            if result:
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo = True)
        # Right
        if (
            i < self.num_cols - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            result = self.__solve_r(i + 1, j)
            if result:
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo = True)
        # Top
        if (
            j > 0 
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            result = self.__solve_r(i, j - 1)
            if result:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo = True)
        # Bottom
        if (
            j < self.num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            result = self.__solve_r(i, j + 1)
            if result:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo = True)

        return False

    def __create_cells(self):
        for i in range(0, self.num_cols):
            self.__cells.append([])
            for j in range(0, self.num_rows):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x

        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y

        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            possible_directions = []

            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))

            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))

            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))

            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            next_i, next_j = random.choice(possible_directions)

            if next_i == i - 1:  # Moving left
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            elif next_i == i + 1:  # Moving right
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            elif next_j == j - 1:  # Moving up
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False
            elif next_j == j + 1:  # Moving down
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False

            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        for _ in self.__cells:
            for cell in _:
                cell.visited = False

    def __animate(self):
        if self.win is None:
            return

        self.win.redraw()
        time.sleep(0.008)
