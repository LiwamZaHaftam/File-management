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
        if os.path.exists(self.test_file_path):
            os.chmod(self.test_file_path, 0o644)  # Restore file permissions
        shutil.rmtree(self.test_dir, ignore_errors=True)
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
           
     
    def test_read_file_with_permission_error(self):
        with patch('builtins.open', mock_open(read_data='test content')) as mock_file:
            mock_file.side_effect = PermissionError("Permission denied")
            with self.assertRaises(PermissionError) as context:
                self.file_manager.read_file(self.test_file_path)
            self.assertIn("Permission denied", str(context.exception))




    def test_create_file_in_valid_directory(self):
        """Test creating a file in a valid directory."""
        self.file_manager.change_directory(self.test_dir)
        new_file_path = os.path.join(self.test_dir, 'new_file.txt')
        self.file_manager.create_file('new_file.txt', 'new file content')
        self.assertTrue(os.path.exists(new_file_path))
        with open(new_file_path, 'r') as f:
            self.assertEqual(f.read(), 'new file content')


    def test_create_file_with_empty_filename(self):
        """Test creating a file with an empty filename."""
        with self.assertRaises(ValueError):
            self.file_manager.create_file('', 'new file content')
            
    def test_create_file_with_mock_open(self):
        """Test creating a file using a mocked open function."""
        with patch('builtins.open', mock_open()) as mock_open_func:
            self.file_manager.change_directory(self.test_dir)
            new_file_path = os.path.join(self.test_dir, 'new_file.txt')
            self.file_manager.create_file('new_file.txt', 'new file content')
            mock_open_func.assert_called_once_with(new_file_path, 'w')


    def test_delete_file_in_valid_directory(self):
        """Test deleting a file in a valid directory."""
        self.file_manager.change_directory(self.test_dir)
        file_path = os.path.join(self.test_dir, 'test.txt')
        self.file_manager.delete(file_path)
        self.assertFalse(os.path.exists(file_path))
        
    def test_delete_non_existent_file(self):
        """Test deleting a non-existent file."""
        non_existent_file = os.path.join(self.test_dir, 'non_existent.txt')
        with self.assertRaises(OSError):
            self.file_manager.delete(non_existent_file)


    
    def test_list_files_in_valid_directory(self):
        """Test listing files in a valid directory."""
        self.file_manager.change_directory(self.test_dir)
        files = self.file_manager.list_files()
        self.assertIn('test.txt', files)


    def test_list_files_in_empty_directory(self):
        """Test listing files in an empty directory."""
        empty_dir = os.path.join(self.test_dir, 'empty_dir')
        os.makedirs(empty_dir, exist_ok=True)
        self.file_manager.change_directory(empty_dir)
        files = self.file_manager.list_files()
        self.assertEqual(files, [])

    def test_list_files_in_non_existent_directory(self):
        """Test listing files in a non-existent directory."""
        non_existent_dir = os.path.join(self.test_dir, 'non_existent')
        with self.assertRaises(OSError):
            self.file_manager.list_files(non_existent_dir)


    
    def test_calculate_file_hash(self):
        """Test calculating the hash of a file."""
        file_path = os.path.join(self.test_dir, 'test.txt')
        expected_hash = hashlib.sha256('test content'.encode()).hexdigest()
        file_hash = self.file_manager.calculate_file_hash(file_path)
        self.assertEqual(file_hash, expected_hash)

    def test_calculate_hash_for_non_existent_file(self):
        """Test calculating the hash of a non-existent file."""
        non_existent_file = os.path.join(self.test_dir, 'non_existent.txt')
        with self.assertRaises(OSError):
            self.file_manager.calculate_file_hash(non_existent_file)

    def test_calculate_file_hash_with_empty_file(self):
        """Test calculating the hash of an empty file."""
        empty_file_path = os.path.join(self.test_dir, 'empty.txt')
        with open(empty_file_path, 'w') as f:
            pass
        file_hash = self.file_manager.calculate_file_hash(empty_file_path)
        expected_hash = hashlib.sha256().hexdigest()
        self.assertEqual(file_hash, expected_hash)

    def test_calculate_file_hash_with_large_file(self):
        """Test calculating the hash of a large file."""
        large_file_path = os.path.join(self.test_dir, 'large.txt')
        with open(large_file_path, 'wb') as f:
            f.write(os.urandom(1024 * 1024 * 10))  # 10 MB file
        file_hash = self.file_manager.calculate_file_hash(large_file_path)
        self.assertIsInstance(file_hash, str)
        self.assertEqual(len(file_hash), 64)  # SHA-256 hash length

    def test_calculate_file_hash_with_binary_file(self):
        """Test calculating the hash of a binary file."""
        binary_file_path = os.path.join(self.test_dir, 'binary.bin')
        with open(binary_file_path, 'wb') as f:
            f.write(b'\x00\x01\x02\x03\x04\x05\x06\x07')
        file_hash = self.file_manager.calculate_file_hash(binary_file_path)
        expected_hash = hashlib.sha256(b'\x00\x01\x02\x03\x04\x05\x06\x07').hexdigest()
        self.assertEqual(file_hash, expected_hash)


    def test_copy_file_to_non_existent_directory(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
