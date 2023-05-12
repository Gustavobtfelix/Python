from PIL import Image, ImageDraw, ImageFont

fontsize = 14

font = ImageFont.truetype('./fontes/SHARONSANS-LIGHT.OTF', fontsize, encoding='utf-8')
fontBold = ImageFont.truetype('./fontes/SHARONSANS-BOLD.OTF', fontsize, encoding='utf-8')


# Create a new image onto which the text will be added
image = Image.new(mode='RGB', size=(613, 953), color='#ffaa00')
# Create an ImageDraw object onto which the font text will be placed
draw = ImageDraw.Draw(im=image)
# Draw the text onto our image
draw.text(xy=(512, 128), text="Gustavo Batista Felix", font=font, fill='black', anchor='mm')
# Open the image via system standard image viewer
image.show()