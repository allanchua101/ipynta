from ipynta.sourcing import DirectorySniffer
from os import path

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"

def test_get_img_paths():
    globber = DirectorySniffer()
    img_paths = globber.get_img_paths(SAMPLES_DIR)
    actual = len(img_paths)
    expected = 6

    assert(actual == expected)

def test_get_img_paths_png():
    globber = DirectorySniffer()
    img_paths = globber.get_img_paths(SAMPLES_DIR)

    assert(any(path.endswith(".png") for path in img_paths))

def test_get_img_paths_jpg():
    globber = DirectorySniffer()
    img_paths = globber.get_img_paths(SAMPLES_DIR)

    assert(any(path.endswith(".jpg") for path in img_paths))