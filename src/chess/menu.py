import re
from src.common.config import * 
from tkinter import Button, PhotoImage
from src.common.interface import Interface

class Menu(Interface):
    """
    Menu

    Al dar click en recrear partida nos mostrará un menú
    para agregar/eliminar piezas negras o blancas
    """
    
    def __init__(self, board) -> None:
        Interface.__init__(self, [])
        self.board = board
        self.pieces = ["R","D","T","A","C","p"]
        self.is_select = True
        self.is_arrow = False
        self.menu = False
        self.arrow = []
        #Img para el menú (flechas, seleccionar, borrar)
        self.menu_button = [PhotoImage(file=relative_to_assets("images/chess/flecha.png")),
                     PhotoImage(file=relative_to_assets("images/chess/seleccionar.png")),
                     PhotoImage(file=relative_to_assets("images/chess/borrar.png"))]
        #Img para cerrar el menú
        self.close  =PhotoImage(
            file=relative_to_assets("images/chess/close.png"))

    def get_is_menu(self):
        """Nos indica si el menu está activo"""
        return self.menu

    def add_arrow(self, line):
        """Agrega la referencia a una flecha"""
        self.arrow.append(line)

    def get_is_arrow(self):
        """Nos indica si la opción de poner flechas está activa"""
        return self.is_arrow

    def do_click(self, id):
        """
            Función que se ejecuta cuando hacemos click 
            en alguna pieza del menú 

            id - nos indica que pieza fue seleccionada 
        """
        if self.is_select:
            self.board.set_piece(id)

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
                x=100.0 + (43 * i),
                y= y,
                width=43.0,
                height=43.0
            )

    def switch_var(self, val):
        """Función auxiliar para indicar si se pone una pieza 
           o una flecha"""
        if val == 0:
            self.is_arrow = True
            self.is_select = False
        else:
            self.is_select = True
            self.is_arrow = False

    def delete(self):
        """Borra una pieza o flecha del tablero"""
        if self.is_select:
            self.board.set_piece("")
        elif len(self.arrow) > 0:
            x = self.arrow.pop()
            canvas.delete(x)

    def set_menu(self):
        """Muestra un menú para la fichas blancas y 
        otro para las negras que permite agregar o 
        eliminar piezas"""

        self.menu = True

        self.set_pieces(43.0, "N") #Piezas negras
        self.set_pieces(479.0, "B") #Piezas blancas

        for i in range(3):

            menu_set = lambda x = i: self.switch_var(x)
            #Botón para agregar/borrar una pieza
            self.buttons.append(Button(
                image=self.menu_button[i],
                borderwidth=0,
                highlightthickness=0,
                command= self.delete if i == 2 else menu_set,
                relief="flat"
            ))

            self.buttons[12 + i].place(
                x=377.0 + (i * 55),
                y=43.0 if i != 1 else 40,
                width=40.0 if i != 1 else 50,
                height=40.0 if i != 1 else 50
            )

        #Botón para cerrar el menú
        self.buttons.append(Button(
            image=self.close,
            borderwidth=0,
            highlightthickness=0,
            command= self.clean,
            relief="flat"
        ))

        self.buttons[15].place(
            x=542.0,
            y=45,
            width=40.0,
            height=40.0
        )

    def clean(self):
        """Eliminamos el menu"""
        super().clean(False)
        self.is_select = True
        self.is_arrow = False
        self.menu = False
        self.board.set_piece("")