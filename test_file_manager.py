import unittest
from unittest.mock import patch, mock_open
import os
import shutil
import hashlib
import tempfile

from file_manager import FileManager

class TestFileManager(unittest.TestCase):	
    def setUp(self):
        self.file_manager = FileManager()
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_files')
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file_path = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file_path, 'w') as f:
            f.write('test content')
        os.chmod(self.test_file_path, 0o400)  # Set file to read-only
        print(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        os.chmod(self.test_file_path, 0o644)  # Restore file permissions
        shutil.rmtree(self.test_dir)
        print(f"Finished test: {self._testMethodName}")
    
        
    def test_change_to_valid_directory(self):
        ''' testing by passing valid directory'''
        self.file_manager.change_directory(self.test_dir)
        self.assertEqual(self.file_manager.current_directory, self.test_dir)

    def test_change_to_root_directory(self):
        ''' testing by passing the root of the curent directory'''
        self.file_manager.change_directory('/')
        self.assertEqual(self.file_manager.current_directory, '/')
    def test_change_to_relative_directory(self):
        os.makedirs(os.path.join(self.test_dir, 'subdir'), exist_ok=True)
        self.file_manager.change_directory(os.path.join(self.test_dir, 'subdir'))
        self.assertEqual(self.file_manager.current_directory, os.path.join(self.test_dir, 'subdir'))

    def test_change_to_non_existent_directory(self):
        with self.assertRaises(OSError):
            self.file_manager.change_directory('/non-existent-directory')
            
    @patch('builtins.open', mock_open(read_data='test content'))
    def test_change_to_file_path(self):
        file_path = os.path.join(self.test_dir, 'test.txt')
        with open(file_path, 'w') as f:
            f.write('test content')

        with self.assertRaises(OSError) as context:
            self.file_manager.change_directory(file_path)
        self.assertIn('is not a valid directory', str(context.exception))

    def test_change_to_empty_path(self):
        with self.assertRaises(OSError):
            self.file_manager.change_directory('')

  
  
  
    @patch('builtins.open', mock_open(read_data='test content'))
    def test_read_file(self):
       file_path = os.path.join(self.test_dir, 'test.txt')
       with open(file_path, 'w') as f:
           f.write('test content')

       content = self.file_manager.read_file(file_path)
       self.assertEqual(content, 'test content')
       
    def test_read_non_existent_file(self):
       file_path = os.path.join(self.test_dir, 'non_existent.txt')
       with self.assertRaises(OSError):
           self.file_manager.read_file(file_path)
  
  

if __name__ == '__main__':
    unittest.main()