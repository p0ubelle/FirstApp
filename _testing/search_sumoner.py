import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x700")
app.resizable(False,False)



def button_function():
    print("button pressed")


search_image = customtkinter.CTkImage(Image.open("search.png"))

text = customtkinter.CTkLabel(master=app, text="Entrez votre nom", font=customtkinter.CTkFont(size=15, weight="normal"))
text.place(x=500, y=280, anchor=customtkinter.CENTER)


saisi = customtkinter.CTkTextbox(master=app, width=170, height=1, activate_scrollbars=False)
saisi.place(x=500, y=330, anchor=customtkinter.CENTER)


combobox_1 = customtkinter.CTkSegmentedButton(app, values=["NA", "EUW", "EUN", "KR"], fg_color="#34323A")
combobox_1.place(x=500, y=380, anchor=customtkinter.CENTER)


button = customtkinter.CTkButton(master=app, command=button_function, border_spacing=2, image=search_image, text="")
button.place(x=675, y=330, anchor=customtkinter.CENTER)


combobox_1.set("EUW")
app.mainloop() 