import zipfile
import os

# Author: Allan Chua allanchua.officefiles@gmail.com

class ZipExtractor:
    """Class used for extracting zip file contents
    
    Attributes:
      zip_file_path (str): path to the zip file.
      destination_path (str): path to the destination folder.
    """
    def __init__(self, zip_file_path, destination_path):
        self.zip_file_path = zip_file_path
        self.destination_path = destination_path

    def execute(self):
        """Execute the extraction of the zip file contents
        
        Returns:
          list[str]: List of extracted file paths.
        """
        extracted_files = []

        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            # TODO: Add path ensurement logic here
            zip_ref.extractall(os.path.dirname(self.destination_path))
            extracted_files = zip_ref.namelist()

        return extracted_files