# Author: Allan Chua allanchua.officefiles@gmail.com

from PIL import Image

class BasePred:
  """Base class used to represent a ipynta predicates.

  Attributes
  ----------
  images : list[PIL.Image]
    List of pillow images
  """
  def __init__(self, images=[]):
    """Constructs all the necessary attributes for a predicate instance.

    Args:
      images (list[PIL.Image]): List of pillow images
    """
    self.images = images