from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import FileExtPred
from os import path
import pytest

@pytest.fixture
def sample_images():
  sample_dir = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"
  img_list = DirectorySniffer().get_img_paths(sample_dir)

  return PillowLoader().load(img_list)

def test_filext_pred_init():
  try:
    FileExtPred(".jpg")
  except Exception:
    pytest.fail("FileExtPred constructor failed")

@pytest.mark.parametrize("file_ext, expected", [
  (".jpg", 3),
  (".png", 3),
  (".exe", 0)
])
def test_filext_pred_match(file_ext, expected, sample_images):
  pred = FileExtPred(file_ext)
  pass_count = len(pred.execute(sample_images))

  assert(pass_count == expected)