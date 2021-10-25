from ipynta.extractors import TarExtractor
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
def extractor():
  extractor = TarExtractor(SAMPLE_TAR, DST_FOLDER)
  return extractor

def test_tar_extractor_init():
  try:
    TarExtractor(SAMPLE_TAR, DST_FOLDER)
  except Exception:
    pytest.fail("TarExtractor construction failed")

def test_tar_extractor_untar_count(extractor):
  files = extractor.execute()
  
  assert(len(files) == 6)

def test_tar_extractor_file_existence(extractor):
  files = extractor.execute()

  assert(all([path.exists(f"{file}") for file in files]))

