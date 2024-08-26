import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('module_2/data/dog.jpeg')

gray_image = np.array(np.max(image, axis=2)/2 + np.min(image, axis=2)/2)
plt.imshow(gray_image, cmap="gray")
plt.show()