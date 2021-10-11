#from config import relative_to_assets
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

def relative_to_assets(path: str):
    return "./assets/"+path

window = Tk()

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

canvas.place(x = 0, y = 0)
canvas.create_text(
    139.0,
    175.0,
    anchor="nw",
    text="Raiting acual",
    fill="#000000",
    font=("PTSans Bold", 18 * -1)
)

canvas.create_text(
    139.0,
    244.0,
    anchor="nw",
    text="Resultado del torneo",
    fill="#000000",
    font=("PTSans Bold", 18 * -1)
)

canvas.create_text(
    139.0,
    208.0,
    anchor="nw",
    text="Número de juegos",
    fill="#000000",
    font=("PTSans Bold", 18 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("images/ola_down.png"))
image_1 = canvas.create_image(
    385.0,
    552.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_1 = canvas.create_image(
    467.5,
    183.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_1.place(
    x=363.0,
    y=169.0,
    width=209.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_2 = canvas.create_image(
    467.5,
    219.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_2.place(
    x=363.0,
    y=205.0,
    width=209.0,
    height=27.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_3 = canvas.create_image(
    467.5,
    255.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_3.place(
    x=363.0,
    y=241.0,
    width=209.0,
    height=27.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("images/elo/siguiente.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=649.0,
    y=69.0,
    width=40.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("images/elo/10.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=169.0,
    y=408.0,
    width=41.0,
    height=37.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("images/elo/20.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=365.0,
    y=408.0,
    width=41.0,
    height=37.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("images/elo/40.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=541.0,
    y=408.0,
    width=41.0,
    height=37.0
)

canvas.create_text(
    139.0,
    301.0,
    anchor="nw",
    text="K",
    fill="#000000",
    font=("PTSans Bold", 18 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("images/elo/barra.png"))
image_2 = canvas.create_image(
    375.0,
    386.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("images/elo/num.png"))
image_3 = canvas.create_image(
    385.0,
    381.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("images/ola_top.png"))
image_4 = canvas.create_image(
    385.0,
    10.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
