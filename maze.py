from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is None:
            self._seed = random.seed(seed)
        else:
            self._seed = seed
        
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))         
            self._cells.append(cols)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            to_visit = [i+1, i-1, j+1, j-1]
            available_cells = []
            if to_visit[0] < self._num_cols:
                if not self._cells[to_visit[0]][j]._visited:
                    available_cells.append(self._cells[to_visit[0][j]])
            
            if to_visit[1] > 0:
                if not self._cells[to_visit[1]][j]._visited:
                    available_cells.append(self._cells[to_visit[1][j]])

            if to_visit[2] < self._num_rows:
                if not self._cells[i][to_visit[2]]._visited:
                    available_cells.append(self._cells[i][to_visit[2]])
            
            if to_visit[3] > 0:
                if not self._cells[i][to_visit[3]]._visited:
                    available_cells.append(self._cells[i][to_visit[3]])

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(0, len(to_visit))
            


