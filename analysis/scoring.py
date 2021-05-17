
# Import libraries
import pandas as pd

# Import Data
df = pd.read_csv('alldata.csv')
left_corr = df[df['correct_side'] == 0]
left_corr = left_corr[left_corr['key_press'] == 65]
right_corr = df[df['correct_side'] == 1]
right_corr = right_corr[right_corr['key_press'] == 76]
proportion = (len(left_corr) + len(right_corr)) / len(df)
print(proportion)