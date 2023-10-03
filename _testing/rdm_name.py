import os
import random

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def random_name():
    is_good = False
    while is_good == False:
        zz = ""
        for _ in range (9):
            zz += random.choice(alphabet)

        if zz.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            pass
        else:
            return zz


roaming_folder = os.getenv('APPDATA')

app_folder = os.path.join(roaming_folder, "poubelle27")
if not os.path.exists(app_folder):
    os.makedirs(app_folder)

settings_file = os.path.join(app_folder, random_name() + ".txt")


# write
with open(settings_file, 'w') as f:
    f.write('Your settings data here')


# read
with open(settings_file, 'r') as f:
    settings_data = f.read()
    print(settings_data)



