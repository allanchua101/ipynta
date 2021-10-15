from pyntor.globbing import ImageGlobber

SAMPLES_DIR = "./imgs"

def test_initializer():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()

    assert(len(img_paths) == 1)