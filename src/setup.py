from setuptools import setup, find_packages
import os

README_PATH = "./README.md"

PROJECT_URLS = {
      "Source Code": "https://github.com/allanchua101/ipynta",
}


if (os.path.isfile(README_PATH)):
      with open(README_PATH) as f:
            long_description = "".join(f.readlines())
else:
      long_description = "We're fixing our docs!"

setup(name='ipynta',
      version='0.0.27',
      long_description=long_description,
      long_description_content_type='text/markdown',
      description="A Python library for different image processing tasks.",
      packages=find_packages(),
      author="Allan Chua",
      install_requires=["pillow"],
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
      project_urls=PROJECT_URLS,
      zip_safe=False)
