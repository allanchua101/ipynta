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
        exts = ['jpeg', 'jpg', 'png']
        img_list = []
        
        for ext in exts:
            img_list.extend(glob.iglob(f'{dir_path}/**/*.{ext}', recursive=True))

        return img_list