
#! IMPORTING
import os, subprocess, re, tkinter.filedialog, ctypes
from tkinter import *
from pathlib import Path

#! PATHS
current_file_location = os.path.abspath(__file__)
current_file_directory = os.path.dirname(current_file_location)
assets_path = f'{current_file_directory}/assets'
main_path = f'{assets_path}/frame0/'
user_directory = f'{current_file_directory}'
def relative_to_assets(path: str) -> Path:
    return main_path / Path(path)

#! VARIABLES
# Options to switch
delete_hidden_grzyb = False
delete_autostart_files = False
delete_podarunek = False
delete_wiadomosc_bat = False
FILE_ATTRIBUTE_HIDDEN = 0x2

# Arrays
switchable_programs = [delete_hidden_grzyb, delete_autostart_files, delete_podarunek, delete_wiadomosc_bat]
buttons = []
for i in range(0, 8):
    buttons.append(None)

# Processes for Eden to kill
process_names = ["cmd.exe", "notepad.exe", "PhotosApp.exe", "calc.exe", "CalculatorApp.exe", "msedge.exe", "microsoft.windows.camera:", "WindowsCamera.exe", "WindowsTerminal.exe"]

# Changing checkboxes' image
off = PhotoImage(
    file=relative_to_assets("checkbox.png"))
on = PhotoImage(
    file=relative_to_assets("checkbox_clicked.png"))

#! FUNCTIONS
# Switching the True/False statement of a particular program (insert the array index of the program in buttons[])
def switchProgram(buttonNumber):
    global buttons, switchable_programs
    if switchable_programs[buttonNumber - 2] == True:
        switchable_programs[buttonNumber - 2] = False
        buttons[buttonNumber].config(image=off)
    else:
        switchable_programs[buttonNumber - 2] = True
        buttons[buttonNumber].config(image=on)

# Starting the whole operation
def startPrograms():

    # Delete essential files
    deleteFilesEssential(user_directory)

    if os.name == "nt":
        # Deleting files
        if switchable_programs[0] == True:
            deletePrzyczajonyGrzyb(user_directory)
        if switchable_programs[1] == True:
            startup_path = os.path.expandvars('%USERPROFILE%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
            deleteAutostart(startup_path)
        if switchable_programs[2] == True:
            deletePodarunek(user_directory)
        if switchable_programs[3] == True:
            deleteWiadomoscTxt(user_directory)

        # Killing tasks
        for name in process_names:
            os.system(f"taskkill /F /IM {name}")
        os.system(f'taskkill /F /IM explorer.exe')
        subprocess.Popen("explorer.exe")

# Deleting files (customizable)
def deleteFilesEssential(output_path):
    for root, dirs, files in os.walk(output_path):
        for file in files:
            filepath = os.path.join(root, file)
            if not ctypes.windll.kernel32.GetFileAttributesW(filepath) & FILE_ATTRIBUTE_HIDDEN and re.search(r'grzyb', file, re.IGNORECASE):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            if not ctypes.windll.kernel32.GetFileAttributesW(dirpath) & FILE_ATTRIBUTE_HIDDEN and re.search(r'grzyb', dir, re.IGNORECASE):
                os.rmdir(os.path.join(root, dir))

def deletePrzyczajonyGrzyb(output_path):
    for root, dirs, files in os.walk(output_path):
        for file in files:
            if re.search(r'grzyb', file, re.IGNORECASE):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if re.search(r'grzyb', dir, re.IGNORECASE):
                os.rmdir(os.path.join(root, dir))

def deleteAutostart(autostart_path):
    for root, dirs, files in os.walk(autostart_path):
        for file in files:
            if re.search(r'skull\.png|wiadomosc\.bat', file, re.IGNORECASE):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if re.search(r'skull\.png|wiadomosc\.bat', dir, re.IGNORECASE):
                os.rmdir(os.path.join(root, dir))

def deletePodarunek(output_path):
    for root, dirs, files in os.walk(output_path):
        for file in files:
            if re.search(r'podarunek\.jpg', file, re.IGNORECASE):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if re.search(r'podarunek\.jpg', dir, re.IGNORECASE):
                os.rmdir(os.path.join(root, dir))

def deleteWiadomoscTxt(output_path):
    for root, dirs, files in os.walk(output_path):
        for file in files:
            if re.search(r'wiadomosc\.txt', file, re.IGNORECASE):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if re.search(r'wiadomosc\.txt', dir, re.IGNORECASE):
                os.rmdir(os.path.join(root, dir))

# Selecting the output path
def selectPath():
    global user_directory
    user_directory = tkinter.filedialog.askdirectory()
    print(user_directory)

# Set all options to minimum/maximum
def minimum():
    global switchable_programs, buttons
    for i in range(0, 4):
        switchable_programs[i] = False
    for i in range(2, 6):
        buttons[i].config(image=off)
def maximum():
    global switchable_programs, buttons
    for i in range(0, 4):
        switchable_programs[i] = True
    for i in range(2, 6):
        buttons[i].config(image=on)