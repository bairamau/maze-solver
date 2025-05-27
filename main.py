from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    
    line1 = Line(Point(0, 0), Point(800, 600))
    line2 = Line(Point(800, 0), Point(0, 600))
    
    win.draw_line(line1, "gold")
    win.draw_line(line2, "lightblue")

    win.wait_for_close()


if __name__ == "__main__":
    main()
