from config import relative_to_assets
from tkinter import Button, PhotoImage

class Menu:
    """
    Menu

    Al dar click en recrear partida nos mostrará un menú
    para agregar/eliminar piezas negras o blancas
    """
    
    def __init__(self, canvas, board) -> None:
        self.canvas = canvas
        self.board = board
        self.pieces = ["R","D","T","A","C","p"]
        #Primeros 0-5 negras, 6 - 11 blancas
        self.buttons= [] # Botones para la fichas 
        self.img_buttons= [] #Imágenes de los botones
        #Img para seleccionar una pieza
        self.select_piece =PhotoImage(
            file=relative_to_assets("images/seleccionar.png"))
        #Img para borrar una pieza
        self.delete_piece  =PhotoImage(
            file=relative_to_assets("images/borrar.png"))

    def do_click(self, id="algoo"):
        """
            Función que se ejecuta cuando hacemos click 
            en alguna pieza del menú 

            id - nos indica que pieza fue seleccionada 
        """
        print(id)

    def set_pieces(self, y, color):
        """
            Función auxiliar para poner las piezas del menú 
            y - posición en el eje y
            color - B (blancas), N (negras)
        """
        #posición dentro del arreglo
        p = 0 if color == "N" else 6

        for i in range(6):
            name = self.pieces[i] + color + "0"
            self.img_buttons.append(PhotoImage(
                file=relative_to_assets("images/" + name + ".png")))
            self.buttons.append(Button(
                image=self.img_buttons[p+i],
                borderwidth=0,
                highlightthickness=0,
                command= self.do_click,
                relief="flat"
            ))
            self.buttons[p+i].place(
                x=234.0 + (43 * i),
                y= y,
                width=43.0,
                height=43.0
            )

    def delete_menu(self):
        """Quita las opciones para agregar piezas"""
        self.buttons= [] 
        self.img_buttons= []
        #Falta buscar como ocultar/eliminar los botones


    def set_menu(self):
        """Muestra un menú para la fichas blancas y 
        otro para las negras que permite agregar o 
        eliminar piezas"""

        self.set_pieces(43.0, "N") #Piezas negras
        self.set_pieces(479.0, "B") #Piezas blancas

        for i in range(2):
            #Botón para agregar/seleccionar una pieza
            self.buttons.append(Button(
                image=self.select_piece,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("Agregar"),
                relief="flat"
            ))

            self.buttons[12+(i*2)].place(
                x=184.0,
                y=43.0 + (i * 432),
                width=50.0,
                height=50.0
            )

            #Botón para borrar/seleccionar una pieza (negras)
            self.buttons.append(Button(
                image=self.delete_piece,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("Borrar"),
                relief="flat"
            ))

            self.buttons[13+(i*2)].place(
                x=496.0,
                y=43.0 + (i * 432),
                width=40.0,
                height=40.0
            )