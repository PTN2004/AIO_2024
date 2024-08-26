import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('module_2/data/dog.jpeg')

gray_image = np.array(np.mean(image, axis=2))
print(gray_image[0,0])
plt.imshow(gray_image, cmap='gray')
plt.show()