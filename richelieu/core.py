"""
	Implémentation de la proclamation de la bonne parole.
 
	Usage:
 
	>>> from sm_lib import proclamer
	>>> proclamer()
"""
import argparse
import os
import platform
from typing import List, Union
from .generator.Generator import *
import sys

__all__ = ['generator']

def main(args: List[Union[str, bytes]] = sys.argv,):
	"""
	The main function.
	Pre-process args, handle some special types of invocations,
	and run the main program with error handling.
	Return exit status code.
	"""
	program_name, *args = args
	args = decode_raw_args(args, str)

	gen = Generator(*args)
	gen.generate_data()
	gen.print_return_list()

def usage():
	print("usage:")
	print("	python3 main.py type cardinality <size>")

def decode_raw_args(
	args: List[Union[str, bytes]],
	stdin_encoding: str
) -> List[str]:
	"""
	Convert all bytes args to str
	by decoding them using stdin encoding.
	"""
	return [
		arg.decode(stdin_encoding)
		if type(arg) == bytes else arg
		for arg in args
	]