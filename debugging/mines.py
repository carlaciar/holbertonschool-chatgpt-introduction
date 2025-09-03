#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        total = width * height
        if not (0 < mines < total):
            raise ValueError("Mines must be between 1 and total-1 cells.")
        self.mines = set(random.sample(range(total), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.safe_cells = total - mines  # number of non-mine cells
        self.revealed_safe = 0          # track how many safe cells we've revealed

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2}', end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        ch = '*'
                    else:
                        count = self.count_mines_nearby(x, y)
                        ch = str(count) if count > 0 else ' '
                    print(f'{ch:2}', end='')
                else:
                    print(' .', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the center cell
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reveal(self, x, y):
        if not self.in_bounds(x, y):
            return True  # ignore out-of-bounds gracefully
        if self.revealed[y][x]:
            return True  # already revealed: nothing to do

        idx = y * self.width + x
        if idx in self.mines:
            return False  # hit a mine

        # reveal this safe cell
        self.revealed[y][x] = True
        self.revealed_safe += 1

        # flood-reveal neighbors if no adjacent mines
        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if self.in_bounds(nx, ny) and not self.revealed[ny][nx]:
                        # only recurse on still-hidden cells
                        self.reveal(nx, ny)

        return True

    def has_won(self):
        return self.revealed_safe == self.safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            ok = self.reveal(x, y)
            if not ok:
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            if self.has_won():
                self.print_board(reveal=True)
                print("🎉 You win! All safe cells revealed.")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
