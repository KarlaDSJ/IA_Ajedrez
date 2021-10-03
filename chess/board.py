from .box import Box

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
        self.board = [] # Tablero compuesto de casillas

        #Para el historial de las piezas del tablero
        self.white_pieces = []
        self.black_pieces = []

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
        for x in range(8):
            for y in range(8):
                if len(self.board) < 64:
                    #Si el tablero ya contiene todas las casillas
                    box = Box(self.canvas, x, y, num * 1)
                    box.set_image()
                    box.show_on_screen()
                    self.board.append(box)
                else:
                    #Si existen las casillas modificamos su imagen
                    self.board[(8*x)+y].set_piece("","")
                num = not num
            num = not num

    def rotate(self):
        print("Tablero rotado")

    def save(self):
        print("Tabero guardado")
    
    def save_play_history(self):
        print("historial de tiradas")

    def set_fila(self, x_i, x_j, color):
        """
            Pone las 2 filas de piezas de un colar para
            el inicio del juego

            x_i - número de la fila donde está el rey 
            x_j - número de la fila de peones
            color - color de las piezas
        """
        pieces = ["T","C","A","D","R","A","C","T"]

        for i in range(8):
            self.board[i+x_i].set_piece(pieces[i], color)
        
        for i in range(8):
            self.board[i+x_j].set_piece("p", color)

    def set_initial_board(self):
        """Piezas inicio del juego"""
        self.set_fila(0,1*8,"N")
        self.set_fila(7*8,6*8,"B")