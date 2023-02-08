import os

def delete_unannotated_images(images_dir, annotations_dir):
    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg"):
            annotation_filename = filename[:-4] + ".txt"
            annotation_path = os.path.join(annotations_dir, annotation_filename)
            if not os.path.exists(annotation_path):
                image_path = os.path.join(images_dir, filename)
                os.remove(image_path)
                
                
images_dir = "./images"
annotations_dir = "./annotations"
delete_unannotated_images(images_dir, annotations_dir)
print("Deleted all unannotated images")

