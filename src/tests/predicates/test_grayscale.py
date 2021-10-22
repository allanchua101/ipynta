from ipynta.loaders import PillowLoader
from ipynta.predicates import GrayscalePred
from os import path
import pytest

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

@pytest.mark.parametrize("src_path, expected_match_count", [
  (f"{SAMPLES_DIR}/1x1.png", 1),
  (f"{SAMPLES_DIR}/1x1.jpg", 1),
  (f"{SAMPLES_DIR}/1x1_red.jpg", 0),
  (f"{SAMPLES_DIR}/1x1_red.png", 0),
])
def test_grayscale_inferencing(src_path, expected_match_count):
  """Test the grayscale predicate."""
  loader = PillowLoader()
  img_list = loader.load([src_path])

  pred = GrayscalePred(img_list)
  grayscale_img_list = pred.filter(is_grayscale=True)
  match_count = len(grayscale_img_list)

  assert(match_count == expected_match_count)