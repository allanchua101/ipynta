from ipynta.extractors import ZipExtractor
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
def extractor():
  extractor = ZipExtractor(SAMPLE_ZIP, DST_FOLDER)
  return extractor

def test_zip_extractor_init():
  try:
    ZipExtractor(SAMPLE_ZIP, DST_FOLDER)
  except Exception:
    pytest.fail("ZipExtractor construction failed")

def test_zip_extractor_unzip_count(extractor):
  files = extractor.execute()

  assert(len(files) == 6)

def test_zip_extractor_file_existence(extractor):
  files = extractor.execute()

  assert(all([path.exists(f"{DST_FOLDER}/{file}") for file in files]))

