import pandas as pd 
import os 
import numpy as np
import random
from itertools import combinations


TRAIN_DIR = "products_10k_train_50"
NEGATIVE_MULTIPLIER = 2     # the positive to negative ratio, 2 means the pos to neg ratio is 1:2

def generate_pairs(paths, labels, class_size):
    # create file list 
    TRAIN_PATH = os.path.join(TRAIN_DIR, "data")

    num_positve, num_negative = 0,0

    # labels and paths should have corresponding indices
    # labels represent the class number
    # construct dict 
    class_dict = {}
    for image_path, label in zip(paths, labels):
        # append the image path in the dict
        if label not in class_dict:
            class_dict[label] = []
        class_dict[label].append(image_path)


    pairs_output = []
    labels_output = [] 

    # iterate the key and value of the dict
    for key, value in class_dict.items():
        if len(value) > 1:
            num_positive_added = len(list(combinations(value, 2)))

            # add the positive pair
            # append every distinct combination
            pairs_output.extend([(os.path.join(TRAIN_PATH, a),os.path.join(TRAIN_PATH, b)) for a,b in combinations(value, 2)])
            labels_output.extend([1] * num_positive_added)
            num_positve += num_positive_added


            # add the negative pairs
            for img in value:
                # the average number of negative pairs we need per data equal to (n-1)/2, for a class that has n data in it
                # = nC2/n
                for _ in range(len(value)//2*NEGATIVE_MULTIPLIER):
                    # find another distinct class
                    another_class = ((key + random.randrange(1, class_size)) % class_size)

                    # within that class, choose a random index
                    second_image = random.sample(class_dict[another_class], 1)[0]
                    pairs_output.append((os.path.join(TRAIN_PATH, img), os.path.join(TRAIN_PATH, second_image)))
                    labels_output.append(0)
                    num_negative += 1

    # shuffle the pairs
    combined = list(zip(pairs_output, labels_output))
    random.shuffle(combined)
    pairs_output, labels_output = zip(*combined)
    pairs_output = list(pairs_output)
    labels_output = list(labels_output)

    # output the number of pairs
    print(f"Number of pairs: {len(pairs_output)}")
    print(f"Number of positives: {num_positve}")
    print(f"Number of negatives: {num_negative}")

    # split into train and val
    train_size = int(0.7 * len(pairs_output))

    pairs_train = pairs_output[:train_size]
    labels_train = labels_output[:train_size]
    pairs_val = pairs_output[train_size:]
    labels_val = labels_output[train_size:]

    return np.array(pairs_train), np.array(labels_train), np.array(pairs_val), np.array(labels_val)



LAST_ROW = 1855
def read_data(first_row = 1, last_row = LAST_ROW):

    # read the first 538 rows of the csv file 
    df = pd.read_csv(os.path.join(TRAIN_DIR, "labels_filtered.csv"), header = None, skiprows = 1)
    df_sliced = df.iloc[first_row: last_row]

    # the number of classes is equal to the last class + 1
    num_classes = int(df_sliced.iloc[-1, 1])+1

    # create the labels and files name, according to each row in the dataset
    labels = []
    files = []
    for index, row in df_sliced.iterrows():
        file_name = row[0]
        class_name = int(row[1])
        files.append(file_name)
        labels.append(class_name)

    # generate pairs
    return generate_pairs(files, labels, num_classes)


a,b,c,d = read_data()
print(a)
print(b)