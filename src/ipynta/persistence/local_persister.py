# Author: Allan Chua allanchua.officefiles@gmail.com

from ipynta.enums import NamingStrategy
from ipynta.validators import StringValidator
import os
import uuid

class LocalPersister:
  """Class used for saving files to the local file system
  
  Attributes:
  -----------
  img_list (list) : list of images to be saved to the local file system.
  dir (string) : directory to save images to.
  naming_strategy (NamingStrategy) : strategy to use for naming the images.
  output_file_type (string) : file type to use for saving images.
  """

  def __init__(self, img_list=[], dir="", naming_strategy=NamingStrategy.UUID4):
    """Method used for constructing a local persister instance.

    Args:
    ----------
    img_list : list  
      Images to be saved to the local file system.

    dir : string
      Directory to save images to.

    naming_strategy : NamingStrategy
      Strategy to use for naming the images.
    """
    self.img_list = img_list
    self.dir = dir
    self.naming_strategy = naming_strategy
    self.output_file_type = ".jpg"

  def set_output_file_type(self, file_type):
    """Method used for setting the output file type.

    Args:
    ----------
    file_type : string
      File type to use for saving images.
    """
    self.output_file_type = file_type

  def _save_file(self, file_name, img):
    if self.output_file_type in [".jpg", ".jpeg"]:
      img.convert('RGB').save(file_name)
      return

    img.convert('RGBA').save(file_name)

  def _run_number_strategy(self):
    id = 0
    for img in self.img_list:
      id += 1
      file_name = f"{self.dir}/{id}{self.output_file_type}"

      self._save_file(file_name, img)

  def _run_guid_strategy(self):
    for img in self.img_list:
      id = uuid.uuid4()
      file_name = f"{self.dir}/{id}{self.output_file_type}"

      self._save_file(file_name, img)
  
  def execute(self):
    """Method used for invoking the saving of images to the local file system."""
    if StringValidator().is_empty(self.dir):
      raise Exception("Please specify an output directory")

    if not os.path.exists(self.dir):
      os.makedirs(self.dir)

    if len(self.img_list) == 0:
      return

    strategy_map = {
      NamingStrategy.UUID4: self._run_guid_strategy,
      NamingStrategy.NUMERICAL: self._run_number_strategy
    }

    if self.naming_strategy in strategy_map:
      strategy_map[self.naming_strategy]()