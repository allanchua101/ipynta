# PillowLoader

`PillowLoader` class used for loading Pillow images.

## How to load images from local drive

You can use the `ImageGlobber` class to list down the path of images from a specific directory and pass its output to `PillowLoader` to load images from your local drive.

```py
from ipynta.globbers import ImageGlobber
from ipynta.loaders import PillowLoader

# Use ImageGlobber to load images from your local drive.
globber = ImageGlobber("./test/images")
path_list = globber.get_img_paths()

# Pass the list of image paths to the PillowLoader.load
# method to get your list of Pillow images
pil_loader = PillowLoader()
img_list = pil_loader.load(path_list)
```
