# Author: Allan Chua allanchua.officefiles@gmail.com

import os
from .download_keypair import DownloadKeyPair
import urllib.request as rq

class HttpDownloader:
  """Class used for downloading files over HTTP.

  Attributes:
  ----------------
  download_list: list[DownloadKeyPair]
    A list of DownloadKeyPair objects.
  """
  def __init__(self, download_list: DownloadKeyPair):
    self.download_list = download_list

  def execute(self):
    """Method used to trigger the download of registered files."""
    if (self.download_list is None):
      return

    for item in self.download_list:
      if (not item.is_valid()):
        continue

      dir_name = os.path.dirname(item.local_path)

      if not os.path.exists(dir_name):
        os.makedirs(dir_name)

      rq.urlretrieve(item.download_url, item.local_path)
