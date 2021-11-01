from ipynta.sourcing import DownloadKeyPair
import pytest

@pytest.mark.parametrize("dl_src, local_path, expected_validity", [
    ("https://localhost:8080/download", "./dl_kp/test_dest/", True),
    ("https://localhost:3000/download", "./", True),
    ("", "./dl_kp/test_dest/", False),
    (" ", "./dl_kp/test_dest/", False),
    (None, "./dl_kp/test_dest/", False),
    ("https://localhost:8080/download", "", False),
    ("https://localhost:8080/download", " ", False),
    ("https://localhost:8080/download", None, False),
])
def test_download_keypair_validity_check(dl_src, local_path, expected_validity):
    keypair = DownloadKeyPair(dl_src, local_path)
    actual_validity = keypair.is_valid()

    assert(actual_validity == expected_validity)

@pytest.mark.parametrize("dl_src, local_path", [
    ("https://localhost:8080/download", "./dl_kp/test_dest/"),
    ("https://localhost:3000/download", "./"),
    ("", "./dl_kp/test_dest/"),
    (" ", "./dl_kp/test_dest/"),
    (None, "./dl_kp/test_dest/"),
    ("https://localhost:8080/download", ""),
    ("https://localhost:8080/download", " "),
    ("https://localhost:8080/download", None,),
])
def test_download_keypair_constructor(dl_src, local_path):
  try:
    DownloadKeyPair(dl_src, local_path)
  except Exception:
    pytest.fail("DownloadKeyPair constructor failed")