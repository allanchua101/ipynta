from ipynta.predicates import BasePredicate
from pathlib import Path
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
    f"{SAMPLES_DIR}/1x1.jpg",
  ])

  assert(type(pred.images[0]) is Image )
