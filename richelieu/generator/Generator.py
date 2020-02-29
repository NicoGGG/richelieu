import random
import os
import sys

from .values.string import StringValue

class Generator(object):
	"""
	Object that takes a string representing a type, and an int representing cardinality as args
	Then generate a list of <type>, respecting de cardinality inputted.

	Supported types are: 'string', 'int'(wip), 'double'(wip)

	Eg. Generator('string', 5) will generate a random word and duplicate it 5 times. ['hello', 'hello', 'hello', 'hello', 'hello']

	A third arg (int) can be inputted to generate a fixed amount of data.

	Eg. Generator('string', 5, 10) will generate 2 random words and duplicate them 5 times.
	['hello', 'hello', 'hello', 'hello', 'hello',
	'world', 'world', 'world', 'world', 'world']

	Additional methods will allow you print it, write it into json file, or into csv file.
	"""
	def __init__(self, data_type, cardinality, size=0, filename=""):
		super(Generator, self).__init__()
		self.data_type = data_type
		self.cardinality = int(cardinality)
		self.size = int(size)
		self.return_list = []
		self.filename = filename
		if self.size == 0 or self.size < self.cardinality:
			self.size = self.cardinality
		print("data_type:", self.data_type)
		print("cardinality:", self.cardinality)
		print("size:", self.size)

	def generate_data(self):
		print("generating...")
		if self.data_type == 'string':
			StringValue().nextValue()
		elif self.data_type == 'int':
			self.generate_int()
		elif self.data_type == '':
			self.generate_int()
		elif self.data_type == 'int':
			self.generate_int()
	
	def read_dict(self):
		with open(self.filename) as f:
			self.word_list = f.read().splitlines()
			random.shuffle(self.word_list)

	def generate_string(self):
		"""
		Generates size number of string, each one being duplicated cardinality times. Check for duplicates to garantee requested cardinality
		WARNING: word_list * cardinality cannot be smaller than size. If that happens, return_list length will not exceed word_list * cardinality
		"""
		#self.word_list = ['hello', 'world']
		self.read_dict()
		word_list_length = len(self.word_list)
		if word_list_length * self.cardinality < self.size:
			self.size = len(self.word_list) * self.cardinality
			print("changed size to", self.size)
		while len(self.return_list) < self.size:
			self.random_word = self.word_list.pop()
			i = 0
			# if self.random_word in self.return_list:
			# 	continue
			while len(self.return_list) < self.size and i < self.cardinality:
				self.return_list += [self.random_word]
				i += 1

	def generate_int(self):
		"""
		Generates size number of int, each one being duplicated cardinality times. Check for duplicates to garantee requested cardinality
		WARNING: int_list * cardinality cannot be smaller than size. If that happens, return_list length will not exceed int_list * cardinality
		"""
		# Not checking for int_list < cardinality because it is assumed cardinality is never > 9223372036854775807
		current_int = 0
		while current_int < self.size:
			random_int = current_int
			i = 0
			while len(self.return_list) < self.size and i < self.cardinality:
				self.return_list += [random_int]
				i += 1
			current_int += 1

	def print_return_list(self):
		print(self.return_list)

