# Author: Allan Chua allanchua.officefiles@gmail.com

class BaseTransform:
  """Base class used to represent a ipynta transformers."""

  def execute(self, images=[]) -> list:
    """Runs the transformer against an image list.

    Args:
      images: list(Image) - List of images to run the transformer instance against.

    Returns:
      list(Image) - List of transformed images.
    """
    if images is None:
      return []
      
    return images