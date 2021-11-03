# ZipPackager

`ZipPackager` is used for extracting the contents of `zip` files.

## Use-case

Data scientists would usually compress their image datasets inside a zip file to achieve the following:

- Reduce number of HTTP transactions required to upload/download datasets to/from remote storages
- Reduce image dataset's size on disk

### Example Usage

```py
import ipynta.packaging import ZipPackager

zip_path = "./foo.zip"
dest_path = "./foo"

# Construct class
packager = ZipPackager(zip_path, dest_path)

# unpack method returns the list of file
# paths extracted out of the ZIP file.
files = packager.unpack()
```
