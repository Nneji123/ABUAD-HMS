'''
This script is used to delete all images that do not have corresponding annotations.
'''

import os

def delete_unannotated_images(images_dir: str, annotations_dir: str):
    """
    The delete_unannotated_images function deletes all images in the images_dir that do not have corresponding annotations
    in the annotations_dir. This is useful for cleaning up after a dataset has been annotated, since it removes all of the 
    images that were never annotated.
    
    Args:
        images_dir: Specify the directory where the images are stored
        annotations_dir: Specify the directory where the annotations are stored
    
    Returns:
        None
    """
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg"):
            annotation_filename = filename[:-4] + ".txt"
            annotation_path = os.path.join(annotations_dir, annotation_filename)
            if not os.path.exists(annotation_path):
                image_path = os.path.join(images_dir, filename)
                os.remove(image_path)
                


if __name__=="__main__":            
    images_dir = "./images"
    annotations_dir = "./annotations"
    delete_unannotated_images(images_dir, annotations_dir)
    print("Deleted all unannotated images")

