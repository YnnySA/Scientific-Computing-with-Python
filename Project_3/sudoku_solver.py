class Board:
    def __init__(self, board):
        # Constructor que inicializa el tablero de Sudoku
        self.board = board

    def __str__(self):
        # Método que convierte el tablero en una representación de string
        # Usa '*' para las celdas vacías (valor 0)
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        # Busca la primera celda vacía (valor 0) en el tablero
        # Retorna una tupla (fila, columna) o None si no hay celdas vacías
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        # Verifica si un número es válido en la fila especificada
        # Retorna True si el número no está presente en la fila
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Verifica si un número es válido en la columna especificada
        # Retorna True si el número no está presente en la columna
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Verifica si un número es válido en el cuadrado 3x3 correspondiente
        # Retorna True si el número no está presente en el cuadrado
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Verifica si un número es válido en una posición específica
        # Comprueba fila, columna y cuadrado 3x3
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Implementa el algoritmo de backtracking para resolver el Sudoku
        # Retorna True si encuentra una solución, False si no hay solución
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    # Función principal que resuelve el Sudoku
    # Crea una instancia de Board y muestra el resultado
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')

# Ejemplo de puzzle de Sudoku
# 0 representa las celdas vacías
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)