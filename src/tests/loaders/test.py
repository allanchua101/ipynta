from ipynta.loaders import OpenCVLoader
from os import path

SAMPLES_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/imgs"


loader = OpenCVLoader()
actual = loader.load([SAMPLES_DIR + "/1x1.png"])

print(type(actual))
