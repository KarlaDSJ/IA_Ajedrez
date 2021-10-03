from config import relative_to_assets
from tkinter import PhotoImage

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
    def __init__(self, canvas, x, y, back) -> None:
        self.canvas = canvas
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

    def set_image(self):
        """ 
            Asigna la img correspondiente según la silla
            y la pieza que contiene
        """
        piece = self.name+self.color+str(self.back)
        self.img_box = PhotoImage(
            file=relative_to_assets("images/"+piece+".png"))

    def show_on_screen(self):
        """ Muestra en pantalla la casilla """
        self.canvas_box =  self.canvas.create_image(
                                212.53106689453125 + 43 * self.y,
                                127.07342529296875 + 43 * self.x,
                                image = self.img_box
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
        self.canvas.itemconfig(self.canvas_box,image=self.img_box)