import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('module_2/data/dog.jpeg')
weight = np.array([0.21, 0.72, 0.07]).reshape(1, 1, 3)
gray_image = np.sum(image * weight, axis=2)
print(gray_image[0,0])
plt.imshow(gray_image, cmap='gray')
plt.show()