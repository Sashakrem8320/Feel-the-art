class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]
        self.hit_positions = set()  # Позиции попаданий
        self.missed_positions = set()  # Позиции промахов

    def shoot(self, row, col, result):
        if result == 'miss':
            self.missed_positions.add((row, col))
            self.map[row][col] = '*'
        elif result == 'hit':
            self.hit_positions.add((row, col))
            self.map[row][col] = 'x'
        elif result == 'sink':
            self.hit_positions.add((row, col))
            self.map[row][col] = 'x'
            # Помечаем соседние клетки как ' * '
            self.mark_surrounding_cells(row, col)

    def mark_surrounding_cells(self, row, col):
        # Проверка соседних клеток (вверх, вниз, влево, вправо)
        for d_row in range(-1, 2):
            n_row = row + d_row
            if 0 <= n_row < 10:
                if self.map[n_row][col] == '.':  # Только помечаем пустые клетки
                    self.map[n_row][col] = '*'

        for d_col in range(-1, 2):
            n_col = col + d_col
            if 0 <= n_col < 10:
                if self.map[row][n_col] == '.':
                    self.map[row][n_col] = '*'

    def cell(self, row, col):
        return self.map[row][col]


if __name__ == "__main__":
    sm = SeaMap()

    sm.shoot(2, 0, 'sink')
    sm.shoot(6, 9, 'hit')

    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()