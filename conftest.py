"""Pytest configuration file.

Ensures the project root is on sys.path so tests can import app.py
regardless of the working directory pytest is invoked from.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
