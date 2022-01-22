from tkinter import Button, Entry, Label, PhotoImage, Toplevel, messagebox
from src.common.config import canvas, relative_to_assets
import chess.pgn
from .pattern import Pattern

class PGN():
    """
    PGN

    Clase que me permite interactuar y mostrar las partidas
    de un archivo PGN
    """
    
    def __init__(self, board_set_board) -> None:
        self.board_set_board = board_set_board
        self.games = []
        self.games_num = 0
        self.game = [] #Juego en turno
        self.moves = 0 #Número total de tiradas
        #Img para cerrar el menú
        self.close = PhotoImage(
        file=relative_to_assets("images/chess/close.png"))
        #Img para info
        self.info = PhotoImage(
        file=relative_to_assets("images/chess/info.png"))
        #Para movernos
        self.index_game = 0
        self.index = 0

    def get_next_game(self):
        """Si existe pasa al siguiente juego en el archivo"""
        if self.index_game+1 < self.games_num:
            self.index_game += 1
            self.move_last(self.index_game)

    def get_back_game(self):
        """Si existe se regresa al juego anterior en el archivo"""
        if self.index_game-1 >= 0:
            self.index_game -= 1
            self.move_last(self.index_game)

    def get_next(self):
        """Si es posible avanzamos una tirada"""
        if self.index+1 < len(list(self.game)):
            self.board.push(list(self.game)[self.index])
            self.index += 1
            self.board_set_board(self.parse(self.board))

    def get_back(self):
        """Si es posible regresamos una tirada"""
        if self.index-1 >= 0:
            self.index -= 1
            self.board.pop()
            self.board_set_board(self.parse(self.board))

    def read_file(self, is_pattern):
        """Crea una nueva ventana para que el usuario ingrese 
        la ruta del archivo PGN"""
        level = Toplevel(canvas)
        level.geometry("300x200")
        label_name_arch = Label(level, text="Ruta del archivo:")
        name_arch =  Entry(level, width=30)
        name_arch.insert(0, 'master_games.pgn')
        read = Button(level, text="leer", command= lambda:[self.get_games(name_arch.get(), is_pattern),level.destroy()])
        label_name_arch.place(x=10, y=10)
        name_arch.place(x=30, y=50)
        read.place(x=120,y=80)
    
    def move_last(self, i):
        """Inicializa el juego en la última jugada"""
        self.game = self.games[i].mainline_moves()
        self.board = self.games[i].board()
        for move in self.game:
            self.board.push(move)
        self.moves = self.board.fullmove_number
        self.index = len(list(self.game))
        self.board_set_board(self.parse(self.board))

    def get_games(self, name, is_pattern):
        """ Obtiene los juegos de un archivo PGN y 
        los guarda en una lista
        name - ruta del archivo
        """
        try:
            pgn = open(name)
            while True:
                game = chess.pgn.read_game(pgn)
                if game is not None:
                    self.games.append(game)
                    self.games_num += 1
                else:
                    break

            if is_pattern:
                self.pattern = Pattern(self.games, self.board_set_board, self.parse) #Archivo con el patrón
                self.pattern.read_file()
            else:
                self.move_last(0)
                self.show_buttons()

        except IOError:
            messagebox.showerror("Error","Archivo no encontrado")

    def parse(self, board):
        match = {
            'r' : 'TN',
            'n' : 'CN' ,
            'b' : 'AN',
            'q' : 'DN',
            'k' : 'RN',
            'p' : 'pN',
            'R' : 'TB',
            'N' : 'CB' ,
            'B' : 'AB',
            'Q' : 'DB',
            'K' : 'RB',
            'P' : 'pB',
            '.' : ''
        }
        string = board.__str__().split()
        num = 0
        for x in range(8):
            for y in range(8):
                aux = string[(8*x)+y]
                string[(8*x)+y] = match[aux] + str(int(num))
                num = not num
            num = not num
        return string

    def clean(self):
        """Para borrar los botones para movernos en las jugadas"""
        for i in self.buttons:
            i.destroy()
        self.buttons= [] 
        self.label_num_games.destroy()
        self.games_num = 0

    def get_info(self):
        """Crea una nueva ventana para mostrar la información de la partida"""
        level = Toplevel(canvas)
        level.geometry("300x350")
        labels = []
        i = 0
        for clave in self.games[self.index_game].headers:
            txt = "{}: {}".format(clave, self.games[self.index_game].headers[clave])
            label = Label(level, text=txt)
            label.place(x=2, y=10+(i*20))
            i += 1

    def show_buttons(self):
        """Muestra los botones para moverse entre las jugadas
         y los juegos del archivo"""
        self.buttons = [Button(text='<',command=self.get_back_game),
                        Button(text='>', command=self.get_next_game),
                        Button(text='<',command=self.get_back),
                        Button(text='>', command=self.get_next),
                        Button(image=self.close, borderwidth=0, highlightthickness=0,
                         command= self.clean, relief="flat"),
                        Button(image=self.info, borderwidth=0, highlightthickness=0,
                         command= self.get_info, relief="flat")]
        self.label_num_games = Label(text="Juegos: "+str(self.games_num))
        self.label_num_games.place(x=84, y=45)

        for i in range(len(self.buttons)-1):
            self.buttons[i].place(
                x=190 + 40 * (i%2),
                y=43 if i < 2 else 500,
            )
        
        #Botón para cerrar el menú
        self.buttons[4].place(
            x=542.0,
            y=45,
            width=40.0,
            height=40.0
        )

        #Botón para ver infomación de la partida
        self.buttons[5].place(
            x=500.0,
            y=45,
            width=40.0,
            height=40.0
        )
        