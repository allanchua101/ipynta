# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BasePred

class DimensionPred(BasePred):
  """Class used for writing dimension-based predicates.

  Attributes
  ----------
  images : list[PIL.Image]
  """
  def __init__(self, images=[]):
    """Constructs all the necessary attributes for a predicate instance.

    Args:
      images (list[PIL.Image]): List of pillow images
    """
    BasePred.__init__(self, images)

  def filter(self, min_height=0, min_width=0, max_height=0, max_width=0):
    """Filters the images based on their dimensions.

    Args:
      min_height (int): Minimum height of the images
      min_width (int): Minimum width of the images
      max_height (int): Maximum height of the images
      max_width (int): Maximum width of the images

    Returns:
      list[PIL.Image]: List of pillow images
    """
    filtered_images = []

    return filtered_images