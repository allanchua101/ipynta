# Author: Allan Chua allanchua.officefiles@gmail.com

from PIL import Image

class BasePredicate:
  """Base class used to represent a ipynta predicates.

  Attributes
  ----------
  images : list[PIL.Image]
  """
  def __init__(self, images=[]):
    """Constructs all the necessary attributes for a predicate instance.

    Args:
      images (list[PIL.Image]): List of pillow images
    """

    if (len(images) == 0):
      self.images = []
      return

    # If image path list is provided, construct Pillow Image list
    if isinstance(images[0], str):
      tmp = [Image.open(img_path) for img_path in images]
      self.images = tmp
      return

    self.images = images