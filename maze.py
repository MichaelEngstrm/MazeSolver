from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for cols in range(0, self.num_cols):
            cols = []
            for row in range(0, self.num_cols):
                cols.append(Cell(self.win))         
            self._cells.append(cols)
        
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw(self.x1 + self.cell_size_x * i, self.y1 + self.cell_size_y * j,
                               self.x1 + self.cell_size_x * (i+1), self.y1 + self.cell_size_y * (j+1))
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)