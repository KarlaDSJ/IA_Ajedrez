from tkinter import messagebox
from ..common.config import db

class CardHolder:
    """ cardHolder
    
    Clase que me permite calcular el rating de un jugador
    utilizando el sistema de puntuación Elo, y su desempeño
    """
    def __init__(self) -> None:
        self.cursor = db.cursor()
        self.all_cards = []

    def add_card(self, titulo, tablero, descripcion):
        """Guarda el rating de los oponentes"""
        sql = "INSERT INTO jugadas(titulo, tablero, descripcion) \
        VALUES ('{0}','{1}','{2}')".format(titulo, tablero, descripcion)
        try:
            self.cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Information","Agregado con éxito")
            return self.get_all_cards()
        except:
            db.rollback()

    def delete_card(self, id):
        """Elimina una fila de la base de datos
        id - de la fila a borrar"""
        sql = "DELETE FROM jugadas WHERE id={0}".format(id)
        try:
            self.cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Information","Eliminado con éxito")
            return self.get_all_cards()
        except:
            db.rollback()

    def update_card(self, id, titulo, tablero, descripcion):
        """Actualiza una jugada"""
        sql = " UPDATE jugadas SET titulo ='{0}',tablero ='{1}',\
        descripcion = '{2}'  WHERE id = {3}".format(titulo, tablero, descripcion,id)
        try:
            self.cursor.execute(sql)
            db.commit()
            messagebox.showinfo("Information","Actualizado con éxito")
            return self.get_all_cards()
        except:
            db.rollback()

    def get_all_cards(self):
        """Regresa toda la información de las jugadas
        en una lista """

        sql = "SELECT * FROM jugadas"
        self.cursor.execute(sql)
        self.all_cards = self.cursor.fetchall() #Resultados en una lista
        
        return self.all_cards
