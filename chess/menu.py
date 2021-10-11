from common.config import relative_to_assets
from tkinter import Button, PhotoImage
from common.interface import Interface

class Menu(Interface):
    """
    Menu

    Al dar click en recrear partida nos mostrará un menú
    para agregar/eliminar piezas negras o blancas
    """
    
    def __init__(self, canvas, board) -> None:
        Interface.__init__(self, canvas, [])
        self.canvas = canvas
        self.board = board
        self.pieces = ["R","D","T","A","C","p"]
        self.is_select = True
        #Img para seleccionar una pieza
        self.select_piece =PhotoImage(
            file=relative_to_assets("images/chess/seleccionar.png"))
        #Img para borrar una pieza
        self.delete_piece  =PhotoImage(
            file=relative_to_assets("images/chess/borrar.png"))
        #Img para cerrar el menú
        self.close  =PhotoImage(
            file=relative_to_assets("images/chess/close.png"))

    def do_click(self, id):
        """
            Función que se ejecuta cuando hacemos click 
            en alguna pieza del menú 

            id - nos indica que pieza fue seleccionada 
        """
        if self.is_select:
            self.board.set_piece(id)
        else:
            self.board.set_piece("")

    def set_pieces(self, y, color):
        """
            Función auxiliar para poner las piezas del menú 
            y - posición en el eje y
            color - B (blancas), N (negras)
        """
        #posición dentro del arreglo
        p = 0 if color == "N" else 6

        for i in range(6):
            name = self.pieces[i] + color
            self.img_buttons.append(PhotoImage(
                file=relative_to_assets("images/chess/" + name + "0.png")))
            self.buttons.append(Button(
                image=self.img_buttons[p+i],
                borderwidth=0,
                highlightthickness=0,
                command= lambda x = name: self.do_click(x),
                relief="flat"
            ))
            self.buttons[p+i].place(
                x=234.0 + (43 * i),
                y= y,
                width=43.0,
                height=43.0
            )

    def switch_var(self, val):
        """Función auxiliar para indicar si una pieza 
           debe ponerse o quitarse"""
        self.is_select = val
        if not self.is_select:
            self.do_click(0)

    def set_menu(self):
        """Muestra un menú para la fichas blancas y 
        otro para las negras que permite agregar o 
        eliminar piezas"""

        self.set_pieces(43.0, "N") #Piezas negras
        self.set_pieces(479.0, "B") #Piezas blancas

        aux = False
        for i in range(2):
            #Botón para agregar/borrar una pieza
            aux = not aux
            self.buttons.append(Button(
                image=self.select_piece if i == 0 else self.delete_piece,
                borderwidth=0,
                highlightthickness=0,
                command=lambda x = aux: self.switch_var(x),
                relief="flat"
            ))

            self.buttons[12 + i].place(
                x=580.0 + (i * 55),
                y=43.0 + (i*2),
                width=50.0 - (i*10),
                height=50.0 - (i*10)
            )

        #Botón para cerrar el menú
        self.buttons.append(Button(
            image=self.close,
            borderwidth=0,
            highlightthickness=0,
            command= lambda x = False: self.clean(x),
            relief="flat"
        ))

        self.buttons[14].place(
            x=685.0,
            y=45,
            width=40.0,
            height=40.0
        )

# https://es.wikipedia.org/wiki/Sistema_de_puntuaci%C3%B3n_Elo
# https://la-morsa.blogspot.com/2011/05/la-medida-del-desempeno-en-ajedrez.html
# http://la-morsa.blogspot.com/search?q=elo