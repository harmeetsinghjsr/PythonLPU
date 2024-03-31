from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import matplotlib.pyplot as plt
import numpy as np
import cv2

#reading image
img = imread('cat.jpg')
plt.axis("off")
plt.imshow(img)
print(img.shape)
#resizing  image for hog()
resized_img = resize(img, (128 * 4, 64 * 4))
plt.axis("off")
plt.imshow(resized_img)
plt.show()
print(resized_img.shape)
#using hog()
fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, mchannel_axis=-1)
print(fd.shape)
print(hog_image.shape)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")
plt.show()
#saving resized image
plt.imsave("resized_img.jpg", resized_img)
plt.imsave("hog_image.jpg", hog_image, cmap="gray")

#using LBP
def get_pixel(imag, center, x, y):
    new_value = 0
    try:
        if imag[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value
#calculating local pattern
def lbp_calculated_pixel(imag, x, y):
    center = imag[x][y]
    val_ar = []
    val_ar.append(get_pixel(imag, center, x - 1, y - 1))
    val_ar.append(get_pixel(imag, center, x - 1, y))
    val_ar.append(get_pixel(imag, center, x - 1, y + 1))
    val_ar.append(get_pixel(imag, center, x, y + 1))
    val_ar.append(get_pixel(imag, center, x + 1, y + 1))
    val_ar.append(get_pixel(imag, center, x + 1, y))
    val_ar.append(get_pixel(imag, center, x + 1, y - 1))
    val_ar.append(get_pixel(imag, center, x, y - 1))
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val
#applying LBP to image
path = 'cat.jpg'
img_bgr = cv2.imread(path, 1)
height, width, _ = img_bgr.shape
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_lbp = np.zeros((height, width), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
plt.imshow(img_bgr)
plt.show()
plt.imshow(img_lbp, cmap="gray")
plt.show()
plt.imsave("lbp1.jpg", img_bgr)
plt.imsave("lbp2.jpg", img_lbp)
print("LBP Program is finished")