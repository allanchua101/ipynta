from ipynta.packaging import ZipPackager
from os import path
import pytest
import shutil

DIR_PATH = path.abspath(path.dirname(__file__))
SAMPLE_ZIP = DIR_PATH + "/sample_packages/6-images.zip"
DST_FOLDER = DIR_PATH + "/dst_folder/6-images-zip"

@pytest.fixture(scope="session", autouse=True)
def clear_dst_folder():
  yield
  
  if path.exists(DST_FOLDER):
    shutil.rmtree(DST_FOLDER)

@pytest.fixture()
def packager():
  packager = ZipPackager(SAMPLE_ZIP, DST_FOLDER)
  return packager

def test_zip_packager_init():
  try:
    ZipPackager(SAMPLE_ZIP, DST_FOLDER)
  except Exception:
    pytest.fail("ZipPackager construction failed")

def test_zip_packager_unzip_count(packager):
  files = packager.unpack()

  assert(len(files) == 6)

def test_zip_packager_file_existence(packager):
  files = packager.unpack()

  assert(all([path.exists(f"{DST_FOLDER}/{file}") for file in files]))

