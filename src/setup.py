from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "PyPi Readme.md").read_text()

setup(name='ipynta',
      version='0.0.5',
      long_description=long_description,
      long_description_content_type='text/markdown',
      description="A Python library for different image processing tasks.",
      packages=['ipynta'],
      author="Allan Chua",
      author_email="allanchua.officefiles@gmail.com",
      zip_safe=False)