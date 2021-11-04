# Author: Allan Chua allanchua.officefiles@gmail.com

import boto3
from ipynta.validators import StringValidator

class S3Downloader:
  """Class used for downloading files from S3 buckets
  
  Attributes:
  ---------------
  aws_profile: str
    Name of the AWS profile to use.

  bucket_name: str
    Name of the S3 bucket.

  object_key: str
    Key of the object in the S3 bucket.
  
  local_file_path: str
    Path of the local file to be downloaded.

  Methods:
  ---------------
  execute:
    Method used for triggering the download of specified file from S3 bucket.
  """
  def __init__(self, aws_profile, bucket_name, object_key, local_file_path):
    """Constructor for S3Downloader class.

    Args:
    ---------------
    aws_profile: str
      Name of the AWS profile to use.

    bucket_name: str
      Name of the S3 bucket.
    
    object_key: str
      Key of the object in the S3 bucket.

    local_file_path: str
      Path of the local file to be downloaded.
    """
    self.aws_profile = aws_profile
    self.bucket_name = bucket_name
    self.object_key = object_key
    self.local_file_path = local_file_path

  def _build_client(self):
    return boto3.session.Session(profile_name=self.aws_profile).client('s3')

  def execute(self):
    """Method used for triggering the download of specified file from S3 bucket.
    
    Raises:
    ---------------
    Exception:
      - If the specified file does not exist in the S3 bucket.
      - No S3 bucket name specified.
      - No S3 object key specified.
      - No local download path specified.
      - No AWS profile name specified.
    """
    validator = StringValidator()

    if validator.is_empty(self.bucket_name):
      raise Exception("No S3 bucket name specified.")

    if validator.is_empty(self.object_key):
      raise Exception("No S3 object key specified.")

    if validator.is_empty(self.local_file_path):
      raise Exception("No local download path specified.")

    if validator.is_empty(self.aws_profile):
      raise Exception("No AWS profile name specified.")

    s3_client = self._build_client()
    s3_client.download_file(self.bucket_name, self.object_key, self.local_file_path)