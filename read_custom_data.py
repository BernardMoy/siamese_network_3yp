import os 
import random

def read_custom_data():
    TEST_PATH = "test"

    pairs = []

    # Anchor images are in train/directory/anchor for each directory
    test_path_positive = os.path.join(TEST_PATH, "positive")
    test_path_negative_easy = os.path.join(TEST_PATH, "negative_easy")
    test_path_negative_hard = os.path.join(TEST_PATH, "negative_hard")

    for category in os.listdir(test_path_positive):
        dirs = os.listdir(os.path.join(test_path_positive, category))
        first_dir = os.path.join(test_path_positive, category, dirs[0])
        second_dir = os.path.join(test_path_positive, category, dirs[1])
        pairs.append((first_dir,second_dir, 1))

    for category in os.listdir(test_path_negative_easy):
        dirs = os.listdir(os.path.join(test_path_negative_easy, category))
        first_dir = os.path.join(test_path_negative_easy, category, dirs[0])
        second_dir = os.path.join(test_path_negative_easy, category, dirs[1])
        pairs.append((first_dir,second_dir, 0))

    for category in os.listdir(test_path_negative_hard):
        dirs = os.listdir(os.path.join(test_path_negative_hard, category))
        first_dir = os.path.join(test_path_negative_hard, category, dirs[0])
        second_dir = os.path.join(test_path_negative_hard, category, dirs[1])
        pairs.append((first_dir,second_dir, 0))

    return pairs