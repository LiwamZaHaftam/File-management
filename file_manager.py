import os
import shutil
import hashlib

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
    def change_directory(self, path):
        """
        Change the current working directory to the specified path.

        Args: 
        path (str): The path to change the directory to.
        """
        if not path:
            raise OSError("Path cannot be empty")
        elif os.path.isdir(path):
            self.current_directory = path
        else:
            raise OSError(f"{path} is not a valid directory.")
        
    def read_file(self, file_path):
        """
        Read the content of the specified file.

        Args:
            file_path (str): The path of the file to read.

        Returns:
            str: The content of the file.
        """
        
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except OSError as e:
            raise e
        except PermissionError as e:
            raise PermissionError(f"Unable to read file {file_path} due to permission error: {e}")


    def create_file(self, filename, content):
        if not filename:
            raise ValueError("Filename cannot be empty")

        file_path = os.path.join(self.current_directory, filename)
        print(file_path)
        try:
            # Check if the directory is writable
            if not os.access(self.current_directory, os.W_OK):
                raise OSError(f"Cannot create file in {self.current_directory} (permission denied)")
            with open(file_path, 'w') as f:
                f.write(content)
        except OSError as e:
            if 'Permission denied' in str(e):
                raise OSError(f"Cannot create file in {self.current_directory} (permission denied)")
            else:
                raise e   

