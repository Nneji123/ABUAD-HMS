import os
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

name = input("Name: \n")
path = input("Path: \n")
filetype = input("Filetype: \n")
    
rename_file(name=name, path=path, filetype=filetype)