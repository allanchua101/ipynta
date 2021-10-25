# TarExtractor

`TarExtractor` is used for extracting the contents of `TAR` files.

## Use-case

Data scientists would usually compress their image datasets inside a `TAR` file to achieve the following:

- Reduce number of HTTP transactions required to upload/download datasets to/from remote storages
- Reduce image dataset's size on disk

### Example Usage

```py
import ipynta.extractors import TarExtractor

tar_path = "./foo.tar"
dest_path = "./foo"

# Construct class and execute
extractor = TarExtractor(tar_path, dest_path)

# execute method returns the list of file paths
# extracted out of the TAR file.
files = extractor.execute()
```
