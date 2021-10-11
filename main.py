from chess.interface import Interface
from config import relative_to_assets
from tkinter import Tk, Canvas, PhotoImage, Button

"""
    Programa que en un futuro le dará la oportunidad al usuario de jugar    
    ajedrez contra la computadora (IA), pero que por el momento permite 
    poner piezas en el tablero, guardar la configuración del mismo como 
    imagen o como pdf o calcular el raiting de un jugador.
"""
class Home():
    """
    Home

    Crea una interfaz para que el usuario pueda interactuar 
    con los diferentes programas (jugar, calcular Elo)
    """
    def __init__(self, canvas) -> None:
        self.canvas = canvas 
        self.interface = Interface(self.canvas)
         #Nombres de los botones y la función que harán al dar click
        self.button_name = [("jugar", self.set_game), 
                    ("calcular ELO", self.set_game)]
        self.buttons = [] # Botones del Inicio
        self.img_buttons = [] #Imágenes de los botones

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

    def clean(self):
        """Limpia el canvas"""
        self.canvas.delete('all')
        for i in self.buttons:
            i.destroy()
        self.buttons= [] 
        self.img_buttons= []

    def set_game(self):
        """Se muestra el tablero de ajedrez al dar click en jugar"""
        self.clean()
        self.interface.set_ornaments()
        self.interface.set_play_history()
        self.interface.create_buttons()
        self.interface.set_board()

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