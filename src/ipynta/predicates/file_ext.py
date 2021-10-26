# Author: Allan Chua allanchua.officefiles@gmail.com

from .base import BasePred

class FileExtPred(BasePred):
  """Class used for writing predicates related to file extensions.

  Attributes
  ----------
  file_ext (string): Parameter that defines the extension to be checked against the images.
  """
  def __init__(self, file_ext=".jpg"):
    """Constructs an instance of FileExtPred.

    Args:
      file_ext (string): Parameter that defines the extension to be checked against the images.
    """
    BasePred.__init__(self)
    self.file_ext = file_ext

  def execute(self, images=[]):
    """Filters the provided images based on whether they possess the file extension defined in the constructor.

    Args:
      images (list[PIL.Image]): List of images to be evaluated against the predicate.

    Returns:
      list[PIL.Image]: List of images that satisfied the predicate.
    """
    output = []

    for img in images:
      if img.filename.endswith(self.file_ext):
        output.append(img)

    return output