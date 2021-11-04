# Author: Allan Chua allanchua.officefiles@gmail.com

class StringValidator:
  """Class used for implementing string-related validation methods."""
  def __init__(self):
    pass

  def is_empty(self, input):
    """Method used for checking if a string is empty or not.
    
    Args:
    ----------
      input : (str)
        string to be checked.

    Returns:
    ----------
      True if the string is empty, False otherwise.
    """
    if input is None:
      return True

    cleansed_str = input.strip()

    return len(cleansed_str) <= 0