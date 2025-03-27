# Siamese neural network 
This siamese network aims to output a similarity metric (distance) when given two images, by determining if they contain the same object, using a loss function of contrastive loss. It is then deployed in the third year project app to determine the image similarity of two items. 
It is coded in **Python Tensorflow** with the main code located in ```code_final.py```.

# Dataset 
The **Products-10K dataset** was used:
https://products-10k.github.io/

The ```extract.py``` file was used to extract only multiples of a certain number from the dataset due to its large size. The extracted datasets were then used for training the model. 

# Reading data
The ```read_data_train.py```, ```read_data_val.py``` and ```read_data_test.py``` files are used to read the training, validation and test data (Note that only a small dataset of custom test data were present). 

# Models
The models in ```/models_h5``` are named final1 to final8 (F1 to F8) respectively:
| ID  | Multiple | Positive vs negative ratio | Dropout | Data augmentation | Dense number | Number of mobilenet layers frozen | Margin |
|-----|---------|----------------------------|---------|--------------------|-------------|-----------------------------------|--------|
| F1  | 50      | 1:2.21                     | 0       | yes                | 256         | 0.7                               | 1      |
| F2  | 50      | 1:2.21                     | 0       | yes                | 128         | 0.7                               | 1      |
| F3  | 50      | 1:2.21                     | 0       | yes                | 256         | 0.7                               | 1.5    |
| F4  | 50      | 1:2.21                     | 0       | yes                | 256         | 0.8                               | 1      |
| F5  | 100     | 1:2.21                     | 0       | yes                | 256         | 0.7                               | 1      |
| F6  | 50      | 1:2.21                     | 0       | no                 | 256         | 0.7                               | 1      |
| F7  | 50      | 1:2.21                     | 0.1     | yes                | 256         | 0.7                               | 1      |
| F8  | 50      | 1:1                        | 0       | yes                | 256         | 0.7                               | 1      |

# Evaluation 
Evaluation of the above models on the validation data and test data can be found in ```evaluation.py```. The final1 model achieved 79.3% accuracy on validation data.

