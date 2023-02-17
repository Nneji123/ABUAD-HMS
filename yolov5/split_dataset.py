'''
This script is used to split the dataset into train, val and test sets.

'''

import os
import shutil
import numpy as np
from sklearn.model_selection import train_test_split

def divide_dataset(images_dir, annotations_dir, train_dir, val_dir, test_dir, test_size=0.2, val_size=0.2):
    """
    The divide_dataset function divides the dataset into train, val, and test sets.
    The function takes in a directory of images and a directory of annotations as inputs.
    It returns three directories: train_dir, val_dir, and test_dir. 
    train_dir contains the training set (images + annotations). 
    val_dir contains the validation set (images + annotations). 
    test_dir contains the testing set (images + annotations).

    Args:
        images_dir: Specify the directory where the images are stored
        annotations_dir: Specify the path to the directory containing all of the annotations for our dataset
        train_dir: Specify the path to the directory where you want to save your training data
        val_dir: Specify a directory where validation images and labels are stored
        test_dir: Specify where the test images are
        test_size: Split the data into a train and test set
        val_size: Set the size of the validation dataset (20% in this case)

    Returns:
        The train, val and test directories
    """
    image_filenames = [filename for filename in os.listdir(images_dir) if filename.endswith(".jpg")]
    image_filenames = np.array(image_filenames)
    
    train_filenames, test_filenames, _, _ = train_test_split(image_filenames, image_filenames, test_size=test_size)
    train_filenames, val_filenames, _, _ = train_test_split(train_filenames, train_filenames, test_size=val_size / (1 - test_size))
    
    if not os.path.exists(os.path.join(train_dir, "images")):
        os.makedirs(os.path.join(train_dir, "images"))
    if not os.path.exists(os.path.join(train_dir, "labels")):
        os.makedirs(os.path.join(train_dir, "labels"))
        
    if not os.path.exists(os.path.join(val_dir, "images")):
        os.makedirs(os.path.join(val_dir, "images"))
    if not os.path.exists(os.path.join(val_dir, "labels")):
        os.makedirs(os.path.join(val_dir, "labels"))
        
    if not os.path.exists(os.path.join(test_dir, "images")):
        os.makedirs(os.path.join(test_dir, "images"))
    if not os.path.exists(os.path.join(test_dir, "labels")):
        os.makedirs(os.path.join(test_dir, "labels"))
        
    for filename in train_filenames:
        shutil.copy(os.path.join(images_dir, filename), os.path.join(train_dir, "images", filename))
        annotation_filename = filename.replace(".jpg", ".txt")
        shutil.copy(os.path.join(annotations_dir, annotation_filename), os.path.join(train_dir, "labels", annotation_filename))
        
    for filename in val_filenames:
        shutil.copy(os.path.join(images_dir, filename), os.path.join(val_dir, "images", filename))
        annotation_filename = filename.replace(".jpg", ".txt")
        shutil.copy(os.path.join(annotations_dir, annotation_filename), os.path.join(val_dir, "labels", annotation_filename))
        
    for filename in test_filenames:
        shutil.copy(os.path.join(images_dir, filename), os.path.join(test_dir, "images", filename))
        annotation_filename = filename.replace(".jpg", ".txt")
        shutil.copy(os.path.join(annotations_dir, annotation_filename), os.path.join(test_dir, "labels", annotation_filename))


if __name__=="__main__":
    images_dir = "../images"
    annotations_dir = "../annotations"
    train_dir = "../dataset/train"
    val_dir = "../dataset/val"
    test_dir = "../dataset/test"
    divide_dataset(images_dir, annotations_dir, train_dir, val_dir, test_dir)
    print("Dataset Has been split successfully")