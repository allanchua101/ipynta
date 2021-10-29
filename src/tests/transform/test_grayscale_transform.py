from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import GrayscaleTransform
from os import path
from PIL import Image
import pytest

SAMPLES_DIR = path.dirname(path.abspath(__file__)) + "/sample_images/grayscale"

@pytest.fixture
def sample_images():
  img_list = DirectorySniffer().get_img_paths(SAMPLES_DIR)

  return PillowLoader().load(img_list)

def _check_if_grayscale(img):
  """Method used for checking if an image is grayscale or colored.

  Args:
    images (PIL.Image): Image to check.

  Returns:
    boolean: True if the image is grayscale, False otherwise.
  """
  tmp = img.convert('RGB')
  w, h = img.size

  for i in range(w):
      for j in range(h):
          r, g, b = tmp.getpixel((i,j))
          if r != g != b: 
              return False
              
  return True

def test_grayscale_transform_init():
  try:
    GrayscaleTransform()
  except Exception:
    pytest.fail("GrayscaleTransform constructor failed")

@pytest.mark.parametrize("test_input", [
  (None),
  ([]),
])
def test_grayscale_transform_vs_empty_list(test_input):
  grayscale_img_list = GrayscaleTransform().execute(test_input)
  output_count = len(grayscale_img_list)

  assert(output_count == 0)
  assert(isinstance(grayscale_img_list, list))

def test_grayscale_output_count(sample_images):
  grayscale_img_list = GrayscaleTransform().execute(sample_images)
  output_count = len(grayscale_img_list)

  assert(output_count == len(sample_images))

def test_grayscale_output_type(sample_images):
  grayscale_img_list = GrayscaleTransform().execute(sample_images)

  assert(isinstance(grayscale_img_list, list))

def test_grayscale_output_colors(sample_images):
  grayscale_img_list = GrayscaleTransform().execute(sample_images)
  grayscale_flags = [_check_if_grayscale(img) for img in grayscale_img_list]

  assert(all(grayscale_flags))
