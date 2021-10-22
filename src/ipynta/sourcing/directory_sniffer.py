# Author: Allan Chua allanchua.officefiles@gmail.com

import glob 

class DirectorySniffer:
    """Class used for sourcing image paths from a local directory."""
        
    def get_img_paths(self, dir_path):
        """Method used for sourcing image paths from a local directory.
        
        Args:
            dir_path : str
                Local directory path to source images from.
        Returns
        -------
            list[str]: List of image paths found from the target directory.
        """
        jpeg_list = [f for f in glob.glob(f'{dir_path}/*.jpeg')]
        jpgs_list = [f for f in glob.glob(f'{dir_path}/*.jpg')]
        pngs_list = [f for f in glob.glob(f'{dir_path}/*.png')]
        
        return jpeg_list + jpgs_list + pngs_list