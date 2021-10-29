# GrayscaleTransform

`GrayscaleTransform` is used for creating grayscale versions of images.

### Performing a batch grayscaling operation

The sample below:

- Uses the `DirectorySniffer` class to list down the path of images from a specific directory
- It then passes its output to `PillowLoader` to load images from a local directory.
- It then utilizes the `GrayscaleTransform` class to generate grayscaled versions of the provided images.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import GrayscaleTransform

## Use DirectorySniffer to load images from local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## GrayscaleTransform class was used to create
## grayscale copies of the provided images
grayscale_img_list = GrayscaleTransform().execute(img_list)
```
