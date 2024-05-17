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

    def delete(self, file_path):
        """Delete the specified file."""
        try:
            os.chmod(file_path, 0o644)  # Set file to writable
            os.remove(file_path)
        except OSError as e:
            raise OSError(f"Cannot delete file '{file_path}': {e}")

    def list_files(self, directory=None):
        """List the files in the specified directory."""
        if directory is None:
            directory = self.current_directory
        try:
            return os.listdir(directory)
        except OSError as e:
            raise OSError(f"Cannot list files in '{directory}': {e}")

    

    def calculate_file_hash(self, file_path):
        """Calculate the SHA-256 hash of a file."""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
            return file_hash.hexdigest()
        except OSError as e:
            raise e


    def copy_file(self, source_file, destination_dir):
        """
        Copy a file from the source path to the destination directory.
    
        Args:
            source_file (str): The path of the file to be copied.
            destination_dir (str): The path of the destination directory.
        """
        try:
            if not os.path.exists(source_file):
                raise OSError(f"Source file '{source_file}' does not exist.")
    
            if not os.path.isdir(destination_dir):
                raise OSError(f"Destination directory '{destination_dir}' does not exist.")
    
            # Check if the destination directory is writable
            if not os.access(destination_dir, os.W_OK):
                raise PermissionError(f"Cannot copy file to '{destination_dir}' (permission denied)")
    
            destination_file = os.path.join(destination_dir, os.path.basename(source_file))
            shutil.copy(source_file, destination_file)
        except OSError as e:
            raise OSError(f"Error copying file: {e}")
        except PermissionError as e:
            raise PermissionError(f"Permission denied to copy file: {e}")
