# tests/conftest.py
# This file is automatically loaded by PyTest before running any test.
# It adds the root project folder to Python's path so tests can find the mock/ folder.

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
