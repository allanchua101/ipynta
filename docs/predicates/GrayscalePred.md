# GrayscalePred

`GrayscalePred` is used for writing predicates related to grayscale inference.

### Finding grayscale images from a local drive

The sample below uses the `DirectorySniffer` class to list down the path of images from a specific directory and passes its output to `PillowLoader` to load images from a local directory. It then utilizes the `GrayscalePred` to find all grayscale and colored images.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import GrayscalePred

# Use DirectorySniffer to load images from your local drive.
sniffer = DirectorySniffer()
path_list = sniffer.get_img_paths("./test/images")

# Pass the list of image paths to the PillowLoader.load
# method to get your list of OpenCV images
loader = PillowLoader()
img_list = loader.load(path_list)

## Find gray images by passing True flag to the filter method
predicate = GrayscalePred(img_list)
grayscale_images = predicate.filter(is_grayscale=True)

## Find colored images by passing False flag to the filter method
colored_images = predicate.filter(is_grayscale=False)
```
