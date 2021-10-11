from tkinter import messagebox

class Elo:
    def __init__(self) -> None:
        #Valores dados por el usuario
        self.Ro = 0 #Rating actual
        self.games = 0 #Número de juegos 
        self.results = 0 #Puntos obtenidos de los juegos
        self.k = 10
        self.players_rating = []
        self.prom = 0
        self.is_valid = False

    def set_Ro(self, Ro):
        """Verifica el rating del jugador y lo guarda"""
        if Ro > 3000:
            messagebox.showerror("Error","Ingresa un rating menor a 3000")
            self.is_valid = False
        else:
            self.Ro = Ro
            self.is_valid = True

    def set_games(self, games):
        """Verifica el número de juegos y lo guarda"""
        if games > 29:
            messagebox.showerror("Error","El límite de partidas es 29")
            self.is_valid = False
        else:
            self.games = games
            self.is_valid = True

    def set_results(self, results):
        """Verifica el número de juegos ganados y lo guarda"""
        if results > self.games*3:
            messagebox.showerror("Error","El número de partidas jugadas es mayor al de ganadas")
            self.is_valid = False
        else:
            self.Ro = results
            self.is_valid = True

    def set_k(self, k):
        """Guarda la constante k del jugador"""
        self.k = k

    def get_initial_info(self):
        """Regresa la infomación dada en un inicio 
        para hacer los cálculos"""
        return [self.Ro, self.games, self.results]

    def get_we(self):
        """Valor esperado de partidas ganadas"""
        d = self.prom - self.Ro
        return 1 / (1 + 10**(d/400))

    def calculate_elo(self):
        """Regresa el nuevo rating del jugador (Elo)"""
        #Promedio
        self.prom = sum(self.players_rating) / len(self.players_rating)
        return self.Ro + self.k * (self.results - self.get_we())

    def calculate_performance(self):
        """Regresa el rendimiento de un jugador sin tomar 
        en cuenta el valor de k"""
        factor = (self.set_games - self.set_results) / self.set_games
        return len(self.players_rating + 400 * factor)

   