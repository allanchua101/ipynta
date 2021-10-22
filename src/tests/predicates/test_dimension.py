from ipynta.predicates import DimensionPred
from os import path
from PIL import Image
import PIL
import pytest

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

def test_dimpred_empty_init():
  """Test function for empty filter construction"""
  pred = DimensionPred([])
  actual = len(pred.images)
  expected = 0

  assert(expected == actual)

def test_dimpred_pillow_list_init():
  """Test function for checking type of image"""
  pred = DimensionPred([
    Image.open(f"{SAMPLES_DIR}/1x1.png")
  ])

  assert(isinstance(pred.images[0],  PIL.PngImagePlugin.PngImageFile))

# Test by minimum height only
@pytest.mark.parametrize("h, expected", [
  (1, 4),
  (5, 2),
  (6, 0)
])
def test_dimpred_filter_by_min_height(h, expected):
  """Test function for filtering by minimum height"""
  pred = DimensionPred([
    Image.open(f"{SAMPLES_DIR}/1x1.png"),
    Image.open(f"{SAMPLES_DIR}/1x1.jpg"),
    Image.open(f"{SAMPLES_DIR}/5x5.png"),
    Image.open(f"{SAMPLES_DIR}/5x5.jpg"),
  ])

  img_list = pred.filter(min_height=h)
  actual = len(img_list)

  assert(actual == expected)

# Test by minimum width only
@pytest.mark.parametrize("w, expected", [
  (1, 4),
  (5, 2),
  (6, 0)
])
def test_dimpred_filter_by_min_width(w, expected):
  """Test function for filtering by minimum width"""
  pred = DimensionPred([
    Image.open(f"{SAMPLES_DIR}/1x1.png"),
    Image.open(f"{SAMPLES_DIR}/1x1.jpg"),
    Image.open(f"{SAMPLES_DIR}/5x5.png"),
    Image.open(f"{SAMPLES_DIR}/5x5.jpg"),
  ])

  img_list = pred.filter(min_height=-1, min_width=w)
  actual = len(img_list)

  assert(actual == expected)

# Test by minimum height and width
@pytest.mark.parametrize("h, w, expected", [
  (1, 1, 4),
  (5, 5, 2),
  (6, 6, 0)
])
def test_dimpred_filter_by_min_dims(h, w, expected):
  """Test function for filtering by minimum width and height"""
  pred = DimensionPred([
    Image.open(f"{SAMPLES_DIR}/1x1.png"),
    Image.open(f"{SAMPLES_DIR}/1x1.jpg"),
    Image.open(f"{SAMPLES_DIR}/5x5.png"),
    Image.open(f"{SAMPLES_DIR}/5x5.jpg"),
  ])

  img_list = pred.filter(min_height=h, min_width=w)
  actual = len(img_list)

  assert(actual == expected)