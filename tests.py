#!/usr/bin/env python3

from os.path import dirname, abspath
from os import chdir
import pytest
from typing import List

# set tests directory
TESTS_DIR = dirname(abspath(__file__)) + '/tests/'

def execute_pytests(paths: List[str]) -> None:
  ''' Allows running pytests in subdirectories
  :params paths: subdirectories in `tests` that contain pytest files
  :type paths: List[str]
  :rtype: None
  '''
  
  for path in paths:
    # set path for current working directory
    chdir(TESTS_DIR + path)
    # execute pytests in cwd
    pt = pytest.main()
    # exit loop if a pytest fails
    if pt.name == 'TESTS_FAILED':
      break
    
  return None
  
if __name__ == '__main__':
  # subdirectories in `tests` where pytests are located
  paths = [
    'problems/leetcode',
    'utils'
  ]
  
  execute_pytests(paths)
  
