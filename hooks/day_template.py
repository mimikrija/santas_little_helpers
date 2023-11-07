import sys
import re
from os import path


string_format = re.compile(r'day[0-2][0-9]')
branch_name = sys.argv[1]

# if the branch name doesn't match e.g. "day04" format, quit
if string_format.search(branch_name) is None:
    quit()

day = branch_name[-2:]
day_filename = f'python/{day}.py'

# if python file already exists, do not overwrite
if path.isfile(day_filename):
    quit()

# finally, create a template for solving the day
with open(f'python/{day}.py', 'w') as file:
    file.write('from santas_little_helpers.helpers import *\n')
    file.write('\n\n')
    file.write(f'input_data = read_input({int(day)})\n')
    file.write('print(input_data[:4])\n')


