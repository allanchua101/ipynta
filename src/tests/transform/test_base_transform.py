from ipynta.transform import BaseTransform
import pytest

def test_base_transform_init():
  try:
    BaseTransform()
  except Exception:
    pytest.fail("BaseTransform constructor failed")

@pytest.mark.parametrize("test_input", [
  (None),
  ([]),
])
def test_base_transform_execute_empty_sets(test_input):
  bt = BaseTransform()
  output = bt.execute(test_input)

  assert(isinstance(output, list) == True)