# OpenCVLoader

`OpenCVLoader` class used for loading OpenCV images.

## Pre-requisites

Before using this module, please make sure that you've installed its dependencies using the shell commands below:

```sh
#!/bin/bash
pip install numpy opencv-python
```

### How to load images from local drive

You can use the `DirectorySniffer` class to list down the path of images from a specific directory and pass its output to `OpenCVLoader` to load images from your local drive.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import OpenCVLoader

# Use DirectorySniffer to load images from your local drive.
sniffer = DirectorySniffer()
path_list = sniffer.get_img_paths("./test/images")

# Pass the list of image paths to the OpenCVLoader.load
# method to get your list of OpenCV images
cv2_loader = OpenCVLoader()
img_list = cv2_loader.load(path_list)
```
