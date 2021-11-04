from ipynta.persistence import LocalPersister
from ipynta.enums import NamingStrategy
from ipynta.loaders import PillowLoader
from ipynta.sourcing import DirectorySniffer
from os import path
from PIL import Image
import uuid
import pytest
import shutil

DIR_PATH = path.dirname(path.dirname(path.abspath(__file__))) 
SAMPLES_DIR = f"{DIR_PATH}/imgs"
DEST_PATH = f"{DIR_PATH}/persistence/local_testing/test_outputs"

def load_single_img():
  return Image.open(f"{SAMPLES_DIR}/1x1.jpg")

def load_multiple_images():
  img_list = DirectorySniffer().get_img_paths(SAMPLES_DIR)

  return PillowLoader().load(img_list)

def get_output_files(dir):
  return DirectorySniffer().get_img_paths(dir)

def is_valid_uuid(val):
  try:
    uuid.UUID(str(val))
    return True
  except ValueError:
    return False

def generate_dump_path(name):
  return f"{DEST_PATH}/{name}"

@pytest.fixture(scope="session", autouse=True)
def clear_dst_folder():
  yield
  
  if path.exists(DEST_PATH):
    shutil.rmtree(DEST_PATH)

# regardless of parameter validity,
# we should have a peaceful construction.
@pytest.mark.parametrize("img_list, out_path, strat", [
  (None, DEST_PATH, NamingStrategy.UUID4),
  (None, DEST_PATH, NamingStrategy.NUMERICAL),
  ([], DEST_PATH, NamingStrategy.NUMERICAL),
  ([], DEST_PATH, NamingStrategy.UUID4),
  ([load_single_img()], None, NamingStrategy.NUMERICAL),
  ([load_single_img()], None, NamingStrategy.UUID4),
])
def test_local_persister_init(img_list, out_path, strat):
  try:
    LocalPersister(img_list, out_path, strat)
  except Exception:
    pytest.fail("LocalPersister construction failed")

# If output path is not specified or messed up,
# an exception should be raised to inform dev about
# output directory.
@pytest.mark.parametrize("img_list, out_path, strat", [
  ([load_single_img()], None, NamingStrategy.NUMERICAL),
  ([load_single_img()], "", NamingStrategy.UUID4),
  ([load_single_img()], " ", NamingStrategy.NUMERICAL),
  ([load_single_img()], "     ", NamingStrategy.NUMERICAL),
])
def test_local_persister_empty_output_path(img_list, out_path, strat):
  try:
    persister = LocalPersister(img_list, out_path, strat)
    persister.execute()
  except Exception as ex:
    assert str(ex) == "Please specify an output directory"

# Validate if the input amount and output amount matches.
@pytest.mark.parametrize("img_list, out_path, strat", [
  ([load_single_img()], generate_dump_path("1"), NamingStrategy.NUMERICAL),
  ([load_single_img()], generate_dump_path("2"), NamingStrategy.UUID4),
  (load_multiple_images(), generate_dump_path("3"), NamingStrategy.NUMERICAL),
  (load_multiple_images(), generate_dump_path("4"), NamingStrategy.UUID4),
])
def test_local_persister_output_count(img_list, out_path, strat):
  persister = LocalPersister(img_list, out_path, strat)
  persister.execute()
  output_files = get_output_files(out_path)

  input_count = len(img_list)
  output_count = len(output_files)

  assert input_count == output_count

# Validate if the output files exists.
@pytest.mark.parametrize("img_list, out_path, strat", [
  ([load_single_img()], generate_dump_path("5"), NamingStrategy.NUMERICAL),
  ([load_single_img()], generate_dump_path("6"), NamingStrategy.UUID4),
  (load_multiple_images(), generate_dump_path("7"), NamingStrategy.NUMERICAL),
  (load_multiple_images(), generate_dump_path("8"), NamingStrategy.UUID4),
])
def test_local_persister_output_files_exist(img_list, out_path, strat):
  persister = LocalPersister(img_list, out_path, strat)
  persister.execute()
  output_files = get_output_files(out_path)
  
  assert(all(map(lambda x: path.exists(x), output_files)))

# Validate UUID4 naming strategy
@pytest.mark.parametrize("img_list, out_path, strat", [
  ([load_single_img()], generate_dump_path("9"), NamingStrategy.UUID4),
  (load_multiple_images(), generate_dump_path("10"), NamingStrategy.UUID4),
])
def test_local_persister_guid_names(img_list, out_path, strat):
  persister = LocalPersister(img_list, out_path, strat)
  persister.execute()

  output_files = get_output_files(out_path)
  names = map(lambda x: path.basename(x).split(".")[0], output_files)
  validity_flags = list(map(lambda name : is_valid_uuid(name), names))

  assert(all(validity_flags))

# Validate Numerical naming strategy
@pytest.mark.parametrize("img_list, out_path, strat", [
  ([load_single_img()], generate_dump_path("11"), NamingStrategy.NUMERICAL),
  (load_multiple_images(), generate_dump_path("12"), NamingStrategy.NUMERICAL),
])
def test_local_persister_numerical_names(img_list, out_path, strat):
  persister = LocalPersister(img_list, out_path, strat)
  persister.execute()

  output_files = get_output_files(out_path)
  names = map(lambda x: path.basename(x).split(".")[0], output_files)
  validity_flags = list(map(lambda name : name.isnumeric(), names))

  assert(all(validity_flags))