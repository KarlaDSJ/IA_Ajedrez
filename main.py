from chess.interface import Interface
from tkinter import Tk, Canvas

"""
    Programa que en un futuro le dará la oportunidad al usuario de jugar    
    ajedrez contra la computadora (IA), pero que por el momento permite 
    poner piezas en el tablero y guardar la configuración del mismo como 
    imagen o como pdf.
"""

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

    interface = Interface(canvas)
    interface.set_ornaments()
    interface.set_play_history()
    interface.create_buttons()
    interface.set_board()

    window.resizable(False, False)
    window.mainloop()