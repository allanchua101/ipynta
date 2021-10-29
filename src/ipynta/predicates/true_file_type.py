# Author: Allan Chua allanchua.officefiles@gmail.com

import imghdr
import os
from .base import BasePred

class TrueFileTypePred(BasePred):
  """Class used for writing predicates used for validating true file types.

  Attributes
  ----------
    seek_accurate_files (boolean): Flag that dictates wether the predicate seeks files with true file type or the ones with mis-represented file extensions.
  """
  def __init__(self, seek_accurate_files=True):
    """Initializes the TrueFileTypePred class.

    Parameters
    ----------
      seek_accurate_files (boolean): Flag that dictates wether the predicate seeks files with true file type or the ones with mis-represented file extensions.
    """
    BasePred.__init__(self)
    self.seek_accurate_files = seek_accurate_files

  def execute(self, images=[]):
    """Runs the predicate against the provided list of images.

    Args:
      images (list[PIL.Image]): List of images to be evaluated against the predicate.

    Returns:
      list[PIL.Image]: List of images that passed the true file type assertion.
    """
    output = []

    for img in images:
      true_file_type = imghdr.what(img.filename)
      declared_file_type = os.path.splitext(img.filename)[1]
      is_accurate_type = f".{true_file_type}" == declared_file_type

      if self.seek_accurate_files == is_accurate_type:
        output.append(img)

    return output