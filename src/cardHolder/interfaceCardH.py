from tkinter.constants import WORD
from src.common.config import relative_to_assets
from src.common.interface import Interface
from tkinter import Entry, Button, PhotoImage, messagebox, Text

class InterfaceCardH(Interface):
    """
    InterfaceCardH

    Crea una interfaz para que el usuario pueda 
    agregar, modificar, buscar y ver jugadas 
    """
    def __init__(self, canvas, set_home, board, set_menu) -> None:
        self.canvas = canvas
        #Home
        self.set_home = set_home
        #Tablero
        self.board = board 
        #Menu
        self.set_menu = set_menu
        #Para que el usuario ingrese los valores
        self.entry_img = []
        self.entry = []
        #Botones y su función al dar click
        self.button_info = [("regresar", self.back),
                       ("home", self.go_home),
                       ("guardar", self.save),
                       ("editar", self.set_menu),
                       ("borrar", self.go_home)]
        super().__init__(canvas, self.button_info)

    def save(self):
        """Guarda en la base de datos la información
        de la tarjeta"""
        print("Título: "+ self.entry[0].get(1.0,'end'))
        print("Descripción: "+ self.entry[1].get(1.0,'end'))
        #Falta guardarlo en la base

    def delete_card(self):
        #Falta borrarlo de la base
        self.clean() 

    def set_entry(self):
        #Rectángulo para jugadas
        self.canvas.create_rectangle(
            432.0,
            98.0,
            599.0,
            473.0,
            fill="#FFFFFF",
            outline="")

        self.entry.append(Text(
            width = 253, 
            height = 35, 
            wrap = WORD,
            padx = 5,
            pady = 5))
        
        self.entry.append(Text(
            width = 253, 
            height = 224, 
            wrap = WORD,
            padx = 5,
            pady = 5))

        self.entry[0].place(
                x=462,
                y=110,
                width=253,
                height=35
            )
        self.entry[0].insert('1.0','''Título''')

        self.entry[1].place(
                x=462,
                y=170,
                width=253,
                height=224
            )
        self.entry[1].insert('1.0','''Descripción''')
            
    def get_data(self) -> list:
        """Obtiene la información data por el usuario"""
        data = []
        try:
            for text in self.entry:
                data.append(int(text[1].get()))
        except:
            messagebox.showerror("Error","Los datos deben ser números")
        return data

    
    def clean(self):
        """Eliminamos todo lo del canvas"""
        super().clean()
        for i in self.entry:
            i[1].destroy()
        self.entry_img = []
        self.entry = []

    def default_buttons(self):
        """Agrega imágenes de adorno y para regresar a la
        página anterior o al inicio"""
        self.set_footer()
        self.set_header()
        
        for i in range(len(self.button_info)):
            self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/elo/"+self.button_info[i][0] + ".png")))
            self.buttons.append(Button(
                image=self.img_buttons[i],
                borderwidth=0,
                highlightthickness=0,
                command=self.button_info[i][1],
                relief="flat"
            ))
        for i in range(2):
            self.buttons[i].place(
                x=47 + (i * 621),
                y=37,
                width=40,
                height=40
            )

    def set_buttons(self):
        """Agrega los botones para editar, guardar, eliminar"""
        
        for i in range(3):
            self.buttons[i+2].place(
                x=462 + (i*131) if i < 2 else 528,
                y=422 if i < 2 else 464,
                width=117.41,
                height=29.89
            )

    def back(self):
        """Nos regresa a la primera vista del elo
        para ingresar nuevos datos"""
        self.clean()
        self.set_text()
        self.set_buttons()
        #Lo regresamos a la página de buscar

    def go_home(self):
        """Regresa al usuario a la página principal"""
        self.clean()
        self.set_home()
