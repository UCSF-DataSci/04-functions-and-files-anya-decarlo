#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse
def fibonnanci(limit):
    # Do something
	list = []
	a,b = 0,1 
	while a < limit: 
		list.append(a)
		a,b = b, a + b
	return list
	
	def write_file(list, file): 
		try: 
			with open(file, "w") as f: 
				for number in list: 
					f.write(f"{number} \n")
		except IOError as e: 
			print(f"Error writing to file: {e} ")
	
	
	if __name__ == "__main__":
		parser = argparse.ArgumentParser(description="Fibonacci numbers.")
		parser.add_argument("limit", type=int, help="The  limit for Fibonacci sequence is.")
		parser.add_argument("output_file", type=str, help="The output file name to save Fibonacci numbers.")
		args = parser.parse_args()
		fibonacci_numbers = generate_fibonacci(args.limit)
		write_fibonacci_to_file(fibonacci_numbers, args.output_file)
		print(f"Fibonacci numbers less than {args.limit} have been written to {args.output_file}.")
