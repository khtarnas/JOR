import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

import sys
import os

from db_conversion import df

# print(df[df['left_word_study'] == 'WHISKERS']['right_word_study'])
# print(df[df['left_word_test'] == 'WHISKERS'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
selected_columns = df[['left_word_study', 'right_word_study', 'left_word_test', 'right_word_test', 'left_comp_type', 'right_comp_type']]

# Open a txt file in writing mode
my_file = 'whoop.txt'
file = open(my_file,"w")

# Write out everything to a file extension
file.write(selected_columns.to_string())
file.close()

