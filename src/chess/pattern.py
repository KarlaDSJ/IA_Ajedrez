from tkinter import Button, Entry, Label, Toplevel, messagebox
from xmlrpc.client import boolean
from src.common.config import canvas
import chess
"""Las instrucciones del lenguaje son:

P1(P2) - La pieza 1 ataca/defiende a la pieza 2.
P(casilla) - La pieza ataca la casilla.
P casilla - La pieza está en esa casilla

Por convención las piezas blancas se ponen con su iniciales mayúsculas 
y las piezas negras con sus iniciales en minúscula.

Leer el archivo de patrones 
Crear otro archivo pgn donde exista uno de los patrones antes mencionados 
Iterar sobre los movimientos de cada juego y preguntar por las piezas atacadas
"""

class Pattern():
    
    """
    Patrón 

    Busca un patrón dentro de una jugada de ajedrez
    """
    
    def __init__(self, games, board_set_board, parse) -> None:
        self.patterns = []
        self.games = games
        self.board_set_board = board_set_board
        self.parse = parse


    def read_file(self):
        """Crea una nueva ventana para que el usuario ingrese 
        la ruta del archivo que contiene el patrón"""
        level = Toplevel(canvas)
        level.geometry("300x200")
        label_name_arch = Label(level, text="Ruta del archivo con el patrón:")
        name_arch =  Entry(level, width=30)
        name_arch.insert(0, 'patron.txt')
        read = Button(level, text="leer", command= lambda:[self.get_pattern(name_arch.get()),level.destroy()])
        label_name_arch.place(x=10, y=10)
        name_arch.place(x=30, y=50)
        read.place(x=120,y=80)
    
    def get_pattern(self, name):
        """ Obtiene el patrón
        name - ruta del archivo
        """
        try:
            pattern = open(name)
            #self.pattern = self.parse(pattern)
            lineas = pattern.readlines()
            for i in lineas:
                self.patterns.append(i[0:-1].split(", "))
            boards, games = self.search_pattern()
            if len(boards) > 0:
                self.board_set_board(self.parse(boards[0]))
                cadena = " ,".join(map(str,games))
                messagebox.showinfo("Information", "Pantrón encontrado en los juegos: [" + cadena + "]")
                for i in range(len(boards)):
                    print("Pantrón encontrado en el juego ", games[i])
                    print(boards[i])
            else:
                messagebox.showerror("Error","Patrón no encontrado")
        except IOError:
            messagebox.showerror("Error","Archivo no encontrado")
    
    def check_piece(self, val, p_search, p):
        """
        Verifica que la pieza de una casilla sea igual a la que
        buscamos
        :param val: 
        :param p_search: Pieza que está en la casilla del tablero
        :param p: pieza para comparar
        """
        if p_search is not None:
            val += p_search.piece_type == p
            val = boolean(val)
        else:
            val = False
        return val

    def attack_by(self, val, i, board):
        """
        Comprueba que una pieza sea atacada como lo indica el patrón
        :param i: cadena con la información del patrón
        :param board: tablero de ajedrez
        """
        squares = i.split("(")
        square = chess.parse_square(squares[1][:-1]) 
        color = squares[0].isupper()
        attackers = board.attackers(color, square)
        for a in attackers:
            val = self.check_piece(val, board.piece_at(a), squares[0])
            if not val: return val
        return True

    def search_pattern(self):
        """
        Función que busca los patrones en un juego
        :param game: juego de ajedrez 
        """
        val = True
        game_pattern = []
        game_num = []
  
        for j in range(len(self.games)):
            print("juego: ", j)
            game = self.games[j].mainline_moves()

            for pattern in self.patterns:
                board = self.games[j].board()
                for move in game:
                    val = True
                    for i in pattern:
                        if i.find("(") != -1:
                            val = self.attack_by(val, i, board)
                            if not val: break
                        else:
                            square = chess.parse_square(i[1:])
                            val = self.check_piece(val, board.piece_at(square), i[0])
                            if not val: break
                    if val:
                        game_pattern.append(board)
                        game_num.append(j)
                        break
                    board.push(move)
        return game_pattern, game_num
