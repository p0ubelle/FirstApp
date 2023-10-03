import os




def startup(file_name, path, content):
    user_name = os.getlogin()
    startup_path = f'C:\\Users\\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\test.bat'

    with open(startup_path, "w") as startup_file:
        startup_file.write("helo")