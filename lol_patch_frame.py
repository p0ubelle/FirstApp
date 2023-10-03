import requests
import re
from PIL import Image, ImageTk
from io import BytesIO
from lol_version import get_lol_version
import customtkinter


lol_v = get_lol_version()

def lol_patch_screen(frame, label):

    url = f"https://www.leagueoflegends.com/fr-fr/news/game-updates/patch-{lol_v}-notes/"
    response = requests.get(url)
    if response.status_code == 200:
        # Find all image URLs in the HTML content using regular expressions
        image_urls = re.findall(r'https://images\.contentstack\.io/.*?\.(?:jpg|png)', response.text)
        if len(image_urls) >= 2:
            # Get the second image URL
            image_url = image_urls[5]

            img_response = requests.get(image_url)
            if img_response.status_code == 200: 
                img_data = BytesIO(img_response.content)
                img = customtkinter.CTkImage(Image.open(img_data), size=(1990,1080))

                label.configure(image=img)
                label.image = img  # Store a reference to avoid garbage collection
                frame.after(100000, lol_patch_screen, frame)  # Fetch the image every 1000ms 



