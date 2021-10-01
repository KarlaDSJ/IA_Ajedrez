import numpy as np
from config import relative_to_assets
from tkinter import PhotoImage

class Board():
    """
    Board

    Permite al usuario interactuar con un tablero de ajedrez:
        > Crear un tablero en blanco
        > Recrear una jugada
        > Mover piezas
        > Crear un tablero para iniciar el juego
    """
    
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.board = np.zeros((8, 8)) # Tablero de ceros
        self.img_box = [] # Imagen de la casilla

    def set_board_num(self):
        """Agrega los números de las coordenadas del tablero"""
        for i in range(8):
            self.canvas.create_text(
                177.0,
                421.0 - (43 * i),
                anchor="nw",
                text=str(i + 1),#Números
                fill="#000000",
                font=("PTSans Bold", 14 * -1)
            )

    def set_board_letters(self):
        """Agrega las letras de las coordenadas del tablero"""
        letters  = list(map(chr, range(97, 105)))
        for i in range(8):
            #Letras
            self.canvas.create_text(
                205.0 + (43 * i),
                453.0,
                anchor="nw",
                text= letters[i], #Letras
                fill="#000000",
                font=("PTSans Bold", 14 * -1)
            )
    
    def set_empty_board(self):
        """Muestra en pantalla un tablero de ajedrez vacío"""
        num = 0
        for y in range(8):
            for x in range(8):
                self.img_box.append(PhotoImage(
                    file=relative_to_assets(str(num * 1)+".png")))
                self.board[x][y] = self.canvas.create_image(
                    212.53106689453125 + 43 * y,
                    127.07342529296875 + 43 * x,
                    image = self.img_box[x+y]
                )
                num = not num



"""------------------Piezas inicio del juego---------------------"""

"""image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    515.51806640625,
    127.07342529296875,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    212.53106689453125,
    127.07342529296875,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    211.99002075195312,
    430.3017883300781,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    514.9770202636719,
    429.75830078125,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    385.12548828125,
    127.07342529296875,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    472.2342224121094,
    170.54702758789062,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    515.51806640625,
    170.54702758789062,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    385.66650390625,
    170.54702758789062,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    428.95037841796875,
    170.54702758789062,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    299.0987854003906,
    170.54702758789062,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    342.38262939453125,
    170.54702758789062,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    212.53106689453125,
    170.54702758789062,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    255.81494140625,
    170.54702758789062,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=relative_to_assets("image_49.png"))
image_49 = canvas.create_image(
    428.4093017578125,
    386.2847595214844,
    image=image_image_49
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    385.12548828125,
    386.2847595214844,
    image=image_image_50
)

image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    514.9770202636719,
    386.2847595214844,
    image=image_image_51
)

image_image_52 = PhotoImage(
    file=relative_to_assets("image_52.png"))
image_52 = canvas.create_image(
    471.6932067871094,
    386.2847595214844,
    image=image_image_52
)

image_image_53 = PhotoImage(
    file=relative_to_assets("image_53.png"))
image_53 = canvas.create_image(
    341.841552734375,
    386.2847595214844,
    image=image_image_53
)

image_image_54 = PhotoImage(
    file=relative_to_assets("image_54.png"))
image_54 = canvas.create_image(
    298.5577697753906,
    386.2847595214844,
    image=image_image_54
)

image_image_55 = PhotoImage(
    file=relative_to_assets("image_55.png"))
image_55 = canvas.create_image(
    255.27386474609375,
    386.2847595214844,
    image=image_image_55
)

image_image_56 = PhotoImage(
    file=relative_to_assets("image_56.png"))
image_56 = canvas.create_image(
    211.99002075195312,
    386.2847595214844,
    image=image_image_56
)

image_image_57 = PhotoImage(
    file=relative_to_assets("image_57.png"))
image_57 = canvas.create_image(
    342.38262939453125,
    127.07342529296875,
    image=image_image_57
)

image_image_58 = PhotoImage(
    file=relative_to_assets("image_58.png"))
image_58 = canvas.create_image(
    341.30059814453125,
    429.75830078125,
    image=image_image_58
)

image_image_59 = PhotoImage(
    file=relative_to_assets("image_59.png"))
image_59 = canvas.create_image(
    255.81494140625,
    127.07342529296875,
    image=image_image_59
)

image_image_60 = PhotoImage(
    file=relative_to_assets("image_60.png"))
image_60 = canvas.create_image(
    472.2342224121094,
    127.07342529296875,
    image=image_image_60
)

image_image_61 = PhotoImage(
    file=relative_to_assets("image_61.png"))
image_61 = canvas.create_image(
    471.6932067871094,
    429.75830078125,
    image=image_image_61
)

image_image_62 = PhotoImage(
    file=relative_to_assets("image_62.png"))
image_62 = canvas.create_image(
    255.27386474609375,
    430.3017883300781,
    image=image_image_62
)

image_image_63 = PhotoImage(
    file=relative_to_assets("image_63.png"))
image_63 = canvas.create_image(
    428.95037841796875,
    127.07342529296875,
    image=image_image_63
)

image_image_64 = PhotoImage(
    file=relative_to_assets("image_64.png"))
image_64 = canvas.create_image(
    299.0987854003906,
    127.07342529296875,
    image=image_image_64
)

image_image_65 = PhotoImage(
    file=relative_to_assets("image_65.png"))
image_65 = canvas.create_image(
    298.01666259765625,
    429.75830078125,
    image=image_image_65
)

image_image_66 = PhotoImage(
    file=relative_to_assets("image_66.png"))
image_66 = canvas.create_image(
    428.4093017578125,
    429.75830078125,
    image=image_image_66
)

image_image_67 = PhotoImage(
    file=relative_to_assets("image_67.png"))
image_67 = canvas.create_image(
    386.12548828125,
    429.75830078125,
    image=image_image_67
)"""