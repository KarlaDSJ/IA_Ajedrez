from src.common.config import relative_to_assets
from .board import Board
from .menu import Menu
from src.common.interface import Interface
from tkinter import Text, Button, PhotoImage

class InterfaceChess(Interface):
    """
    InterfaceChess

    Crea una interfaz para que el usuario pueda interactuar 
    con el tablero de ajedrez
    """
    def __init__(self, canvas, set_home) -> None:
        self.canvas = canvas
        self.set_home = set_home #Home
        self.board = Board(canvas)
        self.pieces_menu = Menu(canvas, self.board)
        # Recuadros en donde se mostrarán las jugadas
        self.play_history = [[],[]] 
        #Recuadro para historial de jugadas
        self.rec_history =PhotoImage(
            file=relative_to_assets("images/chess/historial.png"))
        # Variables para la imágenes de adorno
        self.logo = 0
        self.logo_img = 0
        #Nombres de los botones y la función que harán al dar click
        button_info = [("home", self.go_home),
                       ("recrear_jugada", self.pieces_menu.set_menu), 
                       ("limpiar", self.board.set_empty_board), 
                       ("guardar_jugada", self.board.save), 
                       ("jugar", self.board.set_initial_board),
                       ("rotar", self.board.rotate), 
                       ("guardar_historial", self.board.save_play_history)]
        super().__init__(canvas, button_info)

    def go_home(self):
        """Regresa al usuario a la página principal"""
        self.clean()
        self.play_history[0][2].destroy()
        self.play_history[1][2].destroy()
        self.play_history = [[],[]] 
        self.board.clean()
        self.set_home()

    def set_board(self):
        """Crea un tablero de ajedrez vacío"""
        #Rectángulo detrás del tablero
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            172.13052368164062,
            93.01907348632812,
            548.7826538085938,
            472.9211120605469,
            fill="#C4C4C4",
            outline="")
        self.board.set_board_num()
        self.board.set_board_letters()
        self.board.set_empty_board()

    def create_buttons(self):
        """Crea los botones del menú del juego"""
        for i in range(7):
            self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/chess/"+self.button_name[i][0] + ".png")))
            self.buttons.append(Button(
                image=self.img_buttons[i],
                borderwidth=0,
                highlightthickness=0,
                command=self.button_name[i][1],
                relief="flat"
            ))
            if i == 6:
                self.buttons[i].place(
                    x=598.3993530273438,
                    y=479.40289306640625,
                    width=124.44107818603516,
                    height=25.540735244750977
                )
            else: 
                self.buttons[i].place(
                    x=28.134521484375 if i != 0 else 70,
                    y=175.0877685546875 + (55 * i),
                    width=117.407470703125 if i != 0 else 40,
                    height=29.888092041015625 if i != 0 else 40
                )

    def set_play_history (self):
        """Crea un recuadro para poner las jugadas de blancas y negras"""
        #Rectángulo para jugadas
        self.canvas.create_rectangle(
            577.0,
            98.0,
            742.0,
            473.0,
            fill="#C4C4C4",
            outline="")

        for i in range(2):
            #Imágen que indica el color
            self.play_history[i].append((PhotoImage(
                file=relative_to_assets("images/chess/image_"+ str(i+1) +".png"))))
            
            #Donde irán las jugadas
            self.play_history[i].append(self.canvas.create_image(
                620.0 + (81 * i),
                303.0,
                image=self.rec_history
            ))
            self.play_history[i].append(Text(
                bd=0,
                bg="#E5E5E5",
                highlightthickness=0
            ))
            self.play_history[i][2].place(
                x=587.0 + (81 * i),
                y=140.0,
                width=66.0,
                height=324.0
            )
            
            #Img del color
            self.play_history[i].append(self.canvas.create_image(
                620.0 + (81 * i),
                116.0,
                image=self.play_history[i][0]
            ))

    def set_ornaments(self):
        """Agrega algunos adornos a la interfaz del juego 
           para que se vea mejor"""
        #Logo
        self.logo_img = PhotoImage(
            file=relative_to_assets("images/chess/logo.png"))
        self.logo = self.canvas.create_image(
            91.0,
            99.0,
            image=self.logo_img
        )
        self.set_footer()
        self.set_header()