import cv2
import matplotlib.pyplot as plt

# Load the images
background_image = cv2.imread('frontPreview.jpg')  # Replace 'background_image.jpg' with your background image file path


# Display the result
cv2.imshow('Result', background_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert them from BGR to RGB
img1 = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

# Visualize First Image
plt.imshow(img1) 
plt.show()


