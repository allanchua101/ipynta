# PillowLoader

`PillowLoader` class used for loading Pillow images.

## How to load images from local drive

You can use the `DirectorySniffer` class to list down the path of images from a specific directory and pass its output to `PillowLoader` to load images from your local drive.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader

# Use DirectorySniffer to load images from your local drive.
sniffer = DirectorySniffer()
path_list = sniffer.get_img_paths("./test/images")

# Pass the list of image paths to the PillowLoader.load
# method to get your list of Pillow images
pil_loader = PillowLoader()
img_list = pil_loader.load(path_list)
```
