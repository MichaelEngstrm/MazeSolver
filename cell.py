from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)

        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x2 + self._x1)*0.5, (self._y2 + self._y1)*0.5)
        to_cell_center = Point((to_cell._x2 + to_cell._x1) * 0.5 , (to_cell._y2 + to_cell._y1) * 0.5)
        line = Line(self_center, to_cell_center)
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")