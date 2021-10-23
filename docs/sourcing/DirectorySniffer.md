# DirectorySniffer

`DirectorySniffer` class is used to load image metadata from a local directory.

## Sourcing image paths from a local directory

You can use the `DirectorySniffer` class to list down the path of images from a specific directory.

```py
from ipynta.sourcing import DirectorySniffer

sniffer = DirectorySniffer()
img_paths = sniffer.get_img_paths("./test/images")
```
