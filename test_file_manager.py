import os
import unittest
from file_manager import FileManager
import shutil

class TestFileManager(unittest.TestCase):
  '''this will contain all the test for the project File Manager'''
  def setUp(self):
    '''setting up the environment before executing each test method'''
    self.file_manager = FileManager()
    self.test_file_path = 'test_file.txt'
    os.makedirs(self.test_dir, exist_ok=True)
  
  def tearDown(self):
    '''cleaning up the environment after executing each test method'''
    shutil.rmtree(self.test_dir)
