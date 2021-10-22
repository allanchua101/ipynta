from ipynta.predicates import BasePred
from os import path
from PIL import Image
import PIL

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

def test_base_pred_empty_init():
  pred = BasePred([])
  actual = len(pred.images)
  expected = 0

  assert(expected == actual)

def test_base_pred_pillow_list_init():
  pred = BasePred([
    Image.open(f"{SAMPLES_DIR}/1x1.png")
  ])

  assert(isinstance(pred.images[0],  PIL.PngImagePlugin.PngImageFile))
