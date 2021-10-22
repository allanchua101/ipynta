# Author: Allan Chua allanchua.officefiles@gmail.com

from PIL import Image

class PillowLoader:
    """A class used for loading Pillow images"""

    def load(self, img_paths=[]):
      """Method used for loading images from a list of paths in Pillow format.

      Args:
        img_paths (list): List of image paths to load.
      """
      return [Image.open(img_path) for img_path in img_paths]