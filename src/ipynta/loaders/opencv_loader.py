# Author: Allan Chua allanchua.officefiles@gmail.com

import cv2

class OpenCVLoader:
    """A class used for loading OpenCV images"""

    def load(self, img_paths=[]):
      """Method used for loading images from a list of paths in OpenCV format.

      Args:
        img_paths (list): List of image paths to load.
      """
      return [cv2.imread(img_path) for img_path in img_paths]