# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BaseTransform

class GrayscaleTransform(BaseTransform):
  """Class used for creating a grayscale version of images."""

  def __init__(self):
    """Constructs an instance of GrayscaleTransform."""
    BaseTransform.__init__(self)

  def execute(self, img_list):
    """Method used for creating grayscale version of the provided images.
    
    Args:
      img_list list[PIL.Image]: A list of Pillow images to be used as seed image set.

    Returns:
      list[PIL.Image]: List of grayscaled images.
    """
    if (img_list is None):
      return []
    
    return [img.copy().convert("LA") for img in img_list]