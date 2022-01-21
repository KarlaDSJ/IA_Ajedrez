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
    
    def __init__(self, games) -> None:
        self.patterns = []
        self.games = games


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
            self.search_pattern()
        except IOError:
            messagebox.showerror("Error","Archivo no encontrado")
    
    def search_pattern(self):
        """
        Función que busca los patrones en un juego
        :param game: juego de ajedrez 
        """
        for j in range(len(self.games)):
            print("juego: ", j)
            game = self.games[j].mainline_moves()

            for pattern in self.patterns:
                board = self.games[j].board()
                for move in game:
                    val = True
                    for i in pattern:
                        if i.find("(") != -1:
                            print("m")
                        else:
                            square = chess.parse_square(i[1:]) 
                            piece = board.piece_at(square)
                            print("Pieza tablero: ",piece, "pieza: ", i[0])
                            print(board)
                            if piece is not None:
                                val += piece.piece_type == i[0]
                                val = boolean(val)
                            else:
                                val = False
                                break
                    print(val)
                    if val:
                        print("Pantrón encontrado, juego: ", j)
                        return True
                    board.push(move)

