'''
Goal: TODO
'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import Data
df = pd.read_csv('alldata.csv')

#comparisons = [(0, 2), (2, 4), (0, 4), (4, 16), (2, 16), (0, 16), (16, 68), (4, 68), (2, 68), (0, 68), (68, "many"), (16, "many"), (4, "many"), (2, "many"), (0, "many")]
comparisons = [(0, 2), (0, 4), (0, 16), (0, 68), (0, "many"), (2, 4), (2, 16), (2, 68), (2, "many"), (4, 16), (4, 68), (4, "many"), (16, 68), (16, "many"), (68, "many")]

proportions = []
labels = []
for i in comparisons:
    first, second = i
    string = str(first) + ',' + str(second)
    print(string)
    compdf = df[df['comparison_type'] == string]
    left_corr = compdf[compdf['correct_side'] == 0]
    left_corr = left_corr[left_corr['key_press'] == 65]
    right_corr = compdf[compdf['correct_side'] == 1]
    right_corr = right_corr[right_corr['key_press'] == 76]
    proportion = (len(left_corr) + len(right_corr)) / len(compdf)
    proportions.append(proportion)
    labels.append('(' + string + ')')

print(proportions)
plt.bar(labels, proportions)
plt.title('Cross Category Recency Judgements')
plt.ylabel('Proportion Correct')
plt.xlabel('Comparison Type')
plt.show()