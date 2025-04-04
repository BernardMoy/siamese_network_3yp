"""
Extract the relevant rows from the training data
because it is too large
"""

import pandas as pd 
import shutil
import os 

df = pd.read_csv(r"C:\Users\holog\Downloads\train.csv")

# extract rows of multiple of a number
MULTIPLE = 197
filtered_df = df[df["class"] % MULTIPLE == 0]    # Extract multiples only
# If 50 is used as multiple for training data
# Then there are 9690//50 = 193 rows for training (0, 50, 100...)
# Select the next number with LCM(n, 50) > 9690 which is 197 
# 197 will be used as the multiple for validation data


for file_name in filtered_df['name']:
        source_path = os.path.join(r"C:\Users\holog\Downloads\train", file_name)
        destination_path = os.path.join(r"C:\Users\holog\Downloads\train_filtered\data", file_name)
        
        # Check if file exists before copying
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied: {file_name}")

filtered_df = filtered_df[filtered_df['name'].apply(lambda x: os.path.exists(os.path.join(r"C:\Users\holog\Downloads\train", x)))]  # Remove rows with files that doesnt exist
filtered_df["class"] = filtered_df["class"] // MULTIPLE  # Scale down the class number so that negative pairs can be generated by (+1) mod ...
filtered_df.to_csv(r"C:\Users\holog\Downloads\train_filtered\labels_filtered.csv", index=False)  # Output new csv file 
