from generator.Generator import *
import sys

def main(type, cardinality, size=0):
	gen = Generator(type, cardinality, size)
	gen.generate_data()
	gen.print_return_list()

def usage():
	print("usage:")
	print("	python3 main.py type cardinality <size>")

if __name__ == "__main__":
	if len(sys.argv) < 3:
		usage()
		exit(0)
	t = sys.argv[1]
	c = int(sys.argv[2])
	if len(sys.argv) == 4:
		s = int(sys.argv[3])
	else:
		s = 0
	main(t, c, s)