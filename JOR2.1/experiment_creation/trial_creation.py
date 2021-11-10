import sys
import os

# Open a txt file in writing mode
my_file = 'newest.txt'
file = open(my_file,"w")

all_test_orders = []
all_study_orders = []
all_correct_sides = []
all_comparison_type_orders = []
all_ordered_comparison_orders = []

num = 100

for _ in range(num):
    if 'exp_design' in sys.modules:   # If the file is already in the cache (already been called)
        sys.modules.pop('exp_design') # Remove it so it may be re-imported (and change)
    from exp_design import *

    all_test_orders.append(test_order)
    all_study_orders.append(study_order)
    all_correct_sides.append(correct_side_order)
    all_comparison_type_orders.append(comparison_type_order)
    all_ordered_comparison_orders.append(ordered_comparison_order)

# Write out everything to a file extension
file.write("let all_test_orders = [")
for i in range(num):
    file.write(str(all_test_orders[i]))
    if i == (num - 1):
        file.write("]")
    else:
        file.write(",")
    file.write("\n")
file.write("\n")

file.write("let all_study_orders = [")
for i in range(num):
    file.write(str(all_study_orders[i]))
    if i == (num - 1):
        file.write("]")
    else:
        file.write(",")
    file.write("\n")
file.write("\n")

file.write("let all_correct_sides = [")
for i in range(num):
    file.write(str(all_correct_sides[i]))
    if i == (num - 1):
        file.write("]")
    else:
        file.write(",")
    file.write("\n")
file.write("\n")

file.write("let all_comparison_type_orders = [")
for i in range(num):
    file.write(str(all_comparison_type_orders[i]))
    if i == (num - 1):
        file.write("]")
    else:
        file.write(",")
    file.write("\n")
file.write("\n")

file.write("let all_ordered_comparison_orders = [")
for i in range(num):
    file.write(str(all_ordered_comparison_orders[i]))
    if i == (num - 1):
        file.write("]")
    else:
        file.write(",")
    file.write("\n")
file.close()

# Change file extension to js
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.js')
