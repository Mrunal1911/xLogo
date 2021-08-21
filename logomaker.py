from PIL import Image, ImageFont, ImageDraw

import random

text = "MESSAGE"

photo_path = "resources/logos"

color= "Blue"

X = "resources/fonts"

pp = "photo_path"

fnt = random.choice(os.listdir(X))

image = Image.open(photo)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(f"{X}/{fnt}", 130)

draw.text((220, 250), text, fill =color, font =font, align ="center")

image.save('output.jpg')

await e.reply(file="output.jpg")
