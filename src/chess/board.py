from .box import Box
from tkinter import messagebox
#Para generar el pdf
from src.common.config import * 
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle

class Board():
    """
    Board

    Permite al usuario interactuar con un tablero de ajedrez:
        > Crear un tablero en blanco
        > Recrear una jugada
        > Mover piezas
        > Crear un tablero para iniciar el juego
    """
    
    def __init__(self) -> None:
        self.board = [] # Tablero compuesto de casillas

        #Para el historial de las piezas del tablero
        self.white_pieces = []
        self.black_pieces = []

        font = "assets/fonts/MERIFONT.TTF"
        pdfmetrics.registerFont(TTFont('ChessMerida', font))

        self.pdf = SimpleDocTemplate("chess.pdf")

        self.piece = "" #Pieza que será puesta en el tablero

    def set_piece(self, piece):
        """
            Guarda una pieza seleccionada para ser puesta/movida
            en el tablero

            piece - nombre y pieza
        """
        self.piece = piece

    def put_piece(self, id):
        """
            Modifica una casilla para poner o quitar una pieza

            id - número de la pieza
        """
        if self.piece != "":
            self.board[id].set_piece(self.piece[0], self.piece[1])
        else:   
            self.board[id].set_piece("", "")

    def set_board_num(self):
        """Agrega los números de las coordenadas del tablero"""
        for i in range(8):
            canvas.create_text(
                41.8695068359375,
                420 - (43 * i),
                anchor="nw",
                text=str(i + 1),#Números
                fill="#000000",
                font=("PTSans Bold", 14 * -1)
            )

    def set_board_letters(self):
        """Agrega las letras de las coordenadas del tablero"""
        letters  = list(map(chr, range(97, 105)))
        for i in range(8):
            #Letras
            canvas.create_text(
                67.8695068359375 + (43 * i),
                456.9809265136719,
                anchor="nw",
                text= letters[i], #Letras
                fill="#000000",
                font=("PTSans Bold", 14 * -1)
            )
    
    def set_empty_board(self):
        """Muestra en pantalla un tablero de ajedrez vacío"""
        num = 0
        for x in range(8):
            for y in range(8):
                if len(self.board) < 64:
                    #Si el tablero ya contiene todas las casillas
                    box = Box(x, y, num * 1, self.put_piece)
                    box.set_image()
                    box.show_on_screen()
                    self.board.append(box)
                else:
                    #Si existen las casillas modificamos su imagen
                    self.board[(8*x)+y].set_piece("","")
                num = not num
            num = not num

    def rotate(self):
        print("Tablero rotado")

    def set_board(self, pieces):
        """Muestra un tablero con ciertas piezas
        pieces - arreglo que contiene el nombre de las img 
            para mostrar el tablero con las piezas"""
        for x in range(8):
            for y in range(8):
                piece = pieces[(8*x)+y]
                color = piece[-1]
                if len(self.board) < 64:
                    #Si el tablero no contiene todas las casillas
                    box = Box(x, y, color, self.put_piece)
                    box.set_image()
                    box.show_on_screen()
                    self.board.append(box)
                #Modificamos su imagen
                if len(piece) == 1:
                    self.board[(8*x)+y].set_piece("","")
                else:
                    name = piece[:-1]
                    self.board[(8*x)+y].set_piece(name[0],name[1])

    def get_coord(self):
        "Genera una cadena con las coordenas de las piezas en el tablero"
        string = ""
        for x in range(8):
            for y in range(8):
                string += self.board[(8*x)+y].get_name() + " "
        return string


    def to_string(self) -> str:
        "Genera un string del tablero en la fuente MeridaChess"
        pieces_font = {
            "0" : "",
            "1" : "",
            "RB0" : "",
            "DB0" : "",
            "TB0" : "",
            "AB0" : "",
            "CB0" : "",
            "pB0" : "",
            "RB1" : "",
            "DB1" : "",
            "TB1" : "",
            "AB1" : "",
            "CB1" : "",
            "pB1" : "",
            "RN0" : "",
            "DN0" : "",
            "TN0" : "",
            "AN0" : "",
            "CN0" : "",
            "pN0" : "",
            "RN1" : "",
            "DN1" : "",
            "TN1" : "",
            "AN1" : "",
            "CN1" : "",
            "pN1" : ""
        }
        string = ""
        string += " <br />"

        for x in range(8):
            string += ""
            for y in range(8):
                string += pieces_font[self.board[(8*x)+y].get_name()]
            string += " <br />"
        string += "<br />"
        return string

    def save(self):
        tablero = self.to_string()
        text_style = ParagraphStyle(
            "Board",
            fontName="ChessMerida",
            alignment=TA_CENTER,
            leading=30,
            fontSize=30
        )
        self.pdf.build([Paragraph(tablero, text_style)])
        messagebox.showinfo("Information","Tablero guardado en chess.pdf")
    
    def save_play_history(self):
        print("historial de tiradas")

    def set_fila(self, x_i, x_j, color):
        """
            Pone las 2 filas de piezas de un color para
            el inicio del juego

            x_i - número de la fila donde está el rey 
            x_j - número de la fila de peones
            color - color de las piezas
        """
        pieces = ["T","C","A","D","R","A","C","T"]

        for i in range(8):
            self.board[i+x_i].set_piece(pieces[i], color)
        
        for i in range(8):
            self.board[i+x_j].set_piece("p", color)

    def set_initial_board(self):
        """Piezas inicio del juego"""
        self.set_empty_board()
        self.set_fila(0,1*8,"N")
        self.set_fila(7*8,6*8,"B")

    def clean(self):
        """Quitamos el tablero"""
        canvas.delete('all')
        for i in self.board:
            i.clean()
        self.board = []