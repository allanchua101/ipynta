# LocalPersister

Class used for persisting pipeline outputs to the local drive.

### Saving augmented data to disk

The sample below:

- Utilizes `DirectorySniffer` and `PillowLoader` classes to load an existing image dataset.
- Augments the dataset by generating vertical and horizontal flip transforms
- Then utilizes `LocalPersister` instances to save the augmentation dataset to the disk.

```py
from ipynta.enums import NamingStrategy
from ipynta.sourcing import DirectorySniffer
from ipynta.loaders import PillowLoader
from ipynta.transform import HFlipTransform
from ipynta.transform import VFlipTransform
from ipynta.persistence import LocalPersister

## Use DirectorySniffer to load images
## from your local drive.
path_list = DirectorySniffer().get_img_paths("./test/images")
img_list = PillowLoader().load(path_list)

## Utilize flip transformers to augment the original
## image dataset and avoid bias against certain orientations
hflipped_list = HFlipTransform().execute(img_list)
vflipped_list = VFlipTransform().execute(img_list)

LocalPersister(hflipped_list, "./test/augmented/hflipped").execute()
LocalPersister(vflipped_list, "./test/augmented/vflipped").execute()
```
