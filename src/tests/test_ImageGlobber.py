from ..globbing import ImageGlobber

SAMPLES_DIR = "./images"

def test_initializer():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()

    assert(len(img_paths) == 1)