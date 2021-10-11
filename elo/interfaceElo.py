from tkinter.constants import S
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
        #Valores dados por el usuario
        self.Ro = 2000 #Rating actual
        self.games = 29 #Número de juegos 
        self.results = 30 #Puntos obtenidos de los juegos
        self.elo = Elo(canvas)
        button_info = ["10","20","40", 
                       ("calcular", self.elo.calculate),
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
                y + (i*36),
                anchor="nw",
                text=val,
                fill="#000000",
                font=("PTSans Bold", size * -1)
            )

    def set_text(self):
        """Muestra en pantalla los cuadros de texto donde el
           usuario ingresará los datos"""

        op = ["Rating acual","Número de juegos", "Resultado del torneo", "k"]
        self.set_options(op, 18, 139.0, 175.0)
        for i in range(3):
            self.entry_img.append(PhotoImage(
                file=relative_to_assets("images/elo/texto.png")))
            self.entry.append([self.canvas.create_image(
                467.5,
                183.5 + (i*36),
                image=self.entry_img[i]
            ),
            Entry(
                bd=0,
                bg="#C0E3EF",
                highlightthickness=0
            )])
            self.entry[i][1].place(
                x=363.0,
                y=169.0 + (i*36),
                width=209.0,
                height=27.0
            )

    def set_k_data(self):
        """Muestra en pantalla un barra que indica el valor de K"""
        for i in range(3):
            self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/elo/"+ self.button_name[i] + ".png")))
            self.buttons.append(Button(
                image=self.img_buttons[i],
                borderwidth=0,
                highlightthickness=0,
                command=self.button_name[i][1],
                relief="flat"
            ))

            self.buttons[i].place(
                x=169.0 + (i * 196),
                y=408.0,
                width=40.4,
                height=37.0
            )

        op = ["barra", "num"]
        for i in range(2):
            self.images.append(PhotoImage(
                file=relative_to_assets("images/elo/"+op[i]+".png")))
            self.images.append(self.canvas.create_image(
                375.0 + (i*10),
                386.0 - (i*5),
                image=self.images[i + (i*1)]
            ))

    def set_buttons(self):
        """Muestra en pantalla los adornos de footer y header
         y los la opción de continuar"""

        self.set_footer()
        self.set_header()

        self.img_buttons.append(PhotoImage(
            file=relative_to_assets("images/elo/siguiente.png")))
        self.buttons.append(Button(
            image= self.img_buttons[3],
            borderwidth=0,
            highlightthickness=0,
            command=self.click_next,
            relief="flat"
        ))
        self.buttons[3].place(
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
        info=["Rating acual","Número de juegos", "Resultado del torneo"]
        results=["Rating nuevo", "Desempeño", "Rating Promedio"]
        value=[self.Ro, self.games, self.results]
        self.clean()
        self.set_footer()
        self.set_header()
        self.set_players_rating()
        self.set_options(info,14,139,62)
        self.set_options(value,14,310,62)
        self.set_options(["Ratings de los oponentes"],14,39,188)
        self.set_options(results,14,412,62)
        self.set_buttons2()

    def set_players_rating(self):
        """Agrega las casillas sufucientes para ingresar el rating de los
         oponentes"""
        x = 0
        y = 0
        for i in range(self.games):
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
        pass

    def back(self):
        """Nos regresa a la primera vista del elo
        para ingresar nuevos datos"""
        self.clean()
        self.set_text()
        self.set_k_data()
        self.set_buttons()
