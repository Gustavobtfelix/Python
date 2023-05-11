import cv2
import matplotlib.pyplot as plt

# Load the images
background_image = cv2.imread('cracha.png')  # Replace 'background_image.jpg' with your background image file path
overlay_image = cv2.imread('cara.jpg')  # Replace 'overlay_image.jpg' with your overlay image file path

# Resize the overlay image to the desired dimensions
overlay_image = cv2.resize(overlay_image, (355, 355), interpolation=cv2.INTER_AREA)

# Define the position to paste the overlay image
x1, y1 = 129, 242
x2, y2 = x1 + overlay_image.shape[1], y1 + overlay_image.shape[0]

# Paste the overlay image onto the background image
background_image[y1:y2, x1:x2] = overlay_image

# Display the result
cv2.imshow('Result', background_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Convert them from BGR to RGB
img1 = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

# Visualize First Image
plt.imshow(img1) #768x1024
plt.show()



# new_image_path = 'result_image2.jpg'  # Path to save the resulting image
# cv2.imwrite(new_image_path, background_image)





