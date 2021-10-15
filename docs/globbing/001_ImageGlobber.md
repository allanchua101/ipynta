# ImageGlobber

`ImageGlobber` class is used to represent image globbing operation(s).

## get_img_paths()

You can use the `ImageGlobber` class to list down the path of images from a specific directory.

```py
from ipynta import ImageGlobber

globber = ImageGlobber("./test/images")
img_paths = globber.get_img_paths()
```
