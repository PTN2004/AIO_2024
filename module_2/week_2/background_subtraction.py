import numpy as np
import cv2
import matplotlib.pyplot as plt

BACKGROUND_IMAGE = "module_2/week_2/data/image_data/GreenBackground.png"
OBJ_IMAGE = "module_2/week_2/data/image_data/Object.png"
NEW_BACKGROUND = "module_2/week_2/data/image_data/NewBackground.jpg"


def load_image(original_background_image_path, obj_image_path, target_background_path, image_size=(678, 381)):
    original_background_image = cv2.imread(original_background_image_path)
    obj_image = cv2.imread(obj_image_path)
    target_background = cv2.imread(target_background_path)

    original_background_image = cv2.resize(
        original_background_image, image_size)
    obj_image = cv2.resize(obj_image, image_size)
    target_background = cv2.resize(target_background, image_size)

    return (original_background_image, obj_image, target_background)


def compute_difference(original_background_image, obj_image):
    difference_image = cv2.absdiff(original_background_image, obj_image)
    return difference_image


def compute_binary_mask(difference_image):
    _, binary_mark = cv2.threshold(
        difference_image, 15, 255, cv2.THRESH_BINARY)
    return binary_mark


def replace_background(threshold=10):
    original_image, obj_image, target_image = load_image(
        BACKGROUND_IMAGE, OBJ_IMAGE, NEW_BACKGROUND)
    difference_image = compute_difference(original_image, obj_image)
    binary_mark = compute_binary_mask(difference_image)
    target = np.where(binary_mark == 0, target_image, obj_image)

    target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)
    return target


result = replace_background()

plt.imshow(result)
plt.show()
