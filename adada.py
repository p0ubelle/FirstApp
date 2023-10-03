from tkinter import *
from winsound import *
import os
user_name = os.getlogin()

root = Tk() # create tkinter window
startup_path = os.makedirs(f'C:\\Users\\{user_name}\\AppData\\Roaming\\p0ubelle')

with open(startup_path, "w") as startup_file:
    startup_file.write("helo")
root.mainloop()