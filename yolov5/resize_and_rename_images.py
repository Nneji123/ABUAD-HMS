# For resizing and converting images
from PIL import Image
import os
import glob


def resize(root_dir: str, filetype:str, width:int, height:int):
    for filename in glob.iglob(root_dir + f'**/*.{filetype}', recursive=True):
        print(filename)
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        imResize = rgb_im.resize((width,height), Image.ANTIALIAS)
        imResize.save(filename , 'JPEG', quality=90)
        
    print("All files resized!")
    

# Function to rename multiple files
def rename_file(name:str, path: str, filetype: str):
    i = 0
    # path="./images/"
    for filename in os.listdir(path):
        my_dest = name + str(i) + f".{filetype}"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    print("All files renamed!")

if __name__ == '__main__':
    rename_file(name="smoking", path="./images", filetype=".jpg")
    resize(root_dir="./images", filetype='jpg', width=224, height=224)
    