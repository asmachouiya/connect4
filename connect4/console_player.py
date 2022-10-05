from .game import Grid, Player, Cell


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        print(grid)
        column_number = input()
        return int(column_number)

if __name__ == "__main__":
    g = Grid()
    console = ConsolePlayer()
    console.play(g)







