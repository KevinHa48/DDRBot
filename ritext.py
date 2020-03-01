from PIL import Image, ImageDraw, ImageFont
import textwrap

x = 423

def img_txt(thing):

    y = 150

    image = Image.open('rinonbox.jpg')
    font_type = ImageFont.truetype('comic.ttf', 40)
    font_small = ImageFont.truetype('comic.ttf', 25)
    draw = ImageDraw.Draw(image)

    if len(thing) >= 20:
        lines = textwrap.wrap(thing, width = 35)

        for line in lines:
            width, height = font_small.getsize(line)
            draw.text((x, y), line, font = font_small, fill= (0,0,0))
            y += height
        
        image.save('l.png')

    else:
        draw.text((x, 155), thing, font = font_type, fill = (0,0,0))
        image.save('s.png')