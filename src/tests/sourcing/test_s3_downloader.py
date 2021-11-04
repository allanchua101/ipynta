from unittest.mock import Mock
from ipynta.sourcing import S3Downloader
from os import path
import pytest

DIR_PATH = path.dirname(path.dirname(path.abspath(__file__))) 
SAMPLES_DIR = f"{DIR_PATH}/imgs"
DEST_PATH = f"{DIR_PATH}/sourcing/s3_testing/test_dls"
MOCK_S3_URI = "s3://ipynta-test-s3"

@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  ("aws_bar", "ipynta-test-s3", "1x1_red.jpg", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  # No profile name
  (None, "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  (" ", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  # No bucket name
  ("aws_foo", None, "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", " ", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  # No object key
  ("aws_foo", "ipynta-test-s3-v2", None, f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", "", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", " ", f"{DEST_PATH}/1x1_red.jpg"),
  # No destination path
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", None),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f""),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f" "),
])
def test_s3_downloader_constructor(profile, bucket_name, obj_key, dst_path):
  try:
    # regardless of parameter validity,
    # we should have a peaceful construction.
    S3Downloader(profile, bucket_name, obj_key, dst_path)
  except Exception:
    pytest.fail("S3Downloader construction failed")

# Test happy path
@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  ("aws_bar", "ipynta-test-s3", "1x1_red.jpg", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
])
def test_s3_download_invoked(profile, bucket_name, obj_key, dst_path):
  downloader = S3Downloader(profile, bucket_name, obj_key, dst_path)

  s3_client_mock = Mock()

  downloader._build_client = Mock(return_value=s3_client_mock)
  downloader.execute()
  
  assert s3_client_mock.download_file.called
  assert s3_client_mock.download_file.call_count == 1

# Test illegal profile names.
@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  (None, "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  (" ", "ipynta-test-s3-v2", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
])
def test_s3_downloader_bad_aws_profile(profile, bucket_name, obj_key, dst_path):
  try:
    downloader = S3Downloader(profile, bucket_name, obj_key, dst_path)
    downloader.execute()
  except Exception as ex:
    assert str(ex) == "No AWS profile name specified."

# Test illegal bucket names.
@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  ("aws_foo", None, "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", " ", "1x1_red.png", f"{DEST_PATH}/1x1_red.jpg"),
])
def test_s3_downloader_bad_bucket(profile, bucket_name, obj_key, dst_path):
  try:
    downloader = S3Downloader(profile, bucket_name, obj_key, dst_path)
    downloader.execute()
  except Exception as ex:
    assert str(ex) == "No S3 bucket name specified."

# Test illegal object keys
@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  ("aws_foo", "ipynta-test-s3-v2", None, f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", "", f"{DEST_PATH}/1x1_red.jpg"),
  ("aws_foo", "ipynta-test-s3-v2", " ", f"{DEST_PATH}/1x1_red.jpg"),
])
def test_s3_downloader_bad_object_key(profile, bucket_name, obj_key, dst_path):
  try:
    downloader = S3Downloader(profile, bucket_name, obj_key, dst_path)
    downloader.execute()
  except Exception as ex:
    assert str(ex) == "No S3 object key specified."

# Test bad destination paths
@pytest.mark.parametrize("profile, bucket_name, obj_key, dst_path", [
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", None),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f""),
  ("aws_foo", "ipynta-test-s3-v2", "1x1_red.png", f" "),
])
def test_s3_downloader_bad_dst_path(profile, bucket_name, obj_key, dst_path):
  try:
    downloader = S3Downloader(profile, bucket_name, obj_key, dst_path)
    downloader.execute()
  except Exception as ex:
    assert str(ex) == "No local download path specified."