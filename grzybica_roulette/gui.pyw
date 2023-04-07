
#! IMPORTING
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
from ctypes import windll
import os, random, ctypes, tkinter.messagebox, shutil

#! VARIABLES
host_wins = False

#! PATHS
current_file_location = os.path.abspath(__file__)
current_file_directory = os.path.dirname(current_file_location)
assets_path = f'{current_file_directory}/assets'
main_path = f'{assets_path}/frame0/'
user_directory = f'{current_file_directory}'
def relative_to_assets(path: str) -> Path:
    return main_path / Path(path)

#! TKINTER GUI
# Window settings
window = Tk()
window.geometry("1181x840")
window.configure(bg = "#000000")
window.iconphoto(False, PhotoImage(file=relative_to_assets('grzybica_roulette_logo.png')))
window.title('GRZYBICA ROULETTE')
canvas = Canvas(
    window,
    bg = "#000000",
    height = 840,
    width = 1181,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

entry_image_1 = PhotoImage(
    file=relative_to_assets("input_img.png"))
entry_bg_1 = canvas.create_image(
    297.5249938964844,
    374.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#5a0000",
    fg="#ffffff",
    highlightthickness=0,
    font=("Times New Roman", 30, "bold"),
    insertbackground="white"
)

entry_1.place(
    x=35.0,
    y=332.0,
    width=487.04998779296875,
    height=83.0
)

#! FUNCTIONS
def startPrograms(e):
    # Variables
    global host_wins, entry_1
    domek_grzybowski_value = int(entry_1.get())
    win_rng = random.randint(0, 2)

    # Get the path to the pendrive
    def get_removable_disk_path():
        drive_bits = windll.kernel32.GetLogicalDrives()
        drives = [chr(65 + i) + ':/' for i in range(26) if (drive_bits >> i) & 1]
        for drive in drives:
            drive_type = windll.kernel32.GetDriveTypeW(ctypes.c_wchar_p(drive))
            if drive_type == 2:
                return drive
        return None

    # Path to the pendrive
    removable_disk_path = get_removable_disk_path()
    
    # Start the actual program if a pendrive is connected.
    if removable_disk_path != None:
        if (win_rng == 0):
            for i in range(0, domek_grzybowski_value):
                os.mkdir(os.path.expandvars(rf'%USERPROFILE%\Desktop\domek_grzybowski_{i}'))
                print("desktop")
        else:
            for i in range(0, domek_grzybowski_value * 2):
                os.mkdir(os.path.expandvars(rf'{removable_disk_path}\domek_grzybowski_{i}'))
                print("pendrive")
    else:
        tkinter.messagebox.showerror(title='Pendrive', message='YOU MUST INSERT YOUR FLASH DRIVE')

    # Delete Grzybica Roulette folder after executing all of the previous stuff
    print(current_file_directory)
    shutil.rmtree(current_file_directory)

# Background image (everything)
image_image_1 = PhotoImage(
    file=relative_to_assets("bg_img.png"))
image_1 = canvas.create_image(
    590.0,
    420.0,
    image=image_image_1
)

start_btn_img = ImageTk.PhotoImage(Image.open(relative_to_assets('start_btn.png')))
start_btn = canvas.create_image(
    275,
    595,
    image=start_btn_img
)
canvas.tag_bind(start_btn, "<Button-1>", startPrograms)


# Final window settings
window.resizable(False, False)
window.mainloop()