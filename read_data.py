import pandas as pd 
import os 
import numpy as np

def read_data():
    # read the first 538 rows of the csv file 
    df = pd.read_csv("products_10k_classes.csv", header = None, skiprows = 1)
    df_sliced = df.iloc[:538]

    # the number of classes is equal to the last class + 1
    num_classes = int(df_sliced.iloc[-1, 1])+1
    classes = [i for i in range(num_classes)]
    print(num_classes)

    # create file list 
    TRAIN_PATH = "products_10k"

    # shuffle the rows 
    df_shuffled = df_sliced.sample(frac=1)

    # create the labels and files name, according to each row in the shuffled dataset
    labels = []
    files = []
    print(df_shuffled)
    for index, row in df_shuffled.iterrows():
        file_name = os.path.join(TRAIN_PATH, str(row[0]))
        print(row[1])
        class_name = int(row[1])
        files.append(file_name)
        labels.append(class_name)

    return np.array(labels), np.array(files), np.array(classes)

labels, files, classes = read_data()
print(labels)
print(files)