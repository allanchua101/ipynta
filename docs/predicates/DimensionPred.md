# DimensionPred

`DimensionPred` class used for writing dimension-based predicates.

## Filtering by minimum width

You can improve the quality of your image datasets by removing images that are too small which causes deterioration in your model's quality.

```py
from ipynta.predicates import DimensionPred
from PIL import Image

img_list = [
    Image.open("./1x1.png"),
    Image.open("./1x1.jpg"),
    Image.open("./5x5.png"),
    Image.open("./5x5.jpg"),
  ]

predicate = DimensionPred(img_list)
output = predicate.filter(min_width=5)
count = len(output)

print(f"{count} images passed the predicate")
# OUTPUT: 2 images passed the predicate
```

## Filtering by minimum height

You can also filter by minimum height

```py
from ipynta.predicates import DimensionPred
from PIL import Image

img_list = [
    Image.open("./1x1.png"),
    Image.open("./1x1.jpg"),
    Image.open("./5x5.png"),
    Image.open("./5x5.jpg"),
  ]

predicate = DimensionPred(img_list)
output = predicate.filter(min_height=5)
count = len(output)

print(f"{count} images passed the predicate")
# OUTPUT: 2 images passed the predicate
```

## Filtering by minimum width and height

The sample below filters an image list using both minimum width and height

```py
from ipynta.predicates import DimensionPred
from PIL import Image

img_list = [
    Image.open("./1x1.png"),
    Image.open("./1x1.jpg"),
    Image.open("./5x5.png"),
    Image.open("./5x5.jpg"),
  ]

predicate = DimensionPred(img_list)
output = predicate.filter(min_height=5, min_width=5)
count = len(output)

print(f"{count} images passed the predicate")
# OUTPUT: 2 images passed the predicate
```
