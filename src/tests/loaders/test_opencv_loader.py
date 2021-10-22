from ipynta.loaders import OpenCVLoader
from ipynta.globbers import ImageGlobber
from os import path
import numpy as np

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

def test_load_empty_list():
  """Test function for empty list loading of OpenCV images"""
  loader = OpenCVLoader()
  actual = loader.load([])

  assert(len(actual) == 0)

def test_load_single_image():
  """Test function for single image loading of OpenCV images"""
  loader = OpenCVLoader()
  actual = loader.load([SAMPLES_DIR + "/1x1.png"])

  assert(len(actual) == 1)
  assert(isinstance(actual[0], np.ndarray))

def test_load_multiple():
  """Test function for single image loading of OpenCV images"""
  loader = OpenCVLoader()

  globber = ImageGlobber(SAMPLES_DIR)
  path_list = globber.get_img_paths()

  img_list = loader.load(path_list)
  actual = len(img_list)
  expected = len(img_list)

  assert(actual == expected)
  assert(isinstance(img_list[0], np.ndarray))
