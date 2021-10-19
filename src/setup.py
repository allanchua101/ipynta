from setuptools import setup, find_packages
from pathlib import Path

doc_path = Path("./README.md")

if (doc_path.exists()):
      long_description = doc_path.read_text()
else:
      long_description = "We're fixing our docs!"

setup(name='ipynta',
      version='0.0.12',
      long_description=long_description,
      long_description_content_type='text/markdown',
      description="A Python library for different image processing tasks.",
      packages=find_packages(),
      author="Allan Chua",
      install_requires=[
            "pathlib",
            "pillow"
      ],
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