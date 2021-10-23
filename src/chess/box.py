from src.common.config import *
from tkinter import PhotoImage, Button

class Box():
    """
    Box

    Representa una casilla en el tablero, contiene la siguiente info:
        > Coordenada en el tablero
        > Si contiene alguna pieza y de qué color
    
    Iniciales de las piezas:
        R - Rey
        D - Dama
        T - Torre
        A - Alfil
        C - Caballo
        p - Peón 
    """
    def __init__(self, x, y, back, on_clik) -> None:
        self.canvas_box = 0 #componente dentro del canvas
        self.img_box = 0 # Imagen de la casilla
        #Coordenadas
        self.x = x #num que representa las letras (a-h)
        self.y = y #números (0-7)
        #Pieza de la casilla
        self.name = "" #Nombre(inicial)
        self.color = ""  # B - blanco, N - negro(color)
        #Color
        self.back = back # 0 - blanco, 1 - negro (fondo)
        #función a realizar al dar click en la casilla
        self.on_click = on_clik 

    def set_image(self):
        """ 
            Asigna la img correspondiente según la silla
            y la pieza que contiene
        """
        piece = self.name+self.color+str(self.back)
        self.img_box = PhotoImage(
            file=relative_to_assets("images/chess/"+piece+".png"))

    def show_on_screen(self):
        """ Muestra en pantalla la casilla """
        self.canvas_box =  Button(
                                image=self.img_box,
                                borderwidth=0,
                                highlightthickness=0,
                                command= lambda id = (8*self.x)+self.y: self.on_click(id),
                                relief="flat"
                            )
        self.canvas_box.place(
            x=57 + (43 * self.y),
            y=105.0 + (43 * self.x),
            width=43.0,
            height=43.0
        )

    def set_piece(self, name, color):
        """
           Agrega una pieza a la casilla (actualiza la img)
           name (str) - inicial del nombre de la pieza
           color (str) - B o N 
        """
        self.name = name
        self.color = color
        self.set_image()
        self.canvas_box.configure(image=self.img_box)
    
    def get_name(self) -> str:
        """Nos regresa la información de la casilla:
           > Color de fondo
           > Color de la pieza
           > Inicial de la pieza"""
        return self.name+self.color+str(self.back)
    
    def clean(self):
        """Eliminamos la casilla del tablero"""
        self.canvas_box.destroy()
        self.canvas_box = 0
        self.img_box = 0