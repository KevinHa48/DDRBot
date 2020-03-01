from PIL import Image
import requests
from io import BytesIO

#Creating a blank white image for size experimenting purposes
blank_width = 1024
blank_height = 768
meu = Image.open('meutosend.png')

#Grabbing the image from the link the user puts
def meumeu(img_link):
    template = Image.new('RGB', (blank_width, blank_height), color = (255, 255, 255))
    
    response = requests.get(img_link)
    user_img = Image.open(BytesIO(response.content))
    user_img.thumbnail((650, 650), Image.ANTIALIAS)

    template.paste(user_img, (27, 55))
    template.paste(meu, mask = meu)

    template.save('m.png')


