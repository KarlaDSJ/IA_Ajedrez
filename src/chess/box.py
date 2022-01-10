from src.common.config import *
from tkinter import Label, PhotoImage, Button
import tkinter as tk, tkinter.font as tkFont

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
    def __init__(self, x, y, back) -> None:
        self.canvas_box = 0 #componente dentro del canvas
        self.img_box = 0 # Imagen de la casilla
        #Coordenadas
        self.x = 80 + (43 * y) #num que representa las letras (a-h)
        self.y = 125.0 + (43 * x) #números (0-7)
        #Pieza de la casilla
        self.name = "" #Nombre(inicial)
        self.color = ""  # B - blanco, N - negro(color)
        #Color
        self.back = back # 0 - blanco, 1 - negro (fondo)
        #Agregamos la fuente 
        self.chessMerida = tkFont.Font(family='Chess Merida', size=25, weight='bold')

    def set_image(self):
        """ 
            Asigna la img correspondiente según la silla
            y la pieza que contiene
        """
        piece = str(self.back)
        self.img_box = PhotoImage(
            file=relative_to_assets("images/chess/"+piece+".png"))

    def show_on_screen(self):
        """ Muestra en pantalla la casilla """
        self.canvas_box_img = canvas.create_image(self.x, self.y, image = self.img_box)
        self.canvas_box =  canvas.create_text(self.x, self.y, text=self.toString(), fill="black", font=('Carlito 25 bold'))


    def set_piece(self, name, color):
        """
           Agrega una pieza a la casilla (actualiza la img)
           name (str) - inicial del nombre de la pieza
           color (str) - B o N 
        """
        self.name = name
        self.color = color
        self.set_image()
        self.clean()
        self.show_on_screen()
    
    def toString(self):
        """
        Convierte el nombre de las piezas en el símbolo de la pieza
        """
        pieces_font = {"":"",
            "RB":"\u2654", "RN":"\u265A",
            "DB":"\u2655", "DN":"\u265B",        
            "TB":"\u2656", "TN":"\u265C",
            "AB":"\u2657", "AN":"\u265D",
            "CB":"\u2658", "CN":"\u265E",
            "pB":"\u2659", "pN":"\u265F",   
        }
        return pieces_font[self.get_name()]

    def get_name(self) -> str:
        """
        Nos regresa la información de la casilla:
           > Nombre de la pieza
           > Color de la pieza
        """
        return self.name+self.color
    
    def clean(self):
        """Eliminamos la casilla del tablero"""
        canvas.delete(self.canvas_box)
        canvas.delete(self.canvas_box_img)