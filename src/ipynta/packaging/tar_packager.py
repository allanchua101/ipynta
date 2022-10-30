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
      
      import os
      
      def is_within_directory(directory, target):
          
          abs_directory = os.path.abspath(directory)
          abs_target = os.path.abspath(target)
      
          prefix = os.path.commonprefix([abs_directory, abs_target])
          
          return prefix == abs_directory
      
      def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
      
          for member in tar.getmembers():
              member_path = os.path.join(path, member.name)
              if not is_within_directory(path, member_path):
                  raise Exception("Attempted Path Traversal in Tar File")
      
          tar.extractall(path, members, numeric_owner=numeric_owner) 
          
      
      safe_extract(tf, self.dest_path)
      exts = ['png', 'jpg', 'jpeg']
      output = []

      for ext in exts:
        imgs = glob.glob(self.dest_path + f"/**/*.{ext}")
        output.extend(imgs)

      return output