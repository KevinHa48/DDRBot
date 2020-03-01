from PIL import Image, ImageDraw, ImageFont
from rinon import rinonsays

def img_txt(text):
    
    xy = (470, 155)
    image = Image.open('rinonbox.jpg')
    font_type = ImageFont.truetype('comic.ttf', 40)
    draw = ImageDraw.Draw(image)

    draw.text(xy, text, font = font_type, fill = (0,0,0))
    image.save('r.png')