from tkinter import messagebox
from common.config import relative_to_assets
from common.interface import Interface
from tkinter import Entry, Button, PhotoImage
from elo.elo import Elo

class InterfaceElo(Interface):
    """
    InterfaceElo

    Crea una interfaz para que el usuario pueda interactuar 
    con el tablero de ajedrez
    """
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.canvas.place(x = 0, y = 0)
        #Para que el usuario ingrese los valores
        self.entry_img = []
        self.entry = []
        #Para la barra del valor K
        self.images = []
        self.elo = Elo()
        button_info = ["10","20","40", 
                       ("calcular", self.calculate),
                       ("limpiar", self.clean_ratings),
                       ("regresar", self.back),
                       ("home", self.back)]
        super().__init__(canvas, button_info)

    def set_options(self, op, size, x, y):
        """Muestra en pantalla el texto de los datos requeridos
           op - texto de la opciones 
           size - tamaño de la letra
        """
        for i, val in enumerate(op):
            self.canvas.create_text(
                x,
                y + (i*46),
                anchor="nw",
                text=val,
                fill="#000000",
                font=("PTSans Bold", size * -1)
            )

    def get_data(self) -> list:
        """Obtiene la información data por el usuario"""
        data = []
        try:
            for text in self.entry:
                data.append(int(text[1].get()))
        except:
            messagebox.showerror("Error","Los datos deben ser números")
        return data


    def set_text(self):
        """Muestra en pantalla los cuadros de texto donde el
           usuario ingresará los datos"""

        op = ["Rating acual","Número de juegos", "Resultado del torneo", "k"]
        self.set_options(op, 18, 139.0, 185.0)
        for i in range(4):
            self.entry_img.append(PhotoImage(
                file=relative_to_assets("images/elo/texto.png")))
            self.entry.append([self.canvas.create_image(
                467.5,
                193.5 + (i*46),
                image=self.entry_img[i]
            ),
            Entry(
                bd=0,
                bg="#C0E3EF",
                highlightthickness=0
            )])
            self.entry[i][1].place(
                x=363.0,
                y=179.0 + (i*46),
                width=209.0,
                height=27.0
            )

    def set_buttons(self):
        """Muestra en pantalla los adornos de footer y header
         y los la opción de continuar"""

        self.set_footer()
        self.set_header()

        self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/elo/siguiente.png")))
        self.buttons.append(Button(
            image= self.img_buttons[0],
            borderwidth=0,
            highlightthickness=0,
            command=self.click_next,
            relief="flat"
        ))
        self.buttons[0].place(
            x=649.0,
            y=58.0,
            width=40.0,
            height=40.0
        )
    
    def clean(self):
        """Eliminamos todo lo del canvas"""
        super().clean()
        for i in self.entry:
            i[1].destroy()
        self.entry_img = []
        self.entry = []

    def click_next(self):
        """Nos lleva a la siguiente página para calcular el elo"""
        data = self.get_data()
        try:
            if self.elo.validate_data(data):
                info=["Rating acual","Número de juegos", "Resultado del torneo"]
                results=["Rating nuevo", "Desempeño", "Rating Promedio"]
                self.clean()
                self.set_footer()
                self.set_header()
                self.set_players_rating()
                self.set_options(info,14,139,62)
                self.set_options(self.elo.get_initial_info(),14,310,62)
                self.set_options(["Ratings de los oponentes"],14,39,188)
                self.set_options(results,14,412,62)
                self.set_buttons2()
        except:
            messagebox.showerror("Datos inválidos","Por favor llena los campos")

    def set_players_rating(self):
        """Agrega las casillas sufucientes para ingresar el rating de los
         oponentes"""
        x = 0
        y = 0
        for i in range(self.elo.get_games()):
            #Número del jugador
            self.canvas.create_text(
                54.0 + x,
                221.0 + (y * 38),
                anchor="nw",
                text=i+1,
                fill="#000000",
                font=("PTSans Bold", 13 * -1)
            )
            #Recuadro para el rating del jugador
            self.entry_img.append(PhotoImage(
                file=relative_to_assets("images/elo/texto.png")))
            self.entry.append([self.canvas.create_image(
                143.0,
                232.5,
                image=self.entry_img[i]
            ),
            Entry(
                bd=0,
                bg="#C0E3EF",
                highlightthickness=0
            )])
            self.entry[i][1].place(
                x=98.0 + x,
                y=221.0 + (y * 38),
                width=90.0,
                height=21.0
            )
            if (i+1)%8 == 0:
                x += 159
                y = 0
            else:
                y+=1

    def set_buttons2(self):
        """Agrega los botones para calcular, limpiar, regresar
        y home"""
        for i in range(4):
            self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/elo/"+self.button_name[i+3][0] + ".png")))
            self.buttons.append(Button(
                image=self.img_buttons[i],
                borderwidth=0,
                highlightthickness=0,
                command=self.button_name[i+3][1],
                relief="flat"
            ))
 
            self.buttons[i].place(
                x= 561 if i < 2 else 50 + ((i-2) * 620),
                y= 434 + (i*46) if i < 2 else 65,
                width=40 if i > 1 else 117.41,
                height=40 if i > 1 else 29.89
            )
                
    def clean_ratings(self):
        """Limpia los recuadros de rating del oponente"""
        for text in self.entry:
            text[1].delete(0,'end')

    def back(self):
        """Nos regresa a la primera vista del elo
        para ingresar nuevos datos"""
        self.clean()
        self.set_text()
        self.set_buttons()

    def calculate(self):
        """Calcula el rating del jugador y lo muestra en pantalla"""
        self.elo.set_players_rating(self.get_data())
        elo = self.elo.calculate_elo()
        performance = self.elo.calculate_performance()
        self.set_options([elo, performance, self.elo.get_average()],14,550,62)
