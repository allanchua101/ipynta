# Author: Allan Chua allanchua.officefiles@gmail.com

class BaseTransform:
  """Base class used to represent a ipynta transformers."""

  def execute(self, img_list=[]) -> list:
    """Runs the transformer against an image list.

    Args:
      img_list: list(Image) - List of images to run the transformer instance against.

    Returns:
      list(Image) - List of transformed images.
    """
    if img_list is None:
      return []
      
    return img_list