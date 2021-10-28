from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import TrueFileTypePred
from os import path
from PIL import Image
import pytest

SAMPLES_DIR = path.dirname(path.abspath(__file__)) + "/true_file_type_samples"

@pytest.fixture
def tft_sample_images():
  img_list = DirectorySniffer().get_img_paths(SAMPLES_DIR)

  return PillowLoader().load(img_list)

def test_tft_pred_init():
  try:
    TrueFileTypePred(".jpg")
  except Exception:
    pytest.fail("TrueFileTypePred constructor failed")

@pytest.mark.parametrize("accurate_file_type, expected", [
  (False, 3),
  (True, 2),
])
def test_tft_pred_batched_test(accurate_file_type, expected, tft_sample_images):
  pred = TrueFileTypePred(accurate_file_type)
  pass_count = len(pred.execute(tft_sample_images))

  assert(pass_count == expected)

@pytest.mark.parametrize("path, is_accurate, expected_match_count", [
  (f"{SAMPLES_DIR}/1x1_red_wft.jpeg", False, 1),
  (f"{SAMPLES_DIR}/1x1_red_wft.jpeg", True, 0),
  (f"{SAMPLES_DIR}/1x1_red_wft.png", False, 1),
  (f"{SAMPLES_DIR}/1x1_red_wft.png", True, 0),
  (f"{SAMPLES_DIR}/1x1_red_wft2.jpeg", False, 1),
  (f"{SAMPLES_DIR}/1x1_red_wft2.jpeg", True, 0),
  (f"{SAMPLES_DIR}/1x1_tft.jpeg", True, 1),
  (f"{SAMPLES_DIR}/1x1_tft.jpeg", False, 0),
  (f"{SAMPLES_DIR}/1x1_tft.png", True, 1),
  (f"{SAMPLES_DIR}/1x1_tft.png", False, 0),
])
def test_tft_pred_one_at_a_time(path, is_accurate, expected_match_count):
  img_list = [Image.open(path)]
  pred = TrueFileTypePred(is_accurate)
  pass_count = len(pred.execute(img_list))

  assert(pass_count == expected_match_count)