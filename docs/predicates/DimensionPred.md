# DimensionPred

`DimensionPred` class is used for writing dimension-based predicates.

## Use-case

In order to improve the quality of some image datasets, computer vision experts remove images that are either too small or too big. This allows them to eliminate outliers which improves a model's output.

## Filtering by minimum width

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are at least 5 pixels in width
output = DimensionPred(min_width=5).execute(img_list)
```

## Filtering by minimum height

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are at least 5 pixels in height
output = DimensionPred(min_height=5).execute(img_list)
```

## Filtering by minimum width and height

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are at least 5 pixels in height and width
output = DimensionPred(min_height=5, min_width=5).execute(img_list)
```

## Filtering by maximum width

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are not bigger than 5 pixels in width
output = DimensionPred(max_width=5).execute(img_list)
```

## Filtering by maximum height

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are not bigger than 5 pixels in height
output = DimensionPred(max_height=5).execute(img_list)
```

## Filtering by maximum width and height

```py
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.predicates import DimensionPred

paths = DirectorySniffer().get_img_paths("./images")
img_list = PillowLoader().load(paths)

# The line below returns all images
# that are not bigger than 5 pixels in height and width
output = DimensionPred(max_height=5, max_width=5).execute(img_list)
```
