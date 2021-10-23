# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BasePred

class GrayscalePred(BasePred):
  """Class used for writing predicates related to grayscaling.

  Attributes
  ----------
  is_grayscale (boolean): Flag that indicates whether the predicate searches grayscale images or not.
  """
  def __init__(self, is_grayscale=True):
    """Constructs an instance of GrayscalePred.

    Args:
      is_grayscale (boolean): Flag that indicates whether the predicate searches grayscale images or not.
    """
    BasePred.__init__(self)
    self.is_grayscale = is_grayscale

  def execute(self, images=[]):
    """Filters the provided images based on whether they are grayscale or not.

    Args:
      images (list[PIL.Image]): List of images to be evaluated against the predicate.

    Returns:
      list[PIL.Image]: List of images that satisfied the predicate.
    """
    output = []

    for img in images:
      if self._check_if_grayscale(img) == self.is_grayscale:
        output.append(img)

    return output

  def _check_if_grayscale(self, img):
    """Method used for checking if an image is grayscale or colored.

    Args:
      images (PIL.Image): Image to check.

    Returns:
      boolean: True if the image is grayscale, False otherwise.
    """
    tmp = img.convert('RGB')
    w, h = img.size

    for i in range(w):
        for j in range(h):
            r, g, b = tmp.getpixel((i,j))
            if r != g != b: 
                return False
                
    return True