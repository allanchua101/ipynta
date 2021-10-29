from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import HFlipTransform
from os import path
from PIL import Image
import pytest

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

def test_hflip_transform_init():
  try:
    HFlipTransform()
  except Exception:
    pytest.fail("HFlipTransform constructor failed")

@pytest.mark.parametrize("test_input", [
  (None),
  ([]),
])
def test_hflip_transform_execute_empty_sets(test_input):
  transformer = HFlipTransform()
  output = transformer.execute(test_input)

  assert(isinstance(output, list) == True)

## This test case validates if the dimensions
## of the image wasn't tampered during the flip
@pytest.mark.parametrize("src_path", [
  (f"{SAMPLES_DIR}/1x1_red.jpg"),
  (f"{SAMPLES_DIR}/1x1_red.png"),
  (f"{SAMPLES_DIR}/1x1.jpg"),
  (f"{SAMPLES_DIR}/1x1.png"),
  (f"{SAMPLES_DIR}/5x5.jpg"),
  (f"{SAMPLES_DIR}/5x5.png"),
])
def test_hflip_transform_dimension_integrity(src_path):
  img = Image.open(src_path)
  output = HFlipTransform().execute([img])
  flipped_img = output[0]

  assert(flipped_img.width == img.width and flipped_img.height == img.height)

def check_if_pixels_are_flipped(img1, img2):
  w = img1.size[0]
  h = img1.size[1]

  for y in range(0, h):
    for x in range(0, w):
      is_same_pixel = img1.getpixel((x, y)) == img2.getpixel((w - x - 1, y))
      
      if is_same_pixel == False:
        return False

  return True

## This test case validates if the pixels
## are flipped correctly in the horizontal direction
@pytest.mark.parametrize("src_path", [
  (f"{SAMPLES_DIR}/1x1_red.jpg"),
  (f"{SAMPLES_DIR}/1x1_red.png"),
  (f"{SAMPLES_DIR}/1x1.jpg"),
  (f"{SAMPLES_DIR}/1x1.png"),
  (f"{SAMPLES_DIR}/5x5.jpg"),
  (f"{SAMPLES_DIR}/5x5.png"),
])
def test_hflip_transform_pixel_movement(src_path):
  img = Image.open(src_path)
  output = HFlipTransform().execute([img])
  flipped_img = output[0]
  result = check_if_pixels_are_flipped(img, flipped_img)

  assert(result == True)