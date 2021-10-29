# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BaseTransform
from PIL import Image
import numpy as np

class HFlipTransform(BaseTransform):
  """Class used for creating a horizonstally flipped version of images."""
  
  def __init__(self):
    """Constructs an instance of HFlipTransform."""
    BaseTransform.__init__(self)

  def execute(self, images):
    """Method used for creating horizontally flipped versions of provided images.

    Args:
      images list[PIL.Image]: A list of Pillow images to be used as seed image set.

    Returns:
      list[PIL.Image]: List of transformed images.
    """
    if (images is None):
      return []

    output = []

    for image in images:
      tmp = image.copy()
      tmp = np.array(tmp)
      tmp = np.fliplr(tmp)
      output.append(Image.fromarray(tmp))

    return output