from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred
from os import path
import pytest

@pytest.fixture
def sample_images():
  sample_dir = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"
  img_list = DirectorySniffer().get_img_paths(sample_dir)

  return PillowLoader().load(img_list)

def test_dimension_pred_init():
  try:
    DimensionPred()
  except Exception:
    pytest.fail("DimensionPred constructor failed")

# Test by minimum height only
@pytest.mark.parametrize("mh, expected", [
  (1, 6),
  (5, 2),
  (6, 0)
])
def test_dimpred_filter_by_min_height(mh, expected, sample_images):
  pred = DimensionPred(min_height=mh)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)

# Test by minimum width only
@pytest.mark.parametrize("mw, expected", [
  (1, 6),
  (5, 2),
  (6, 0)
])
def test_dimpred_filter_by_min_width(mw, expected, sample_images):
  pred = DimensionPred(min_width=mw)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)

# Test by minimum height and width
@pytest.mark.parametrize("mh, mw, expected", [
  (1, 1, 6),
  (5, 5, 2),
  (6, 6, 0)
])
def test_dimpred_filter_by_min_dims(mh, mw, expected, sample_images):
  pred = DimensionPred(min_height=mh, min_width=mw)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)

# Test by max height only
@pytest.mark.parametrize("max_h, expected", [
  (0, 0),
  (1, 4),
  (5, 6),
])
def test_dimpred_filter_by_max_height(max_h, expected, sample_images):
  pred = DimensionPred(max_height=max_h)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)

# Test by max width only
@pytest.mark.parametrize("max_w, expected", [
  (0, 0),
  (1, 4),
  (5, 6),
])
def test_dimpred_filter_by_max_width(max_w, expected, sample_images):
  pred = DimensionPred(max_width=max_w)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)

# Test by max height and width
@pytest.mark.parametrize("max_h, max_w, expected", [
  (0, 0, 0),
  (1, 0, 0),
  (1, 1, 4),
  (1, 2, 4),
  (2, 1, 4),
  (5, 5, 6),
  (6, 6, 6)
])
def test_dimpred_filter_by_min_dims(max_h, max_w, expected, sample_images):
  pred = DimensionPred(max_height=max_h, max_width=max_w)

  img_list = pred.execute(sample_images)
  actual = len(img_list)

  assert(actual == expected)
