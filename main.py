from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(10,10,20,20)
    cell1.has_left_wall = False
    cell1.draw()

    win.wait_for_close()


main()