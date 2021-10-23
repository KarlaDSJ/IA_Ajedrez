from tkinter.constants import BOTH, END, LEFT, RIGHT, WORD, Y
from .cardHolder import CardHolder
from src.common.config import *
from src.common.interface import Interface
from tkinter import Listbox, messagebox, Text, Scrollbar, PhotoImage, Button, Label

class InterfaceCardH(Interface):
    """
    InterfaceCardH

    Crea una interfaz para que el usuario pueda 
    agregar, modificar, buscar y ver jugadas 
    """
    def __init__(self, set_home, board, menu) -> None:
        #Home
        self.set_home = set_home
        #Tablero
        self.board = board 
        #Menu
        self.set_menu = menu.set_menu
        self.menu = menu
        #Base de datos
        self.card_holder = CardHolder()
        self.cards = self.card_holder.get_all_cards()
        self.holder_card = []
        #Para los rectángulos de todas las cartas
        self.rec = []
        #Para que el usuario ingrese los valores
        self.entry_img = []
        self.entry = []
        #Img botón ver
        self.look = PhotoImage(
            file=relative_to_assets("images/elo/ver.png"))
        #Botones y su función al dar click
        self.button_info = [("regresar", self.back),
                       ("home", self.go_home),
                       ("guardar", self.save),
                       ("editar", self.set_menu),
                       ("borrar", self.delete),
                       ("agregar", lambda : self.card_on_click("", True))]
        super().__init__(self.button_info)

    def move_to_window(self):
        """Limpia la ventana y prepara todo para la siguiente"""
        self.clean()
        self.set_footer()
        self.set_header()
        self.default_buttons()

    def show_cards(self):
        """Muestra todas las tarjetas de jugadas almacenadas 
        en la base de datos"""
        self.move_to_window()
        #Rectángulo para jugadas
        self.rec.append(canvas.create_rectangle(
            66,
            155,
            704,
            480,
            fill="#E5E5E5",
            outline=""))

        self.rec.append(Scrollbar(window))
        #self.rec[1].pack(side = RIGHT,fill = Y)

        self.buttons[5].place(
            x=346,
            y=492,
            width=84,
            height=24
        )

        #self.rec.append(Listbox(window, 
            #yscrollcommand = self.rec[1].set))

        for i in range(len(self.cards)):
            self.set_one_card(i)

        #self.rec[2].pack(side = LEFT, fill = BOTH)
        #self.rec[1].config(command=self.rec[2].yview)

    def set_one_card(self, i):
        """Muestra la información de una tarjeta de juego
        i - id de la tarjeta"""
        move = []
        move.append(Label(
                text=self.cards[i][1],
                bg="#E5E5E5",
                justify=LEFT)) #Título
        move.append(Label(
            text=self.cards[i][3],
            bg="#E5E5E5",
            justify=LEFT)) #Descripción
        move[0].place(x=81, y=175 + (i*65))
        move[1].place(x=301, y=172 + (i*65))
        move.append(Button(
                image=self.look,
                borderwidth=0,
                highlightthickness=0,
                command= lambda id = i: self.card_on_click(id),
                relief="flat"
        ))
        move[2].place(
            x=602,
            y=179 + (i*65),
            width=70.7,
            height=20
        )
        self.holder_card.append(move)
        #self.rec[2].insert(END,move)

    def card_on_click(self,id, new=False):
        """Nos muestra otra vista para editar, guardar, eliminar
        la tarjeta
        id - Id de la jugada"""
        self.move_to_window()
        self.set_buttons()
        #Rectángulo detrás del tablero
        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            34.0,
            92.0,
            410.6521301269531,
            477.90203857421875,
            fill="#C4C4C4",
            outline="")
        self.board.set_board_num()
        self.board.set_board_letters()
        if new:
            self.id = ""
            self.set_entry() #Mostramos las tarjeta
            self.board.set_empty_board()
        else:
            self.id = self.cards[id][0]
            self.set_entry(self.cards[id][1],self.cards[id][3]) #Mostramos las tarjeta
            self.board.set_board(self.cards[id][2].split())

    def save(self):
        """Guarda en la base de datos la información
        de la tarjeta"""
        tablero = self.board.get_coord()
        titulo = self.entry[0].get(1.0,'end')
        descripcion = self.entry[1].get(1.0,'end')
        if self.id == "":
            self.cards = self.card_holder.add_card(titulo, tablero, descripcion)
        else:
            self.cards = self.card_holder.update_card(self.id,titulo, tablero, descripcion)

    def delete(self):
        """Borra una tarjeta de la base de datos, no regresa a ver todas las 
        jugadas"""
        self.cards = self.card_holder.delete_card(self.id) 
        self.clean()
        self.show_cards()

    def set_entry(self, titulo = '''Título''',  descripcion = '''Descripción'''):
        #Rectángulo para jugadas
        canvas.create_rectangle(
            432.0,
            98.0,
            599.0,
            473.0,
            fill="#FFFFFF",
            outline="")

        for i in range(2):
            self.entry.append(Text(
                width = 253, 
                height = 35 + (i*189), 
                wrap = WORD,
                padx = 5,
                pady = 5))

            self.entry[i].place(
                x=462,
                y=110 + (i*60),
                width=253,
                height=35 + (i*189)
            )
            self.entry[i].insert('1.0',titulo if i == 0 else descripcion)
            
    def clean(self):
        """Eliminamos todo lo del canvas"""
        super().clean()
        if len(self.entry) != 0:
            for i in self.entry:
                i.destroy()
        for i in self.holder_card:
            for j in i:
                j.destroy()
        self.holder_card = []
        self.entry = []
        self.board.clean()
        self.menu.clean()

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
        """Nos regresa a la vista de todas las tarjetas"""
        self.clean()
        self.show_cards()

    def go_home(self):
        """Regresa al usuario a la página principal"""
        self.clean()
        self.set_home()
