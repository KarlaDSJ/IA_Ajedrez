from tkinter.constants import X
from config import relative_to_assets
from tkinter import PhotoImage

class Piece():
    def __init__(self, canvas, x, y, name) -> None:
        self.canvas = canvas
        #Coordenadas
        self.x = x
        self.x = y
        #Nombre de la pieza
        self.name = name
        #Img de la pieza
        self.image = 0

    def set_image(self, color, back):
        piece = self.name+color+back
        self.image_down_img = PhotoImage(
            file=relative_to_assets(piece+".png"))

    def set_coord(self, x, y):
        self.x = x
        self.x = y
        #Falta modificar las imágenes
    
    def get_coord(self):
        return [self.x, self.y]



"""
#Botón para agregar un alfil (negro)
button_image_7 = PhotoImage(
    file=relative_to_assets("image_64.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Alfil N"),
    relief="flat"
)
button_7.place(
    x=360.0,
    y=43.0,
    width=43.0,
    height=43.0
)

#Botón para agregar una torre (negro)
button_image_8 = PhotoImage(
    file=relative_to_assets("image_37.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Torre N"),
    relief="flat"
)
button_8.place(
    x=321.0,
    y=43.0,
    width=43.0,
    height=43.0
)

#Botón para agregar un rey (negro)
button_image_9 = PhotoImage(
    file=relative_to_assets("image_40.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Rey N"),
    relief="flat"
)
button_9.place(
    x=234.0,
    y=43.0,
    width=45.0,
    height=43.0
)

#Botón para agregar un peón (negro)
button_image_10 = PhotoImage(
    file=relative_to_assets("image_44.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Peón N"),
    relief="flat"
)
button_10.place(
    x=452.0,
    y=43.0,
    width=43.0,
    height=43.0
)

#Botón para agregar una reina (negro)
button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Reina N"),
    relief="flat"
)
button_11.place(
    x=279.0,
    y=43.0,
    width=42.0,
    height=43.0
)

#Botón para agregar un caballo (negro)
button_image_12 = PhotoImage(
    file=relative_to_assets("image_60.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Caballo N"),
    relief="flat"
)
button_12.place(
    x=409.0,
    y=43.0,
    width=42.0,
    height=43.0
)

#Botón para agregar/seleccionar una pieza
button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Agregar"),
    relief="flat"
)

button_21 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Agregar"),
    relief="flat"
)
button_13.place(
    x=188.0,
    y=43.0,
    width=50.0,
    height=50.0
)

button_21.place(
    x=184.0,
    y=475.0,
    width=50.0,
    height=50.0
)

#Botón para agregar un alfil (blanco)
button_image_14 = PhotoImage(
    file=relative_to_assets("image_66.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Alfil B"),
    relief="flat"
)
button_14.place(
    x=360.0,
    y=479.0,
    width=43.0,
    height=42.0
)

#Botón para borrar/seleccionar una pieza (negras)
button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Borrar"),
    relief="flat"
)

button_22 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Borrar"),
    relief="flat"
)

button_15.place(
    x=496.0,
    y=44.0,
    width=40.0,
    height=40.0
)

button_22.place(
    x=496.0,
    y=479.0,
    width=40.0,
    height=40.0
)

#Botón para agregar una torre (blanco)
button_image_16 = PhotoImage(
    file=relative_to_assets("image_39.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Torre B"),
    relief="flat"
)
button_16.place(
    x=321.0,
    y=479.0,
    width=43.0,
    height=42.0
)

#Botón para agregar un rey (blanco)
button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Rey B"),
    relief="flat"
)
button_17.place(
    x=234.0,
    y=479.0,
    width=45.0,
    height=42.0
)

#Botón para agregar una reina (blanco)
button_image_18 = PhotoImage(
    file=relative_to_assets("image_58.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Reina B"),
    relief="flat"
)
button_18.place(
    x=276.0,
    y=479.0,
    width=43.0,
    height=42.0
)

#Botón para agregar una reina (blanco)
button_image_19 = PhotoImage(
    file=relative_to_assets("image_62.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Caballo B"),
    relief="flat"
)
button_19.place(
    x=409.0,
    y=479.0,
    width=43.0,
    height=42.0
)

#Botón para agregar un peón (blanco)
button_image_20 = PhotoImage(
    file=relative_to_assets("image_52.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Peón B"),
    relief="flat"
)
button_20.place(
    x=453.0,
    y=479.0,
    width=44.0,
    height=42.0
)"""

