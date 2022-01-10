import random
from tkinter.constants import LAST, X
from .box import Box
from tkinter import messagebox, Frame
import time
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

        self.frame = Frame(canvas)
        self.frame.place()

        #Para las flechas
        self.click_num = 0
        self.x1,self.x2,self.y1,self.y2 = 0,0,0,0

        #Para mover las piezas
        self.id_num = 0
        self.id1,self.id2 = 0,0

        font = "assets/fonts/MERIFONT.TTF"
        pdfmetrics.registerFont(TTFont('ChessMerida', font))

        self.pdf = SimpleDocTemplate("chess.pdf")

        self.piece = "" #Pieza que será puesta en el tablero

    def get_num(self, x, y):
        """Regresa el número de la casilla dadas las coordenadas"""
        x = (x - 60) // 43
        y = (y - 110) // 43
        return (8*y)+x

    def move(self,id):
        """Mueve una pieza en el tablero"""
        if self.id_num == 0:
            self.id1 = id
            self.id_num = 1
        else:
            self.id2 = id
            self.id_num = 0
            name = self.board[self.id1].get_name()
            #Que la primer casilla tenga una pieza y la segunda esté vacía
            if len(name) != 0 and len(self.board[self.id2].get_name()) == 0:
                x,y = self.board[self.id1].x, self.board[self.id1].y
                string = self.board[self.id1].toString()
                while True:
                    if x == self.board[self.id2].x and y == self.board[self.id2].y:
                        self.board[self.id1].set_piece("", "") #Quitamos pieza 
                        self.board[self.id2].set_piece(name[0], name[1]) #Img final 
                        break #Si llegamos a la casilla meta
                    #Movemos las coordenadas
                    piece =  canvas.create_text(x, y, text=string, fill="black", font=('Carlito 25 bold'))
                    if x != self.board[self.id2].x : 
                        x = x + 1 if x < self.board[self.id2].x else x - 1
                    if y != self.board[self.id2].y:
                        y = y + 1 if y < self.board[self.id2].y else y - 1
                    
                    #Para la animación
                    canvas.tag_raise(piece)
                    canvas.after(70, canvas.delete, piece)
                    time.sleep(0.0001)
                

    def set_arrow(self, event):
        """Pone una flecha dadas dos coordenadas"""
        if self.click_num == 0:
            self.x1 = event.x
            self.y1 = event.y
            self.click_num = 1
        else:
            #Color aleatorio
            fill="#"+("%06x"%random.randint(0,16777215))
            self.x2 = event.x
            self.y2 = event.y
            self.click_num = 0
            line = canvas.create_line(self.x1,self.y1,self.x2,self.y2, fill=fill, width=5, arrow=LAST)
            canvas.tag_raise(line)
            return line

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
                    box = Box(x, y, num * 1)
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
                    box = Box(x, y, color)
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
                string += self.board[(8*x)+y].get_name()+ str(self.board[(8*x)+y].back) + " "
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
                box = self.board[(8*x)+y]
                string += pieces_font[box.get_name()+ str(box.back)]
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