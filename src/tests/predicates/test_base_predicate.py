from ipynta.predicates import BasePredicate
from pathlib import Path
import PIL
from PIL import Image

SAMPLES_DIR = (Path(__file__).parent.parent / "./imgs")

def test_base_pred_empty_init():
  pred = BasePredicate([])
  actual = len(pred.images)
  expected = 0

  assert(expected == actual)

def test_base_pred_str_list_init():
  pred = BasePredicate([
    f"{SAMPLES_DIR}/1x1.png",
  ])

  assert(isinstance(pred.images[0],  PIL.PngImagePlugin.PngImageFile))

def test_base_pred_pillow_list_init():
  pred = BasePredicate([
    Image.open(f"{SAMPLES_DIR}/1x1.png")
  ])

  assert(isinstance(pred.images[0],  PIL.PngImagePlugin.PngImageFile))
