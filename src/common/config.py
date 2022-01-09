from pathlib import Path
import pymysql
from tkinter import Tk, Canvas

"""
Configuración 

Establece la ruta para encontrar las imágenes
La conexión con la base de datos
"""

db = pymysql.connect(host='localhost',
        user='localhost', 
        password = "pruebatest",
        db='ChessCard',)

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

window = Tk()
#Define el tamaño de la ventana
window.geometry("770x562")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 562,
    width = 770,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def relative_to_assets(path: str) -> Path:
    """Define la ruta de las imágenes"""
    return ASSETS_PATH / Path(path)