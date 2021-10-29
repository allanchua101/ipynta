from .base import BaseTransform
from PIL import Image
import numpy as np

class VFlipTransform(BaseTransform):
  """Class used for creating a vertical flipped copies of images."""
  
  def __init__(self):
    """Constructs an instance of VFlipTransform."""
    BaseTransform.__init__(self)

  def execute(self, img_list):
    """Method used for creating vertically flipped copies of images
    
    Args:
      img_list list[PIL.Image]: A list of Pillow images to be used as seed image set.
    
    Returns:
      list[PIL.Image]: List of transformed images.
    """
    if (img_list is None):
      return []

    output = []
    
    for img in img_list:
      tmp = img.copy()
      tmp = np.array(tmp)
      tmp = np.flipud(tmp)
      output.append(Image.fromarray(tmp))

    return output