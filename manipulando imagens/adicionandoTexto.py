from PIL import Image, ImageDraw, ImageFont

fontsize = 58

font = ImageFont.truetype('./fontes/SHARONSANS-LIGHT.OTF', fontsize, encoding='utf-8')
fontBold = ImageFont.truetype('./fontes/SHARONSANS-BOLD.OTF', fontsize, encoding='utf-8')

# Create a new image onto which the text will be added
image = Image.new(mode='RGB', size=(613, 953), color='#ffaa00')

# Create an ImageDraw object onto which the font text will be placed
draw = ImageDraw.Draw(image)

# Define the text and font properties
text = "Gustavo"
text_width, text_height = draw.textsize(text, font=font)

# Calculate the x coordinates for centering the text
x = (image.width - (text_width // 2)) // 2
y = 128

# Draw the text onto our image
draw.text(xy=(x, y), text=text, font=font, fill='black', anchor='mm') # mm = middle middle

# Open the image via system standard image viewer
image.show()

# y = 753

# # Draw the text onto our image
# draw.text(xy=(x, y), text=text, font=fontBold, fill='white', anchor='mm')
# draw.text(xy=(x, 813), text='Felix', font=font, fill='white', anchor='mm')
