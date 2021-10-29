# VFlipTransform

`VFlipTransform` is used for generating vertically flipped counterparts of provided image datasets.

### Running a vertical flip operation on a list of images.

The sample below:

- Uses the `DirectorySniffer` class to list down the path of images from a specific directory
- It then passes its output to `PillowLoader` to load images from a local directory.
- It then utilizes the `VFlipTransform` class to generate vertically flipped copies of the images.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import VFlipTransform

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Utilize VFlipTransform to create vertically
## flipped copies of the test images.
flipped_img_list = VFlipTransform().execute(img_list)
```
