# TrueFileTypePred

`TrueFileTypePred` is used for writing predicates used for searching images with file extensions that match / don't match their [true file types](https://www.opswat.com/products/metadefender/file-type-verification).

### Use-case

Being able to filter images that present inaccurate file extensions is a powerful capability that can prevent:

- Unhandled exceptions caused by image transformation processes that expect a certain file format.
- Attacks rooting from malicious files.

### Finding files with file extensions that don't match with their true file types.

The sample below:

- Uses the `DirectorySniffer` class to list down the path of images from a specific directory
- It then passes its output to `PillowLoader` to load images from a local directory.
- It then utilizes the `TrueFileTypePred` to get rid of images that don't present their actual file types.

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import TrueFileTypePred

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Get rid of images that don't represent their true file types
tft_pred = TrueFileTypePred(seek_accurate_files=True)
clean_img_list = tft_pred.execute(img_list)
```
