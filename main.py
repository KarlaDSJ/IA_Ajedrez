from src.chess.interfaceChess import InterfaceChess
from src.elo.interfaceElo import InterfaceElo
from src.common.config import *
from src.common.interface import Interface
from tkinter import PhotoImage, Button

"""
    Programa que en un futuro le dará la oportunidad al usuario de jugar    
    ajedrez contra la computadora (IA), pero que por el momento permite 
    poner piezas en el tablero, guardar la configuración del mismo como 
    imagen o como pdf o calcular el rating de un jugador.
"""
class Home(Interface):
    """
    Home

    Crea una interfaz para que el usuario pueda interactuar 
    con los diferentes programas (jugar, calcular Elo)
    """
    def __init__(self) -> None:
        button_info = [("jugar", self.set_game),
                       ("calcular ELO", self.set_elo)]
        super().__init__(button_info)
        self.interface_chess = InterfaceChess(self.set_home)
        self.interface_elo = InterfaceElo(self.set_home)

    def set_home(self):
        """ Mustra las opciones (jugar o calcular Elo)"""
        canvas.place(x = 0, y = 0) #Rectángulo azul
        canvas.create_rectangle(
            0.0,
            0.0,
            385.0,
            562.0,
            fill="#37B5D0",
            outline="")

        for i in range(2):
            self.img_buttons.append(PhotoImage(
                file=relative_to_assets("images/"+self.button_name[i][0]+".png")))
            self.buttons.append(Button(
                image=self.img_buttons[i],
                borderwidth=0,
                highlightthickness=0,
                command=self.button_name[i][1],
                relief="flat"
            ))
            self.buttons[i].place(
                x=85.0 + (385 * i),
                y=260.0,
                width=212.0,
                height=49.0
            )

    def set_game(self):
        """Se muestra el tablero de ajedrez al dar click en jugar"""
        self.clean()
        self.interface_chess.set_ornaments()
        self.interface_chess.set_play_history()
        self.interface_chess.create_buttons()
        self.interface_chess.set_board()

        canvas.bind('<Button-1>', self.interface_chess.board.set_arrow)

    def set_elo(self):
        """Se muestra todo lo necesario para calcular el rating
           de un jugador al seleccionar calcular Elo"""
        self.clean()
        self.interface_elo.set_text()
        self.interface_elo.set_buttons()

if __name__ == "__main__":
    home = Home()
    home.set_home()

    window.resizable(False, False)
    window.mainloop()