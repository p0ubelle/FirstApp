import os
import time

import pygame
import customtkinter
from PIL import Image
import tkinter
from tkvideo import tkvideo

from lol_patch_frame import lol_patch_screen
from lol_summoner import get_summoner_info
from lol_version import get_lol_version

# from customtkinter.windows.widgets.theme import ThemeManager

user_name = os.getlogin()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        

        os.system("cls")
        os.system("ipconfig")

        self.title("")
        self.geometry("1152x648")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


        # load images with light and dark mode image
        video_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\\video")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\\launcher_image")
        music_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images\\music")
        rank_image_path = os.path.join(os.path.dirname(os   .path.realpath(__file__)), "images\\rank_image")

        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "lotus_logo.png")), size=(55, 55))
        self.home_banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_banner.png")), size=(140, 150))

        # navigation frame image
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_light.png")), size=(41, 41))
        self.chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "chat_light.png")), size=(41, 41))
        self.add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "add_user_light.png")), size=(41, 41))
        self.lol_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "lol_light.png")), size=(41, 41))
        self.music_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "music_light.png")), size=(41, 41))
        self.social_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "social_light.png")), size=(41, 41))
        self.shell_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "shell_light.png")), size=(51, 51))
        self.settings_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings_light.png")), size=(41, 41))
      
        ##


        self.search_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "search_light.png")), size=(22, 22))

        self.intro_music = os.path.join(music_path, "intro.wav")
        self.intro_video = os.path.join(video_path, "intro.mp4")


        # RANKED IMAGES
        self.rank_image_list = []
        for images in os.listdir(rank_image_path):
            self.images = customtkinter.CTkImage(Image.open(os.path.join(rank_image_path, images)))
            self.rank_image_list.append(self.images)



        # navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_logo = customtkinter.CTkLabel(self.navigation_frame, image=self.logo_image, text="", anchor=customtkinter.CENTER,compound="left")
        self.navigation_frame_logo.grid(row=0, column=0, padx=10, pady=10)
    



        #NAVIGATION_FRAME//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        # Home
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.home_image, anchor=customtkinter.CENTER, command=self.home_button_event); self.under_logo_frame = customtkinter.CTkFrame(self.navigation_frame, width=35, height=3, fg_color="grey")


        # Lol
        self.lol_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.lol_image, anchor=customtkinter.CENTER, command=self.lol_button_event)


        # Music
        self.music_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.music_image, anchor=customtkinter.CENTER, command=self.music_button_event)
        
        

        # Social
        self.social_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.social_image, anchor=customtkinter.CENTER, command=self.social_button_event)


        # shell
        self.shell_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.shell_image, anchor=customtkinter.CENTER, command=self.shell_button_event)


         # Other
        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="", width=45, 
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.settings_image, anchor=customtkinter.CENTER, command=self.settings_button_event)

        
        # Resolution
        # self.resolution_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,values=["1152x648", "960x540", "640x480", "fullscreen"],  #RESOLUTION
        #                                             command=self.change_resolution_mode)

        self.under_logo_frame.grid(row=1, column=0)
        self.home_button.grid(row=2, column=0, sticky="ew")
        self.lol_button.grid(row=3, column=0, sticky="ew")
        self.music_button.grid(row=4, column=0, sticky="ew")
        self.social_button.grid(row=5, column=0, sticky="ew")

        
        self.shell_button.grid(row=6, column=0, sticky="sew")
        self.settings_button.grid(row=7, column=0, sticky="sew")

        # self.resolution_mode_menu.grid(row=6, column=0, padx=20, pady=0, sticky="s")

        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        


        self.update()

        #_______________________________HOME__________________________________________
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # BANNER CENTRAL
        self.home_banner_frame = customtkinter.CTkLabel(self.home_frame, text="", image=self.home_banner_image)
        self.home_banner_frame.place(x=(self.winfo_width() - self.navigation_frame.winfo_width()) /2, y= self.home_banner_image._size[1] /1.4, anchor=customtkinter.CENTER)
        
        # Invisible frame
        self.invisible_frame = customtkinter.CTkFrame(self.home_frame, width=0)
        self.invisible_frame.grid(row=0, column=0, padx=0, pady=10)
        
        # button
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=0, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="right")
        self.home_frame_button_2.grid(row=1, column=1, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="top")
        self.home_frame_button_3.grid(row=1, column=2, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=1, column=3, padx=20, pady=10)



        #_______________________________lol_______________________________________
        self.lol_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=(self.winfo_width() - self.navigation_frame.winfo_width()), height=self.winfo_height())

        self.lol_frame_sum_name_entry = customtkinter.CTkEntry(self.lol_frame)
        self.lol_frame_search_button = customtkinter.CTkButton(self.lol_frame, command=self.get_summoner_rank, image=self.search_image, text="", width=22, height=22, corner_radius=5)
        self.lol_frame_region_combo = customtkinter.CTkSegmentedButton(self.lol_frame, values=["euw1", "kr", "na1", "eun1"], width=70)
        self.lol_frame_region_combo.set("euw1")

        self.lol_frame_rank_image = customtkinter.CTkLabel(self.lol_frame, text="")
        self.lol_frame_sum_rank_label = customtkinter.CTkLabel(self.lol_frame, text="waiting for name ... ", font=customtkinter.CTkFont(size=20), bg_color="transparent", fg_color="transparent")
        self.lol_frame_sum_name_label = customtkinter.CTkLabel(self.lol_frame, text="")
        self.lol_frame_lol_version_label = customtkinter.CTkLabel(self.lol_frame, text="lol version : " + get_lol_version())



        self.lol_frame_sum_name_entry.place(relx=0.48, rely=0.20, anchor=customtkinter.CENTER)
        self.lol_frame_region_combo.place(relx=0.48, rely=0.25, anchor=customtkinter.CENTER)
        self.lol_frame_search_button.place(relx=0.57, rely=0.20, anchor=customtkinter.CENTER)

        self.lol_frame_rank_image.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
        self.lol_frame_sum_rank_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.lol_frame_lol_version_label.place(relx=0.9, rely=0.92, anchor=customtkinter.CENTER)

        # self.lol_frame_sum_rank_label.after(300, lol_patch_screen, self.lol_frame, self.lol_frame_sum_rank_label)



        #_______________________________social__________________________________________
        self.social_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # button
        self.social_frame_button_1 = customtkinter.CTkLabel(self.social_frame, text="EMPLACEMENT = social")
        self.social_frame_button_1.pack()



        #_______________________________music__________________________________________
        self.music_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # button
        self.music_frame_button_1 = customtkinter.CTkLabel(self.music_frame, text="EMPLACEMENT = musique")
        self.music_frame_button_1.pack()



        #_______________________________shell__________________________________________
        self.shell_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # button
        self.shell_frame_button_1 = customtkinter.CTkLabel(self.shell_frame, text="EMPLACEMENT = shell")
        self.shell_frame_button_1.pack()



        #_______________________________settings____________________________________________
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=(self.winfo_width() - self.navigation_frame.winfo_width()), height=self.winfo_height())
        
        self.settings_frame_startup_button = customtkinter.CTkCheckBox(self.settings_frame, text="start with Windows")
        self.settings_frame_option2_button = customtkinter.CTkCheckBox(self.settings_frame, text="toggle fullscreen", command=self.change_resolution_mode)
        self.settings_frame_color_theme_combo = customtkinter.CTkComboBox(self.settings_frame, values=["green", "blue", "dark-blue"]) # command=self.set_default_color_theme


        self.settings_frame.grid_columnconfigure(0, minsize=350)
        self.settings_frame.grid_rowconfigure(0, minsize=200)

        #column 1                                                                           #column 2
        self.settings_frame_startup_button.grid(column=1, pady=5, row=1, sticky="w")    ;   self.settings_frame_color_theme_combo.grid(column=2, pady=5, row=1, sticky="w")    
        self.settings_frame_option2_button.grid(column=1, pady=5, row=2, sticky="w")



        # select default frame
        self.select_frame_by_name("home")






    # def startup(self):
    #     start_with_windows = self.settings_frame_startup_button.get()
    #     if start_with_windows == True:
            




    def file_explorer(file_name, path, content):
        user_name = os.getlogin()  # Replace with your actual username

        user_name_path = f'C:\\Users\\{user_name}\\AppData\\Roaming\\p0ubelle'
        user_data_path = os.path.join(user_name_path, path)
        os.makedirs(user_data_path, exist_ok=True)

        file_path = os.path.join(user_data_path, file_name)
        with open(file_path, 'w') as file:
            file.write(content)


    file_explorer("text.txt", "C:\\Users\\rapha\\AppData\\Roaming\\poubelle27", "bonjourzzaa")



    def get_summoner_rank(self):
            
        rank_list = {
            "IRON"      : (1, 122, 74),
            "BRONZE"    : (2, 149, 95),
            "SILVER"    : (3, 129, 99),
            "GOLD"      : (4, 138, 116),
            "PLATINUM"  : (5, 135, 115),
            "EMERALD"   : (6, 150, 112),
            "DIAMOND"   : (7, 141, 88)
        }

        try:
            sum_name = self.lol_frame_sum_name_entry.get()
            region = self.lol_frame_region_combo.get()

            sum_stat_json, sum_name, sum_icon = get_summoner_info(sum_name, region)

            # use the result
            self.image_rank = rank_list.get(sum_stat_json["tier"])
            self.image_rank_tk = self.rank_image_list[self.image_rank[0]]


            self.image_rank_tk.configure(size=(self.image_rank[1], self.image_rank[2]))         ;        self.lol_frame_rank_image.configure(image=self.image_rank_tk)
            
            self.lol_frame_sum_rank_label.configure(text="Solo queue: " + str(sum_stat_json["tier"]) + "-" + str(sum_stat_json["rank"]) + str(sum_stat_json["leaguePoints"]) + ' lp\n on "' + str(sum_name) + '"')
            self.lol_frame_sum_name_label.configure(text=str(sum_name))
        
        
        except:
            self.lol_frame_sum_rank_label.configure(text='No solo queue rank found for "' + sum_name + '" in ' + str(region.capitalize()))
            self.image_rank_tk_unranked =  self.rank_image_list[0]         ;        self.image_rank_tk_unranked.configure(size=(rank_list.get("IRON")[1], rank_list.get("IRON")[2]))         
            self.lol_frame_rank_image.configure(image=self.image_rank_tk_unranked)




    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.lol_button.configure(fg_color=("gray75", "gray25") if name == "lol" else "transparent")
        self.social_button.configure(fg_color=("gray75", "gray25") if name == "social" else "transparent")
        self.music_button.configure(fg_color=("gray75", "gray25") if name == "music" else "transparent")
        self.shell_button.configure(fg_color=("gray75", "gray25") if name == "shell" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")


        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "lol":
            self.lol_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.lol_frame.grid_forget()

        if name == "social":
            self.social_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.social_frame.grid_forget()

        if name == "music":
            self.music_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.music_frame.grid_forget()

        if name == "shell":
            self.shell_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.shell_frame.grid_forget()

        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()



    def home_button_event(self):
        self.select_frame_by_name("home")

    def lol_button_event(self):
        self.select_frame_by_name("lol")

    def social_button_event(self): 
        self.select_frame_by_name("social")

    def music_button_event(self): 
        self.select_frame_by_name("music")

    def shell_button_event(self): 
        self.select_frame_by_name("shell")

    def settings_button_event(self): 
        self.select_frame_by_name("settings")


    # def set_default_color_theme(self, color):
    #     ThemeManager.load_theme(color)
    #     print(color)


    def change_resolution_mode(self):
        if  self.settings_frame_option2_button.get() == True:
            self.attributes("-fullscreen", True)
        else:
            self.attributes("-fullscreen", False)
    

if __name__ == "__main__":

    app = App()
    app.mainloop()
