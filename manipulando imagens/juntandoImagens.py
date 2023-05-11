import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the images
background_image = cv2.imread('background_image.jpg')  # Replace 'background_image.jpg' with your background image file path
overlay_image = cv2.imread('overlay_image.jpg')  # Replace 'overlay_image.jpg' with your overlay image file path

# Resize the overlay image to the desired dimensions
overlay_image = cv2.resize(overlay_image, (355, 355), interpolation=cv2.INTER_AREA)

# Define the position to paste the overlay image
x1, y1 = 129, 242
x2, y2 = x1 + overlay_image.shape[1], y1 + overlay_image.shape[0]

# Paste the overlay image onto the background image
background_image[y1:y2, x1:x2] = overlay_image

# Display the result
# cv2.imshow('Result', background_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()  

#this is extra necessary for working with pillow:

# Paste the overlay image onto the background image
result_image = np.copy(background_image)
result_image[y1:y2, x1:x2] = overlay_image

# Convert the image from BGR to RGB
result_image_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

# Convert the NumPy array to PIL Image
result_image_pil = Image.fromarray(result_image_rgb)

# Display the result
# result_image_pil.show()
# plt.imshow(result_image_rgb) 
# plt.show()


