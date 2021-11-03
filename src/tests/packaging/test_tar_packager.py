from ipynta.packaging import TarPackager
from os import path
import pytest
import shutil

DIR_PATH = path.abspath(path.dirname(__file__))
SAMPLE_TAR = DIR_PATH + "/sample_packages/6-images.tar.gz"
DST_FOLDER = DIR_PATH + "/dst_folder/6-images-tar"

@pytest.fixture(scope="session", autouse=True)
def clear_dst_folder():
  yield
  
  if path.exists(DST_FOLDER):
    shutil.rmtree(DST_FOLDER)

@pytest.fixture()
def packager():
  packager = TarPackager(SAMPLE_TAR, DST_FOLDER)
  return packager

def test_tar_packager_init():
  try:
    TarPackager(SAMPLE_TAR, DST_FOLDER)
  except Exception:
    pytest.fail("TarPackager construction failed")

def test_tar_packager_untar_count(packager):
  files = packager.unpack()
  
  assert(len(files) == 6)

def test_tar_packager_file_existence(packager):
  files = packager.unpack()

  assert(all([path.exists(f"{file}") for file in files]))

