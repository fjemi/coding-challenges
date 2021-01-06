#!/usr/bin/env python3

from get_modules_dir import get_modules_dir
get_modules_dir('problems/leetcode/')

from license_key_formatting import license_key_formatting

def test_license_key_formatting() -> None:
  '''
  '''
  test_cases = [
    {'S': '5f3Z-2e-9-w', 'K': 4, 'result': '5F3Z-2E9W'},
    {'S': '2-4A0r7-4k', 'K': 4, 'result': '24A0-R74K'},
    {'S': '2-5g-3-J', 'K': 2, 'result': '2-5G-3J'}
  ]
  
  for test in test_cases:
    LFK = license_key_formatting(test['S'], test['K'])
    assert LFK == test['result']

  return None