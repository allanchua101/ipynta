# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BasePred

class DimensionPred(BasePred):
  """Class used for writing dimension-based predicates.

  Attributes
  ----------
    min_height (int): Minimum height of the images
    min_width (int): Minimum width of the images
    max_height (int): Maximum height of the images
    max_width (int): Maximum width of the images
  """
  def __init__(self, min_height=-1, min_width=-1, max_height=-1, max_width=-1):
    """Constructor used for setting the constraints of the image predicate.

    Args:
      min_height (int): Minimum height of the images
      min_width (int): Minimum width of the images
      max_height (int): Maximum height of the images
      max_width (int): Maximum width of the images
    """
    BasePred.__init__(self)
    self.min_height = min_height
    self.min_width = min_width
    self.max_height = max_height
    self.max_width = max_width


  def execute(self, images=[]):
    """Runs the dimension predicate agains the provided list of images.

    Args:
      images (list[PIL.Image]): List of images to be evaluated against the predicate.

    Returns:
      list[PIL.Image]: List of images that satisfied the predicate.
    """
    output = []

    for image in images:
      width, height = image.size

      if self.min_height > -1 and height < self.min_height:
        continue

      if self.min_width > -1 and width < self.min_width:
        continue

      if self.max_height > -1 and height > self.max_height:
        continue

      if self.max_width > -1 and width > self.max_width:
        continue

      output.append(image)

    return output