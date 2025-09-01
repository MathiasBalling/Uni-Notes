# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Introduction to Image Processing with Python
# ### Image Processing (RM1-VIS)
# ### University of Southern Denmark

# %%
import numpy as np
import matplotlib.pyplot as plt
import skimage
import math

# %%
image = skimage.data.astronaut()
imGray = skimage.color.rgb2gray(image)

# plt.imshow(imGray)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


# %% [markdown]
# ### 1. Rotate image in pi/2 steps


# %%
# image: input grayscale image
# rot: the number of pi/2 rotations to perform (right-hand coordinate system)
def im_rotate(image, rot):
    h, w = image.shape[:2]
    rotated_image = np.zeros_like(image)
    angle = np.pi / 2 * rot  # multiples of 90 degrees

    # rotation matrix (inverse)
    cos_a, sin_a = np.cos(-angle), np.sin(-angle)
    cx, cy = h // 2, w // 2  # center

    for i in range(h):
        for j in range(w):
            # coords relative to center
            x = i - cx
            y = j - cy
            # inverse rotate
            src_x = int(round(x * cos_a - y * sin_a + cx))
            src_y = int(round(x * sin_a + y * cos_a + cy))

            if 0 <= src_x < h and 0 <= src_y < w:
                rotated_image[i, j] = image[src_x, src_y]
    return rotated_image


# %%
# rotate 90 degrees
# plt.imshow(im_rotate(imGray, 1))
# plt.show()

# %%
# rotate 180 degrees
# plt.imshow(im_rotate(imGray, 2))
# plt.show()


# %% [markdown]
# ### 2. Rotate image with interpolation

# %% [markdown]
# Implement a function which rotates grayscale images by a certain angle. Use bilinear interpolation.
#
# Tip: You can use nearest neighbor interpolation first during development.


# %%
# image: input grayscale image
# angle: the rotation angle in radians (right hand coordinate system)
# padding: the pixel value to use in unoccupied new image regions (background)
def im_rotate(image, angle, padding, interpolation="nearest_neighbor"):
    h, w = image.shape[:2]
    rotated_image = np.zeros_like(image)
    rotated_image[:] = padding

    # rotation matrix (inverse)
    cos_a, sin_a = np.cos(-angle), np.sin(-angle)
    cx, cy = h // 2, w // 2  # center

    for i in range(h):
        for j in range(w):
            # coords relative to center
            x = i - cx
            y = j - cy

            # inverse rotate
            src_x = x * cos_a - y * sin_a + cx
            src_y = x * sin_a + y * cos_a + cy

            # Do cases for nearest neighbor and bilinear interpolation
            if interpolation == "nearest_neighbor":
                src_x = int(round(src_x))
                src_y = int(round(src_y))
                if 0 <= src_x < h and 0 <= src_y < w:
                    rotated_image[i, j] = image[src_x, src_y]
                continue
            elif interpolation == "bilinear":
                # Bilinear interpolation
                x0, y0 = int(np.floor(src_x)), int(np.floor(src_y))
                x1, y1 = x0 + 1, y0 + 1

                dx, dy = src_x - x0, src_y - y0

                if 0 <= x0 < h and 0 <= y0 < w and 0 <= x1 < h and 0 <= y1 < w:
                    top = (1 - dy) * image[x0, y0] + dy * image[x0, y1]
                    bottom = (1 - dy) * image[x1, y0] + dy * image[x1, y1]
                    value = (1 - dx) * top + dx * bottom
                    rotated_image[i, j] = value
                continue
            elif interpolation == "bicubic":
                # Bicubic interpolation
                pass
    return rotated_image


# %%
# rotate 40 degrees
plt.imshow(im_rotate(imGray, 40 * math.pi / 180, 0, "nearest_neighbor"))
plt.imshow(im_rotate(imGray, 40 * math.pi / 180, 0, "bilinear"))
plt.show()
