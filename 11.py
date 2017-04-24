import requests
from PIL import Image
import io
import copy

r = requests.get("http://www.pythonchallenge.com/pc/return/cave.jpg",
                 auth=('huge', 'file'))
im = Image.open(io.BytesIO(r.content))
row = [im.getpixel((x + 1, 1)) for x in range(im.width - 1)]

# Making even
even = copy.copy(im)
for x in range(even.width):
    for y in range(even.height):
        if (x + y) % 2 == 1:
            even.putpixel((x, y), 0)

# Making odd
odd = copy.copy(im)
for x in range(odd.width):
    for y in range(odd.height):
        if (x + y) % 2 == 0:
            odd.putpixel((x, y), 0)

# Saving
even.save('11even.png')
odd.save('11odd.png')
