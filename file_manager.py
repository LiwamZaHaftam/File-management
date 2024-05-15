import os
import shutil
import hashlib

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
    def change_directory(self, path):

        if not path:
            raise OSError("Path cannot be empty")
        elif os.path.isdir(path):
            self.current_directory = path
        else:
            raise OSError(f"{path} is not a valid directory.")