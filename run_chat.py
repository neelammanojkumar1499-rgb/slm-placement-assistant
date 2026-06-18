#!/usr/bin/env python
"""Direct chat runner to avoid importing unneeded modules"""

import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from src.inference import chat

if __name__ == "__main__":
    chat()
