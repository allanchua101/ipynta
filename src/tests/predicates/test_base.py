from ipynta.predicates import BasePred
from os import path
import pytest

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"


def test_base_pred_constructor():
  try:
    BasePred()
  except Exception:
    pytest.fail("BasePred constructor failed")

def test_base_pred_execute_empty():
  pred = BasePred()
  input = []
  output = pred.execute(input)

  assert(len(output) == 0)