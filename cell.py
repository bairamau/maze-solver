from line import Line
from point import Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.visited = False

        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win is None:
            return

        self.__win.draw_line(
            Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
            "black" if self.has_left_wall else "#d9d9d9",
        )
        self.__win.draw_line(
            Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
            "black" if self.has_top_wall else "#d9d9d9",
        )
        self.__win.draw_line(
            Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
            "black" if self.has_right_wall else "#d9d9d9",
        )
        self.__win.draw_line(
            Line(Point(self.__x2, self.__y2), Point(self.__x1, self.__y2)),
            "black" if self.has_bottom_wall else "#d9d9d9",
        )

    def draw_move(self, to_cell, undo=False):
        start = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        end = Point(
            (to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2
        )

        if self.__win is None:
            return

        self.__win.draw_line(Line(start, end), "gray" if undo else "red")
