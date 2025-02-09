import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_bg(img):
    # Create mask and models for GrabCut
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Define a rectangle for GrabCut
    rect = (10, 10, img.shape[1] - 10, img.shape[0] - 10)

    # Apply GrabCut to remove bg 
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Create mask where 1 = foreground, 0 = background
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

    # Fill the background with white
    white_bg = np.full_like(img, 255) 
    result = img*mask2[:, :, np.newaxis] + white_bg*(1 - mask2[:, :, np.newaxis])

    return result
