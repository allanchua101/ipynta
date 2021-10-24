from zipfile import ZipFile

# Author: Allan Chua allanchua.officefiles@gmail.com

class ZipExtractor:
  """Class used for extracting zip file contents
  
  Attributes:
    zip_path (str): path of the zip file.
    dest_path (str): path of the destination folder.
  """
  def __init__(self, zip_path, dest_path):
    self.zip_path = zip_path
    self.dest_path = dest_path

  def execute(self):
    """Executes the extraction of zip file contents
    
    Returns:
      list[str]: List of extracted file paths.
    """
    output = []

    with ZipFile(self.zip_path) as zf:
      zf.extractall(self.dest_path)
      output = zf.namelist()

    return output