from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import GrayscalePred
from os import path
import pytest

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

@pytest.fixture
def sample_images():
  img_list = DirectorySniffer().get_img_paths(SAMPLES_DIR)

  return PillowLoader().load(img_list)

@pytest.mark.parametrize("is_grayscale", [
  (True),
  (False)
])
def test_grayscale_pred_init(is_grayscale):
  try:
    GrayscalePred(is_grayscale)
  except Exception:
    pytest.fail("GrayscalePred constructor failed")

@pytest.mark.parametrize("is_grayscale, expected_count", [
  (True, 4),
  (False, 2)
])
def test_grayscale_pred(is_grayscale, expected_count, sample_images):
  pred = GrayscalePred(is_grayscale)
  actual_count = len(pred.execute(sample_images))

  assert(actual_count == expected_count)

@pytest.mark.parametrize("src_path, expected_count", [
  (f"{SAMPLES_DIR}/1x1.png", 1),
  (f"{SAMPLES_DIR}/1x1.jpg", 1),
  (f"{SAMPLES_DIR}/1x1_red.jpg", 0),
  (f"{SAMPLES_DIR}/1x1_red.png", 0),
])
def test_grayscale_inferencing(src_path, expected_count):
  loader = PillowLoader()
  img_list = loader.load([src_path])

  pred = GrayscalePred(is_grayscale=True)
  matched_img_list = pred.execute(img_list)
  match_count = len(matched_img_list)

  assert(match_count == expected_count)