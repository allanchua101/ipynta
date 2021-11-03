import tarfile
import glob

# Author: Allan Chua allanchua.officefiles@gmail.com

class TarPackager:
  """Class used for extracting TAR file contents
  
  Attributes:
    tar_path (str): path of the TAR file.
    dest_path (str): path of the destination folder.
  """
  def __init__(self, tar_path, dest_path):
    self.tar_path = tar_path
    self.dest_path = dest_path

  def unpack(self):
    """Method used for unpacking of TAR file contents
    
    Returns:
      list[str]: List of unpacked file paths.
    """
    with tarfile.open(self.tar_path) as tf:
      tf.extractall(self.dest_path)
      exts = ['png', 'jpg', 'jpeg']
      output = []

      for ext in exts:
        imgs = glob.glob(self.dest_path + f"/**/*.{ext}")
        output.extend(imgs)

      return output