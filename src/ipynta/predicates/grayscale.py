# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BasePred

class GrayscalePred(BasePred):
  """Class used for writing predicates related to grayscaling.

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

  def filter(self, is_grayscale=True):
    """Filters the images based on whether they are grayscale or not.

    Args:
      is_grayscale (bool): Whether the images are grayscale or not.

    Returns:
      list[PIL.Image]: List of images with grayscale configuration similar to the flag provided.
    """
    output = []

    for img in self.images:
      if self._is_grey_scale(img) == is_grayscale:
        output.append(img)

    return output

  def _is_grey_scale(self, img):
    """Method used for checking if an image instance is grayscale or not.
    
    """
    tmp = img.convert('RGB')
    w, h = img.size

    for i in range(w):
        for j in range(h):
            r, g, b = tmp.getpixel((i,j))
            if r != g != b: 
                return False
                
    return True