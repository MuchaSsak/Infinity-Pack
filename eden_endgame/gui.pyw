
#! IMPORTING
from tkinter import Tk, Canvas, Button, PhotoImage

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
window.title('Eden Endgame')
icon = PhotoImage(file = relative_to_assets('eden-endgame-logo.png'))
window.iconphoto(False, icon)

# Background image
bg_eden_img = PhotoImage(
    file=relative_to_assets("bg-eden-img.png"))
image_1 = canvas.create_image(
    393.0,
    277.0,
    image=bg_eden_img
)

# Start button
start_btn_img = PhotoImage(
    file=relative_to_assets("start-btn.png"))
buttons[0] = Button(
    image=start_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=startPrograms,
    relief="flat"
)
buttons[0].place(
    x=32.0,
    y=371.0,
    width=180.0,
    height=36.0
)

# Browse button
browse_btn_img = PhotoImage(
    file=relative_to_assets("browse-btn.png"))
buttons[1] = Button(
    image=browse_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=selectPath,
    relief="flat"
)
buttons[1].place(
    x=228.0,
    y=371.0,
    width=47.0,
    height=36.0
)

# Checkbox no. 1 / "Usuwanie "Grzybków Przyczajonych""
checkbox_1_img = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[2] = Button(
    image=checkbox_1_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(2),
    relief="flat"
)
buttons[2].place(
    x=32.0,
    y=224.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 2 / "Usuwanie "Grzybków Przyczajonych""
checkbox_2_img = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[3] = Button(
    image=checkbox_2_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(3),
    relief="flat"
)
buttons[3].place(
    x=32.0,
    y=255.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 3 / "Usuwanie podarunku"
checkbox_3_img = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[4] = Button(
    image=checkbox_3_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(4),
    relief="flat"
)
buttons[4].place(
    x=32.0,
    y=287.0,
    width=16.0,
    height=16.0
)

# Checkbox no. 4 / "Usuwanie wiadomosc.txt w output_path"
checkbox_4_img = PhotoImage(
    file=relative_to_assets("checkbox.png"))
buttons[5] = Button(
    image=checkbox_4_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: switchProgram(5),
    relief="flat"
)
buttons[5].place(
    x=32.0,
    y=319.0,
    width=16.0,
    height=16.0
)

# Minimum button
minimum_btn_img = PhotoImage(
    file=relative_to_assets("min-btn.png"))
buttons[6] = Button(
    image=minimum_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=minimum,
    relief="flat"
)
buttons[6].place(
    x=32.0,
    y=120.0,
    width=180.0,
    height=36.0
)

# Maximum button
maximum_btn_img = PhotoImage(
    file=relative_to_assets("max-btn.png"))
buttons[7] = Button(
    image=maximum_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=maximum,
    relief="flat"
)
buttons[7].place(
    x=228.0,
    y=120.0,
    width=180.0,
    height=36.0
)

# Texts
canvas.create_text(
    32.0,
    523.0,
    anchor="nw",
    text="Owned by Fungus Inc.",
    fill="#FFFFFF",
    font=("Cabin Italic", 12 * -1)
)
canvas.create_text(
    56.0,
    255.0,
    anchor="nw",
    text="Usuwanie plików z auto-startu",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    225.0,
    anchor="nw",
    text="Usuwanie “Grzybków Przyczajonych”",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    287.0,
    anchor="nw",
    text="Usuwanie podarunku",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    56.0,
    319.0,
    anchor="nw",
    text="Usuwanie wiadomosc.txt w output_path",
    fill="#FFFFFF",
    font=("Cabin Regular", 12 * -1)
)
canvas.create_text(
    32.0,
    192.0,
    anchor="nw",
    text="Usługi:",
    fill="#FFFFFF",
    font=("Cabin Regular", 16 * -1)
)
canvas.create_text(
    32.0,
    38.0,
    anchor="nw",
    text="Eden Endgame",
    fill="#ED5831",
    font=("Cabin Bold", 48 * -1)
)

# Final windows settings
window.resizable(False, False)
window.mainloop()