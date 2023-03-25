from random import randint

class Cell:
    def __init__(self, mine: bool = False, around_mines: int = 0) -> None:
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False
    
    def open(self):
        self.fl_open = True

    def show(self):
        return ("*" if self.mine else self.around_mines) if self.fl_open else "#"
        
class GamePole:
    def init(self) -> list:
        N, M = self.N, self.M
        mines = 0
        
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        
        while mines < M:
            i, j = randint(0, N-1), randint(0, N-1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            mines += 1

        index = ((-1, -1), (-1, 0), (-1, 1), 
                 (0,-1),            (0, 1),
                 (1, -1),  (1, 0),  (1, 1))
        
        for x in range(N):
            for y in range(N):
                m = sum(self.pole[x+i][y+j].mine for (i, j) in index if 0 <= x+i < N and 0 <= y+j < N)
                self.pole[x][y].around_mines = m

        
    def __init__(self, N: int, M: int) -> None:
        """N - size of map. M - number of mines."""
        self.N = N
        self.M = M
        self.init()

    def show(self):
        for line in self.pole:
            for cell in line:
                print(cell.show(), end=" ")
            print()
    
class Game:
    def menu(self):
        while True:
            choice = int(input("1. Почати нову гру.\n0. Вихід\n"))
            if choice == 1:
                self.start_game()
            elif choice == 0:
                return
            else:
                print("Incorect input!")

    def start_game(self):
        self.N = int(input("Скільки клітинок бажаєте?(Мінімум 5, максимум 10): "))
        self.M = int(input("Скільки бомб бажаєте?(Мінімум 5, максимум 10): "))
        self.pole = GamePole(self.N, self.M)
        self.play()

    def play(self):
        while True:
            self.pole.show()
            x, y = input("Вибиріть бажану клітинку(x,y): ").split(",")
            x, y = int(x), int(y)
            if not (0 <= x < self.N and 0 <= y < self.N):
                print("Incorect input!")
                continue
            elif self.pole.pole[x][y].mine:
                self.pole.pole[x][y].open()
                self.pole.show()
                print("!!!BADABOOM!!!\n!!!GAME OVER!!!\n")
                return
            else:
                self.pole.pole[x][y].open()

if __name__ == "__main__":
    game = Game()
    game.menu()