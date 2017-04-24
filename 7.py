import requests
from lxml import etree
from PIL import Image
import io

r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.html')
parser = etree.HTMLParser()
html = etree.fromstring(r.text, parser=parser)
r = requests.get(''.join(['http://www.pythonchallenge.com/pc/def/',
                         html.xpath('//img/@src')[0]]))
image = Image.open(io.BytesIO(r.content))
imageW = image.size[0]
imageH = image.size[1]
halfwayUp = imageH // 2

row = [image.getpixel((x, halfwayUp)) for x in range(0, imageW, 7)]
text = ''.join([chr(x[0]) for x in row])
print(text)
answer = ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
print(answer)
