from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "PyPi Readme.md").read_text()

setup(name='ipynta',
      version='0.0.6',
      long_description=long_description,
      long_description_content_type='text/markdown',
      description="A Python library for different image processing tasks.",
      packages=find_packages(),
      author="Allan Chua",
      install_requires=[],
      author_email="allanchua.officefiles@gmail.com",
      keywords=["python", "images", "image utilities"],
      classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
      ],
      zip_safe=False)