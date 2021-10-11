from chess.interfaceChess import InterfaceChess
from elo.interfaceElo import InterfaceElo
from common.config import relative_to_assets
from common.interface import Interface
from tkinter import Tk, Canvas, PhotoImage, Button

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
    def __init__(self, canvas) -> None:
        button_info = [("jugar", self.set_game),
                       ("calcular ELO", self.set_elo)]
        super().__init__(canvas, button_info)
        self.canvas = canvas 
        self.interface_chess = InterfaceChess(self.canvas)
        self.interface_elo = InterfaceElo(self.canvas)

    def set_home(self):
        """ Mustra las opciones (jugar o calcular Elo)"""
        self.canvas.place(x = 0, y = 0) #Rectángulo azul
        self.canvas.create_rectangle(
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

    def set_elo(self):
        """Se muestra todo lo necesario para calcular el rating
           de un jugador al seleccionar calcular Elo"""
        self.clean()
        self.interface_elo.set_text()
        self.interface_elo.set_k_data()
        self.interface_elo.set_buttons()

if __name__ == "__main__":
    window = Tk()
    #Define el tamaño de la ventana
    window.geometry("770x562")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 562,
        width = 770,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    home = Home(canvas)
    home.set_home()

    window.resizable(False, False)
    window.mainloop()