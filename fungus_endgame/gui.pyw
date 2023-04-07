
#! IMPORTING
from tkinter import *

#! TKINTER GUI
# Window settings
window = Tk()
window.geometry("787x554")
window.configure(bg = "#FFFFFF")

from main import *

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 554,
    width = 787,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
window.title('Fungus Endgame')
icon = PhotoImage(file = relative_to_assets('fungus-endgame-logo.png'))
window.iconphoto(False, icon)

# Background image
image_image_1 = PhotoImage(
    file=relative_to_assets("bg-fungus-img.png"))
image_1 = canvas.create_image(
    393.0,
    277.0,
    image=image_image_1
)

# Input no. 1
entry_image_1 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_1 = canvas.create_image(
    140.0,
    221.0,
    image=entry_image_1
)
entries[0] = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entries[0].place(
    x=44.0,
    y=209.0,
    width=192.0,
    height=22.0
)

# Input no. 2
entry_image_2 = PhotoImage(
    file=relative_to_assets("input.png"))
entry_bg_2 = canvas.create_image(
    140.0,
    131.0,
    image=entry_image_2
)
entries[1] = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entries[1].place(
    x=44.0,
    y=119.0,
    width=192.0,
    height=22.0
)

# Checkbox no. 1 / "Otwieranie kalkulatora"
button_image_1 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[0] = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(0),
    relief="flat"
)
buttons[0].place(
    x=32.0,
    y=297.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 2 / "Otwieranie kamery"
button_image_2 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[1] = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(1),
    relief="flat"
)
buttons[1].place(
    x=211.0,
    y=297.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 3 / "Otwieranie notatnika"
button_image_3 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[2] = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(2),
    relief="flat"
)
buttons[2].place(
    x=32.0,
    y=329.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 4 / "Pobieranie podarunku"
button_image_4 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[3] = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(3),
    relief="flat"
)
buttons[3].place(
    x=211.0,
    y=329.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 5 / "Zmień rozdzielczość"
button_image_5 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[4] = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(4),
    relief="flat"
)
buttons[4].place(
    x=32.0,
    y=361.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 6 / "Auto-wiadomość"
button_image_6 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[5] = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(5),
    relief="flat"
)
buttons[5].place(
    x=211.0,
    y=361.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 7 / "Hackowanie bazy"
button_image_7 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[6] = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(6),
    relief="flat"
)
buttons[6].place(
    x=211.0,
    y=392.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 8 / "Otwieranie przeglądarki"
button_image_8 = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[7] = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(7),
    relief="flat"
)
buttons[7].place(
    x=32.0,
    y=393.0,
    width=16.0,
    height=16.0
)

# Start button
button_image_9 = PhotoImage(
    file=relative_to_assets("start-btn.png"))
buttons[8] = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=programs,
    relief="flat"
)
buttons[8].place(
    x=32.0,
    y=441.0,
    width=180.0,
    height=36.0
)

# Minimum button
button_image_10 = PhotoImage(
    file=relative_to_assets("min-btn.png"))
buttons[9] = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=minimum,
    relief="flat"
)
buttons[9].place(
    x=32.0,
    y=24.0,
    width=180.0,
    height=36.0
)

# Maximum button
button_image_11 = PhotoImage(
    file=relative_to_assets("max-btn.png"))
buttons[10] = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=maximum,
    relief="flat"
)
buttons[10].place(
    x=228.0,
    y=24.0,
    width=180.0,
    height=36.0
)

# Browse button
button_image_12 = PhotoImage(
    file=relative_to_assets("browse-btn.png"))
buttons[11] = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
buttons[11].place(
    x=228.0,
    y=441.0,
    width=47.0,
    height=36.0
)

# Texts
canvas.create_text(
    32.0,
    84.0,
    anchor="nw",
    text="Domki grzybowskie:",
    fill="#FFFFFF",
    font=("Cabin Regular", 16 * -1)
)
canvas.create_text(
    32.0,
    175.0,
    anchor="nw",
    text="Ilość programów:",
    fill="#FFFFFF",
    font=("Cabin Regular", 16 * -1)
)
canvas.create_text(
    32.0,
    265.0,
    anchor="nw",
    text="Usługi:",
    fill="#FFFFFF",
    font=("Cabin Regular", 16 * -1)
)
canvas.create_text(
    56.0,
    297.0,
    anchor="nw",
    text="Otwieranie kalkulatora",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    329.0,
    anchor="nw",
    text="Otwieranie notatnika",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    360.0,
    anchor="nw",
    text="Zmień rozdzielczość",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    392.0,
    anchor="nw",
    text="Otwieranie przeglądarki",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    235.0,
    297.0,
    anchor="nw",
    text="Otwieranie kamery",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    235.0,
    329.0,
    anchor="nw",
    text="Danie podarunku",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    235.0,
    360.0,
    anchor="nw",
    text="Auto-wiadomość",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    235.0,
    391.0,
    anchor="nw",
    text="Hackowanie bazy",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    32.0,
    524.0,
    anchor="nw",
    text="Owned by Fungus Inc.",
    fill="#FFFFFF",
    font=("Cabin Italic", 12 * -1)
)

# Input reset
entries[0].insert(0, "0")
entries[1].insert(0, "0")

# Final window settings
window.resizable(False, False)
window.mainloop()