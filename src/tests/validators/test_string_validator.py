from ipynta.validators import StringValidator
import pytest

@pytest.mark.parametrize("input, expected", [
  (None, True),
  ("", True),
  (" ", True),
  ("\t", True),
  ("This", False),
  (" Not Empty ", False),
])
def test_validate_string_empty(input, expected):
  validator = StringValidator()

  assert validator.is_empty(input) == expected