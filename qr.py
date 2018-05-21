import qrcode
from PIL import Image, ImageDraw, ImageFont

for i in range(0, 101):
    img = qrcode.make('http://happysaver.ddns.net/sound/' + str(i) + '.wav', error_correction=qrcode.constants.ERROR_CORRECT_Q)
    img = img.convert('RGBA')
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y] == (0, 0, 0, 255):
                pixdata[x, y] = (234, 15, 107, 255)

    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.load_default().font
    font = ImageFont.truetype("Pixel Millennium.ttf", 70)
    w, h = font.getsize(str(i))
    draw.rectangle(((width-w)/2 - 5, (height-h)/2, (width-w)/2 + 5 + w, (height-h)/2 + h + 8), fill='white')
    draw.text(((width-w)/2 + 5, (height-h)/2), str(i), font=font, fill="#F4bfd1")
    img.save(str(i) + '.png')
