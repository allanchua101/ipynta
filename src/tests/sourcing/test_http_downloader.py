from ipynta.sourcing import DownloadKeyPair
from ipynta.sourcing import HttpDownloader
from unittest.mock import Mock
from os import path
import pytest
import shutil
import urllib.request as rq

DIR_PATH = path.dirname(path.dirname(path.abspath(__file__))) 
SAMPLES_DIR = f"{DIR_PATH}/imgs"
DEST_PATH = f"{DIR_PATH}/sourcing/http_testing/test_dls"
MOCK_FQDN = "http://localhost:8585"

# Stubbing method for file download simulation
def _mock_download(src, dst):
  local_src = src.replace(MOCK_FQDN, SAMPLES_DIR)

  with open(local_src, "rb") as f:
    with open(dst, "wb") as g:
      g.write(f.read())

# Test class constructor
@pytest.mark.parametrize("download_list", [
  (None),
  ([]),
  (DownloadKeyPair(f"{MOCK_FQDN}/1x1.jpg", f"{DEST_PATH}/1x1.jpg")),
])
def test_http_downloader_init(download_list):
  try:
    HttpDownloader(download_list)
  except Exception:
    pytest.fail("HttpDownloader construction failed")

# Simulate good download operations
@pytest.mark.parametrize("url, dst_path", [
  (f"{MOCK_FQDN}/1x1.jpg", f"{DEST_PATH}/1x1.jpg"),
  (f"{MOCK_FQDN}/1x1.png", f"{DEST_PATH}/1x1.png"),
  (f"{MOCK_FQDN}/5x5.png", f"{DEST_PATH}/5x5.png"),
])
def test_http_downloader_good_dls(url, dst_path):
  download_list = []
  download_list.append(DownloadKeyPair(url, dst_path))

  rq.urlretrieve = Mock()
  rq.urlretrieve.side_effect = lambda src, dst : _mock_download(src, dst)

  downloader = HttpDownloader(download_list)
  downloader.execute()

  assert path.isfile(dst_path)

# Simulate bad download operations
@pytest.mark.parametrize("url, dst_path", [
  (f"{MOCK_FQDN}/gg1.jpg", f"{DEST_PATH}/gg1.jpg"),
  (f"{MOCK_FQDN}/gg2.png", f"{DEST_PATH}/gg2.png"),
  (f"{MOCK_FQDN}/gg3.png", f"{DEST_PATH}/gg3.png"),
])
def test_http_downloader_bad_dls(url, dst_path):
  download_list = []
  download_list.append(DownloadKeyPair(url, dst_path))

  rq.urlretrieve = Mock(side_efffect = rq.HTTPError(url, 404, "Not Found", None, None))

  try:
    downloader = HttpDownloader(download_list)
    downloader.execute()
  except rq.HTTPError:
    pytest.success("HttpDownloader handles HTTP error well")

# Fixture for cleaning up side effects of test
@pytest.fixture(scope="session", autouse=True)
def clear_http_downloader_dst_folder():
  yield
  
  if path.exists(DEST_PATH):
    shutil.rmtree(DEST_PATH)