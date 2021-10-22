# ImageGlobber

`ImageGlobber` class is used to represent image globbing operation(s).

## Getting images from a directory

You can use the `ImageGlobber` class to list down the path of images from a specific directory.

```py
from ipynta.globbers import ImageGlobber

globber = ImageGlobber("./test/images")
img_paths = globber.get_img_paths()
```
