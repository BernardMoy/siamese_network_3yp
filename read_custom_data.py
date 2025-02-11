import os 
import random

def read_custom_data():
    TRAIN_PATH = "train"

    positive_pairs_train = []
    negative_pairs_train = []

    # Anchor images are in train/directory/anchor for each directory
    for category in os.listdir(TRAIN_PATH):
        anchor_dir = os.path.join(TRAIN_PATH, category, "anchor")
        positive_dir = os.path.join(TRAIN_PATH, category, "positive")
        negative_dir = os.path.join(TRAIN_PATH, category, "negative")

        anchor_list = [os.path.join(anchor_dir, f) for f in os.listdir(anchor_dir)]
        positive_list = [os.path.join(positive_dir, f) for f in os.listdir(positive_dir)]
        negative_list = [os.path.join(negative_dir, f) for f in os.listdir(negative_dir)]

        # Within each category directory, match each anchor with each positive and negative 
        positive_pairs_train += [(a, p, 1) for a in anchor_list for p in positive_list]
        negative_pairs_train += [(a, n, 0) for a in anchor_list for n in negative_list]

    data_raw_train = positive_pairs_train + negative_pairs_train 

    return data_raw_train