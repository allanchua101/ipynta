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

  def filter(self, min_height=-1, min_width=-1, max_height=-1, max_width=-1):
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

    for image in self.images:
      width, height = image.size

      if min_height > -1 and height < min_height:
        continue

      if min_width > -1 and width < min_width:
        continue

      if max_height > -1 and height > max_height:
        continue

      if max_width > -1 and width > max_width:
        continue

      filtered_images.append(image)

    return filtered_images