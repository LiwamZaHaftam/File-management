# File Manager Test Suite

This repository contains a comprehensive test suite for the `FileManager` class, a utility for managing files and directories. The tests follow the Test-Driven Development (TDD) approach, ensuring that the `FileManager` class is thoroughly tested and its functionality is well-documented.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The `FileManager` class provides a set of methods for performing various file management operations, including:

- Changing the current directory
- Reading the contents of a file
- Creating a new file
- Deleting a file
- Listing files in a directory
- Calculating the hash of a file
- Copying a file
- Renaming a file

The test suite ensures that each of these methods works as expected, and that the class handles various edge cases and error scenarios.

## Requirements
To run the test suite, you'll need the following:

- Python 3.10 or later
- The `unittest` module (part of the Python standard library)

## Usage
You can clone the repository and navigate to the project directory:

```
git clone https://github.com/mearegteferi/File-management
cd File-management
```

To run the test suite, simply execute the `test_file_manager.py` script:

```
python test_file_manager.py
```

This will run all the test cases and display the results.

## Test Cases
The test suite includes the following test cases:

1. **Changing the Current Directory**:
   - `test_change_to_valid_directory`: Verifies that the `change_directory` method can change the current directory to a valid directory.
   - `test_change_to_root_directory`: Verifies that the `change_directory` method can change the current directory to the root directory.
   - `test_change_to_relative_directory`: Verifies that the `change_directory` method can change the current directory to a relative directory.
   - `test_change_to_non_existent_directory`: Verifies that the `change_directory` method raises an `OSError` when trying to change to a non-existent directory.
   - `test_change_to_file_path`: Verifies that the `change_directory` method raises an `OSError` when trying to change to a file path.
   - `test_change_to_empty_path`: Verifies that the `change_directory` method raises an `OSError` when trying to change to an empty path.

2. **Reading Files**:
   - `test_read_file`: Verifies that the `read_file` method can read the contents of an existing file.
   - `test_read_non_existent_file`: Verifies that the `read_file` method raises an `OSError` when trying to read a non-existent file.
   - `test_read_file_with_permission_error`: Verifies that the `read_file` method raises a `PermissionError` when trying to read a file with insufficient permissions.

3. **Creating Files**:
   - `test_create_file_in_valid_directory`: Verifies that the `create_file` method can create a new file in a valid directory.
   - `test_create_file_with_empty_filename`: Verifies that the `create_file` method raises a `ValueError` when trying to create a file with an empty filename.
   - `test_create_file_with_mock_open`: Verifies that the `create_file` method uses the `open` function correctly.

4. **Deleting Files**:
   - `test_delete_file_in_valid_directory`: Verifies that the `delete` method can delete an existing file.
   - `test_delete_non_existent_file`: Verifies that the `delete` method raises an `OSError` when trying to delete a non-existent file.

5. **Listing Files**:
   - `test_list_files_in_valid_directory`: Verifies that the `list_files` method can list the files in a valid directory.
   - `test_list_files_in_empty_directory`: Verifies that the `list_files` method returns an empty list when the directory is empty.
   - `test_list_files_in_non_existent_directory`: Verifies that the `list_files` method raises an `OSError` when trying to list files in a non-existent directory.

6. **Calculating File Hashes**:
   - `test_calculate_file_hash`: Verifies that the `calculate_file_hash` method can calculate the hash of an existing file.
   - `test_calculate_hash_for_non_existent_file`: Verifies that the `calculate_file_hash` method raises an `OSError` when trying to calculate the hash of a non-existent file.
   - `test_calculate_file_hash_with_empty_file`: Verifies that the `calculate_file_hash` method can calculate the hash of an empty file.
   - `test_calculate_file_hash_with_large_file`: Verifies that the `calculate_file_hash` method can calculate the hash of a large file.
   - `test_calculate_file_hash_with_binary_file`: Verifies that the `calculate_file_hash` method can calculate the hash of a binary file.

7. **Copying Files**:
   - `test_copy_file_to_non_existent_directory`: Verifies that the `copy_file` method raises an `OSError` when trying to copy a file to a non-existent directory.
   - `test_copy_non_existent_file`: Verifies that the `copy_file` method raises an `OSError` when trying to copy a non-existent file.

8. **Renaming Files**:
   - `test_rename_file_in_valid_directory`: Verifies that the `rename_file` method can rename a file in a valid directory.
   - `test_rename_file_with_empty_filename`: Verifies that the `rename_file` method raises a `ValueError` when trying to rename a file with an empty filename.
   - `test_rename_non_existent_file`: Verifies that the `rename_file` method raises an `OSError` when trying to rename a non-existent file.

## Contributing
If you find any issues or have suggestions for improvements, feel free to open a new issue or submit a pull request. Contributions are welcome!

