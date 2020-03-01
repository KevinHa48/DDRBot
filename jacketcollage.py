from PIL import Image
#from rinon import song_set
import requests
import io

images = []
size = 512,512

def collager(set_list):

    for song in set_list:
        fd = requests.get(song)
        image_file = io.BytesIO(fd.content)
        im = Image.open(image_file)
        im.thumbnail(size)
        images.append(im)

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('e.png')

