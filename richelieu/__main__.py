#!/usr/bin/env python
"""The main entry point. Invoke as `http' or `python -m httpie'.
"""
import sys


def main():
    from .core import main
    main()
    

if __name__ == '__main__':
    main()