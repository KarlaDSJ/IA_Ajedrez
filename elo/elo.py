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
    62.0,
    anchor="nw",
    text="Raiting acual",
    fill="#000000",
    font=("PTSans Regular", 14 * -1)
)

canvas.create_text(
    139.0,
    128.0,
    anchor="nw",
    text="Resultado del torneo",
    fill="#000000",
    font=("PTSans Regular", 14 * -1)
)

canvas.create_text(
    39.0,
    188.0,
    anchor="nw",
    text="Raitings de los oponentes",
    fill="#000000",
    font=("PTSans Bold", 14 * -1)
)

canvas.create_text(
    139.0,
    95.0,
    anchor="nw",
    text="Número de juegos",
    fill="#000000",
    font=("PTSans Regular", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_1 = canvas.create_image(
    143.0,
    232.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_1.place(
    x=98.0,
    y=221.0,
    width=90.0,
    height=21.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("images/ola_top.png"))
image_1 = canvas.create_image(
    385.0,
    10.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("images/ola_down.png"))
image_2 = canvas.create_image(
    385.0,
    552.0,
    image=image_image_2
)

canvas.create_text(
    290.0,
    60.0,
    anchor="nw",
    text="1800",
    fill="#000000",
    font=("PTSans Regular", 13 * -1)
)

canvas.create_text(
    290.0,
    93.0,
    anchor="nw",
    text="21",
    fill="#000000",
    font=("PTSans Regular", 13 * -1)
)

canvas.create_text(
    54.0,
    221.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_2 = canvas.create_image(
    143.0,
    270.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_2.place(
    x=98.0,
    y=259.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    259.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_3 = canvas.create_image(
    143.0,
    308.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_3.place(
    x=98.0,
    y=297.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    297.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_4 = canvas.create_image(
    143.0,
    346.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_4.place(
    x=98.0,
    y=335.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    335.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_5 = canvas.create_image(
    143.0,
    384.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_5.place(
    x=98.0,
    y=373.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    373.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_6 = canvas.create_image(
    143.0,
    422.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_6.place(
    x=98.0,
    y=411.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    411.0,
    anchor="nw",
    text="6",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_7 = canvas.create_image(
    143.0,
    460.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_7.place(
    x=98.0,
    y=449.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    449.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_8 = canvas.create_image(
    143.0,
    498.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_8.place(
    x=98.0,
    y=487.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    54.0,
    487.0,
    anchor="nw",
    text="8",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_9 = canvas.create_image(
    302.0,
    232.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_9.place(
    x=257.0,
    y=221.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    221.0,
    anchor="nw",
    text="9",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_10 = canvas.create_image(
    302.0,
    270.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_10.place(
    x=257.0,
    y=259.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    259.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_11 = canvas.create_image(
    302.0,
    308.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_11.place(
    x=257.0,
    y=297.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    297.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_12 = canvas.create_image(
    302.0,
    346.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_12.place(
    x=257.0,
    y=335.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    335.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_13 = canvas.create_image(
    302.0,
    384.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_13.place(
    x=257.0,
    y=373.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    373.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_14 = canvas.create_image(
    302.0,
    422.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_14.place(
    x=257.0,
    y=411.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    411.0,
    anchor="nw",
    text="6",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_15 = canvas.create_image(
    302.0,
    460.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_15.place(
    x=257.0,
    y=449.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    449.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_16 = canvas.create_image(
    302.0,
    498.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_16.place(
    x=257.0,
    y=487.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    213.0,
    487.0,
    anchor="nw",
    text="8",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_17 = canvas.create_image(
    461.0,
    232.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_17.place(
    x=416.0,
    y=221.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    221.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_18 = canvas.create_image(
    461.0,
    270.5,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_18.place(
    x=416.0,
    y=259.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    259.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_19 = canvas.create_image(
    461.0,
    308.5,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_19.place(
    x=416.0,
    y=297.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    297.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_20 = canvas.create_image(
    461.0,
    346.5,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_20.place(
    x=416.0,
    y=335.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    335.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_21 = canvas.create_image(
    620.0,
    232.5,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_21.place(
    x=575.0,
    y=221.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    531.0,
    221.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_22 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_22 = canvas.create_image(
    620.0,
    270.5,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_22.place(
    x=575.0,
    y=259.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    531.0,
    259.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_23 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_23 = canvas.create_image(
    620.0,
    308.5,
    image=entry_image_23
)
entry_23 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_23.place(
    x=575.0,
    y=297.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    531.0,
    297.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_24 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_24 = canvas.create_image(
    620.0,
    346.5,
    image=entry_image_24
)
entry_24 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_24.place(
    x=575.0,
    y=335.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    531.0,
    335.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_25 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_25 = canvas.create_image(
    461.0,
    384.5,
    image=entry_image_25
)
entry_25 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_25.place(
    x=416.0,
    y=373.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    373.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_26 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_26 = canvas.create_image(
    621.0,
    384.5,
    image=entry_image_26
)
entry_26 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_26.place(
    x=576.0,
    y=373.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    532.0,
    373.0,
    anchor="nw",
    text="29",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_27 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_27 = canvas.create_image(
    461.0,
    422.5,
    image=entry_image_27
)
entry_27 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_27.place(
    x=416.0,
    y=411.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    411.0,
    anchor="nw",
    text="6",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_28 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_28 = canvas.create_image(
    461.0,
    460.5,
    image=entry_image_28
)
entry_28 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_28.place(
    x=416.0,
    y=449.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    449.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

entry_image_29 = PhotoImage(
    file=relative_to_assets("images/elo/texto.png"))
entry_bg_29 = canvas.create_image(
    461.0,
    498.5,
    image=entry_image_29
)
entry_29 = Entry(
    bd=0,
    bg="#C0E3EF",
    highlightthickness=0
)
entry_29.place(
    x=416.0,
    y=487.0,
    width=90.0,
    height=21.0
)

canvas.create_text(
    372.0,
    487.0,
    anchor="nw",
    text="24",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

canvas.create_text(
    290.0,
    126.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("PTSans Regular", 13 * -1)
)

canvas.create_text(
    412.0,
    62.0,
    anchor="nw",
    text="Raiting nuevo",
    fill="#000000",
    font=("PTSans Bold", 14 * -1)
)

canvas.create_text(
    412.0,
    128.0,
    anchor="nw",
    text="Raiting Promedio ",
    fill="#000000",
    font=("PTSans Bold", 14 * -1)
)

canvas.create_text(
    412.0,
    95.0,
    anchor="nw",
    text="Desempeño",
    fill="#000000",
    font=("PTSans Bold", 14 * -1)
)

canvas.create_text(
    562.0,
    60.0,
    anchor="nw",
    text="1800",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

canvas.create_text(
    562.0,
    93.0,
    anchor="nw",
    text="21",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

canvas.create_text(
    562.0,
    126.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("PTSans Bold", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("images/elo/calcular.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=561.0001831054688,
    y=434.0,
    width=117.407470703125,
    height=29.888092041015625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("images/elo/limpiar.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=561.0,
    y=480.0,
    width=117.407470703125,
    height=29.888092041015625
)


button_image_4 = PhotoImage(
    file=relative_to_assets("images/elo/regresar.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=46.0,
    y=58.0,
    width=40.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("images/home.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=650.0,
    y=58.0,
    width=40.0,
    height=40.0
)

window.resizable(False, False)
window.mainloop()