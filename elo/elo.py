from tkinter import messagebox
from tkinter.constants import NUMERIC

class Elo:
    """ ELO
    
    Clase que me permite calcular el rating de un jugador
    utilizando el sistema de puntuación Elo, y su desempeño
    """
    def __init__(self) -> None:
        #Valores dados por el usuario
        self.Ro = 0 #Rating actual
        self.games = 0 #Número de juegos 
        self.results = 0 #Puntos obtenidos de los juegos
        self.k = 10
        self.players_rating = []
        self.prom = 0
        self.is_valid = False

    def set_players_rating(self, players):
        """Guarda el rating de los oponentes"""
        self.players_rating = players

    def validate_data(self, data) -> bool:
        """Verifica que los datos iniciales sean válidos

            data[0] - rating inicial
            data[1] - número de juegos
            data[2] - resultado de juegos
            data[3] - k (constante según las partidas)
        """
        if data[0] > 3000:
            messagebox.showerror("Error","Ingresa un rating menor a 3000")
            self.is_valid = False
        elif data[1] > 29:
            messagebox.showerror("Error","El límite de partidas es 29")
            self.is_valid = False
        elif data[2] > data[1]:
            messagebox.showerror("Error","El número de partidas jugadas es mayor al de ganadas")
            self.is_valid = False
        else:
            self.Ro = data[0]
            self.games = data[1]
            self.results = data[2]
            self.k = data[3]
            self.is_valid = True

        return self.is_valid

    def get_initial_info(self) -> list:
        """Regresa la infomación dada en un inicio 
        para hacer los cálculos"""
        return [self.Ro, self.games, self.results]

    def get_average(self) -> int:
        """Regresa el promedio de los ratings de los oponentes"""
        return self.prom

    def get_games(self) -> int:
        """Regresa el número de partidas de ajedrez"""
        return self.games

    def get_we(self) -> int:
        """Valor esperado de partidas ganadas"""
        d = self.prom - self.Ro
        return 1 / (1 + 10**(d/400))

    def calculate_elo(self) -> int:
        """Regresa el nuevo rating del jugador (Elo)"""
        #Promedio
        self.prom = sum(self.players_rating) / len(self.players_rating)
        self.prom = float("{:.2f}".format(self.prom))
        elo = self.Ro + self.k * (self.results - self.get_we())
        return float("{:.2f}".format(elo))

    def calculate_performance(self) -> int:
        """Regresa el rendimiento de un jugador sin tomar 
        en cuenta el valor de k"""
        factor = (self.games - self.results) / self.games
        performance = len(self.players_rating) + 400 * factor 
        return float("{:.2f}".format(performance))

   