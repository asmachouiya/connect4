from .game import Grid, Player, Cell


class DumbIA(Player):

    def play(self, grid: Grid) -> int:
        for line in range(grid.lines):
            # si une colonne de cette ligne est vide on retourne le nombre de la colonne
            for column in range(grid.columns):
                if grid.grid[line][column] == Cell.EMPTY:
                    return column





