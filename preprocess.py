import cv2 
import tensorflow as tf 
from remove_bg import remove_bg

# Read an image from path and resize it 
def resize_image(image_path):
    # Convert Tensor to string
    if isinstance(image_path, tf.Tensor):
        image_path = image_path.numpy().decode("utf-8")  # Convert bytes to string

    img = cv2.imread(image_path)
    img = cv2.imread(image_path)
    img = cv2.resize(img, (155, 220))  # Resize first
    return img

# preprocess an image given its path
def preprocess(image_path):
    # first resize the image 
    img_resized = resize_image(image_path)

    # then remove the bg 
    img_no_bg = remove_bg(img_resized) 

    # Convert to tensor
    img = tf.convert_to_tensor(img_no_bg, dtype=tf.float32)
    img = tf.image.resize(img, (155, 220))  # Resize to 105x105
    img = img[:, :, :3]  # Keep 3 channels
    img = img / 255.0  # Scale image between 0 and 1
    return img 

