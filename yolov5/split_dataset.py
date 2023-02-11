import os
import shutil
import numpy as np
from sklearn.model_selection import train_test_split

def divide_dataset(images_dir, annotations_dir, train_dir, val_dir, test_dir, test_size=0.2, val_size=0.2):
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


images_dir = "./images"
annotations_dir = "./annotations"
train_dir = "./dataset/train"
val_dir = "./dataset/val"
test_dir = "./dataset/test"
divide_dataset(images_dir, annotations_dir, train_dir, val_dir, test_dir)
print("Dataset Has been split successfully")