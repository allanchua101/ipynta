# HFlipTransform

`HFlipTransform` is used for generating horizontally flipped counterparts of provided image datasets.

### Performing a batch horizontal flip operation.

The sample below:

- Uses the `DirectorySniffer` class to list down the path of images from a specific directory
- It then passes its output to `PillowLoader` to load images from a local directory.
- It then utilizes the `HFlipTransform` class to generate horizontally flipped copies of the images.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import HFlipTransform

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Utilize HFlipTransform to create horizontally
## flipped copies of the test images.
flipped_img_list = HFlipTransform().execute(img_list)
```
