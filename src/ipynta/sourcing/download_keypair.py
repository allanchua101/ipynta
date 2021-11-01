# Author: Allan Chua allanchua.officefiles@gmail.com

def is_not_blank(s):
  return bool(s and not s.isspace())

class DownloadKeyPair:
  """Class used for representing a download URI and a local persistence path.
  
  Attributes:
  ----------------
  download_url: str
    The download URI.

  local_path: str
    The local persistence path.
  """

  def __init__(self, download_url, local_path):
    """Initializes a DownloadKeyPair object.

    Parameters:
    ----------------
    download_url: str
      The download URI.

    local_path: str
      The local persistence path.
    """
    self.download_url = download_url
    self.local_path = local_path

  def is_valid(self) -> bool:
    """Checks if the download URI and local persistence path are valid.

    Returns:
    ----------------
    bool
      True if the download URI and local persistence path are valid.
    """
    if (self.download_url is None or self.local_path is None):
      return False

    download_url = self.download_url.strip()
    local_path = self.local_path.strip()

    return is_not_blank(download_url) and is_not_blank(local_path)