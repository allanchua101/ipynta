# Author: Allan Chua allanchua.officefiles@gmail.com

import glob 

class ImageGlobber:
    """A class used to represent an image globber.
    
    Attributes
    ----------
    src_path : str
        Source path of images to be globbed.
    """
    def __init__(self, src_path):
        """Constructs all the necessary attributes for an image globber object.
        
        Args:
            src_path (str): Source path of images to be globbed.
        """
        self.src_path = src_path
        
    def get_img_paths(self):
        """Method used for loading image paths from source directory.
        
        Returns
        -------
            list[str]: List of image paths found from source directory.
        """
        src_path = self.src_path
        jpeg_list = [f for f in glob.glob(f'{src_path}/*.jpeg')]
        jpgs_list = [f for f in glob.glob(f'{src_path}/*.jpg')]
        pngs_list = [f for f in glob.glob(f'{src_path}/*.png')]
        
        return jpeg_list + jpgs_list + pngs_list