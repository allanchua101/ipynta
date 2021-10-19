from ipynta.globbers import ImageGlobber
from pathlib import Path

SAMPLES_DIR = (Path(__file__).parent.parent / "./imgs")

def test_get_img_paths():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()
    actual = len(img_paths)
    expected = 4

    assert(actual == expected)

def test_get_img_paths_png():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()

    assert(any(path.endswith(".png") for path in img_paths))

def test_get_img_paths_jpg():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()

    assert(any(path.endswith(".jpg") for path in img_paths))