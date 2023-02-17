'''
This script is used to resize the images and rename them.
'''



from PIL import Image
import os
import glob


def resize(root_dir: str, filetype:str, width:int, height:int):
    """
    The resize function takes a directory of images and resizes them to the specified width and height.
    It then overwrites the original image with the new resized image.
    
    Args:
        root_dir: str: Specify the directory where all of the files are located
        filetype:str: Specify the filetype of the images that are going to be resized
        width:int: Define the width of the resized image
        height:int: Set the height of the resized image in pixels
    
    Returns:
        The resized image
    """
    for filename in glob.iglob(root_dir + f'**/*.{filetype}', recursive=True):
        print(filename)
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        imResize = rgb_im.resize((width,height), Image.ANTIALIAS)
        imResize.save(filename , 'JPEG', quality=90)
        
    print("All files resized!")
    

# Function to rename multiple files
def rename_file(name:str, path: str, filetype: str):
    '''
    The rename_file function takes a directory of images and renames them.
    It takes in a name, path, and filetype as inputs.
    
    Args:
        name: str: Specify the name of the image
        path: str: Specify the path to the directory where the images are located
        filetype: str: Specify the filetype of the images
        
    Returns:
        The renamed images
    '''
    i = 0
    for filename in os.listdir(path):
        my_dest = name + str(i) + f".{filetype}"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    print("All files renamed!")


if __name__ == '__main__':
    rename_file(name="smoking", path="../images/", filetype="jpg")
    resize(root_dir="../images/", filetype='jpg', width=224, height=224)
    