# GrayscalePred

`GrayscalePred` is used for writing predicates related to grayscale inference.

### Finding grayscale images from a local drive

The sample below uses the `DirectorySniffer` class to list down the path of images from a specific directory and passes its output to `PillowLoader` to load images from a local directory. It then utilizes the `GrayscalePred` to find all grayscale and colored images.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import GrayscalePred

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Find gray images by passing True
## flag to the filter method
gs_pred = GrayscalePred(is_grayscale=True)
grayscale_imgs = gs_pred.execute(img_list)

## Find colored images by passing False
## flag to the filter method
colored_pred = GrayscalePred(is_grayscale=False)
colored_imgs = colored_pred.execute(img_list)
```
