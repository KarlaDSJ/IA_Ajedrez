from tkinter import PhotoImage
from .config import *

class Interface():
    """
    Interface

    Crea una interfaz para que el usuario pueda interactuar
    """

    def __init__(self, button_info) -> None:
        #Nombres de los botones y la función que harán al dar click
        self.button_name = button_info
        self.buttons = [] # Botones del Inicio
        self.img_buttons = [] #Imágenes de los botones

    def clean(self, all=True):
        """Limpia el canvas"""
        if all:
            canvas.delete('all')
        for i in self.buttons:
            i.destroy()
        self.buttons= [] 
        self.img_buttons= []

    def set_footer(self):
        """Pone los adornos de la parte superior"""
        self.image_down_img = PhotoImage(
            file=relative_to_assets("images/ola_down.png"))
        self.image_down = canvas.create_image(
            385.0,
            552.0,
            image=self.image_down_img
        )

    def set_header(self):
        """Pone los adornos de la parte inferior"""
        self.image_top_img = PhotoImage(
            file=relative_to_assets("images/ola_top.png"))
        self.image_top = canvas.create_image(
            385.0,
            10.0,
            image=self.image_top_img
        )
    
        