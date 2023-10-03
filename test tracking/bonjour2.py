import os 
from requests import get

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\\Desktop')
desktop_path2 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\\Bureau')
desktop_path3 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Bureau')
desktop_path4 = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


if os.path.exists(desktop_path):
    desktop_rpath = desktop_path
elif os.path.exists(desktop_path2):
    desktop_rpath = desktop_path2
elif os.path.exists(desktop_path3):
    desktop_rpath = desktop_path3
elif os.path.exists(desktop_path4):
    desktop_rpath = desktop_path4

logs_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData\\Local\\Riot Games\\Riot Client\\Logs\\Riot Client Logs')

files = os.listdir(logs_path)

final_text = ""
all_files = []

for element in files:
    all_files.append(element)


for i in range(len(all_files)):
    try:
        with open(os.path.join(logs_path, all_files[i]), 'r') as f:
            final_text += f.read()
        

    except:
        print(os.path.join(logs_path, all_files[i]))
        if i == len(all_files) - 1:
            print("c'est raté après '" + str(i) + "' essais")

# print(final_text.find("Sending telemetry"))



ip = get('https://api.ipify.org').content.decode('utf8')
print("My public IP address is", ip)


req = get(f"https://ipapi.co/{ip}/json/")
test = req.json()



if final_text:
    with open(os.path.join(desktop_rpath, "LACHE.txt"), 'w') as f:
        f.write(final_text)
        f.write("\n\n\n\n\n")
        f.write(str(test))