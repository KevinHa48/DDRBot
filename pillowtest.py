from PIL import Image
import requests
import io

links = ['https://remywiki.com/images/6/6f/Dancer_in_the_flare.png', 'https://remywiki.com/images/3/30/SigSig_DDR.png', 'https://remywiki.com/images/b/b8/PARANOiA_Revolution.png']
images = []
size = 512,512

for l in links:
    fd = requests.get(l)
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