# Author: Allan Chua allanchua.officefiles@gmail.com

from PIL import Image

class BasePred:
  """Base class used to represent a ipynta predicates."""

  def execute(self, images=[]) -> list:
    """Runs the predicate against the provided list of images.

    Args:
      images: list(Image) - List of images to run the predicate against.

    Returns:
      list(Image) - List of images that satisfy the predicate.
    """
    return images