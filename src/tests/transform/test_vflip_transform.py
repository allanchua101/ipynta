from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import VFlipTransform
from os import path
from PIL import Image
import pytest

SAMPLES_DIR = path.dirname(path.abspath(__file__)) + "/sample_images/flip"

def test_vflip_transform_init():
  try:
    VFlipTransform()
  except Exception:
    pytest.fail("VFlipTransform constructor failed")

@pytest.mark.parametrize("test_input", [
  (None),
  ([]),
])
def test_vflip_transform_execute_empty_sets(test_input):
  transformer = VFlipTransform()
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
def test_vflip_transform_dimension_integrity(src_path):
  img = Image.open(src_path)
  output = VFlipTransform().execute([img])
  flipped_img = output[0]

  assert(flipped_img.width == img.width and flipped_img.height == img.height)

def were_pixels_vflipped(img1, img2):
  w = img1.size[0]
  h = img1.size[1]

  for y in range(0, h):
    for x in range(0, w):
      is_same_pixel = img1.getpixel((x, y)) == img2.getpixel((x, h - y - 1))
      
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
  (f"{SAMPLES_DIR}/shapes.jpg"),
])
def test_vflip_transform_pixel_movement(src_path):
  img = Image.open(src_path)
  output = VFlipTransform().execute([img])
  flipped_img = output[0]
  result = were_pixels_vflipped(img, flipped_img)

  assert(result == True)

def test_vflip_transform_batch_transform():
  img_paths = DirectorySniffer().get_img_paths(SAMPLES_DIR)
  img_list = PillowLoader().load(img_paths)
  flipped_img_list = VFlipTransform().execute(img_list)

  for idx, flipped_img in enumerate(flipped_img_list):
    is_flipped = were_pixels_vflipped(img_list[idx], flipped_img)

    if not is_flipped:
      pytest.fail("An image failed to flip vertically")