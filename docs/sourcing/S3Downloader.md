# S3Downloader

`S3Downloader` class is used for retrieving files from AWS S3 buckets.

### Pre-requisites

In order to use this sourcing class, we have to install an extra dependency which is `boto3`.

```sh
pip3 install boto3
```

### Retrieving a TAR file from S3

The sample below:

- Constructs an `S3Downloader` class using the following parameters:

  - `aws_profile`: The [AWS profile name](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) used for accessing the target S3 bucket.
  - `bucket_name`: The name of the S3 bucket where the `tar` file is stored.
  - `object_key`: The `tar` file's s3 object key.
  - `local_file_path`: The local path where the `tar` file will get stored.

- Triggers the download process from s3 using the `execute` method.
- Utilizes the `TarExtractor` class to extract the images inside the tar file to a local directory (`./train`).

```py
from ipynta.sourcing import S3Downloader
from ipynta.extractors import TarExtractor

aws_profile="cats_corp"
s3_bucket_name="cats-ai-s3"
s3_object_key="train/cats.tar.gz"
local_tar_path = "./tmp/cats.tar.gz"

s3_downloader = S3Downloader(aws_profile, s3_bucket_name, s3_object_key, local_tar_path)

local_train_dir = "./train"

extractor = TarExtractor(local_tar_path, local_train_dir)
extractor.execute()
```
