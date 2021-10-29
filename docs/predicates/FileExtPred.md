# FileExtPred

`FileExtPred` is used for writing predicates related to file extension inference.

### Finding .jpg images from a local drive

The sample below:

- Uses the `DirectorySniffer` class to list down the path of images from a specific directory
- It then passes its output to `PillowLoader` to load images from a local directory.
- And finally utilizes the `FileExtPred` to find all `.jpg` files from the Pillow collection.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import FileExtPred

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Find jpg images by passing '.jpg'
## flag to the filter method
fil_ext_pred = FileExtPred(".jpg")
jpg_list = fil_ext_pred.execute(img_list)
```
