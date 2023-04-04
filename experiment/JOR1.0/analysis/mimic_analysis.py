'''
Goal: TODO
'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from db_conversion import df

# get list of proportions correct, all BEFORE x comparison are inverted (e.g. 1 - y)
# graph with legend

comparisons = [(0, 2), (0, 4), (0, 16), (0, 68), (0, "many"), (2, 4), (2, 16), (2, 68), (2, "many"), (4, 16), (4, 68), (4, "many"), (16, 68), (16, "many"), (68, "many")]
distances = [0, 2, 4, 16, 68, 'many']
# For different graph look reverse distances list (make sure to alter elif statment in graph_for_distance func)
distances.reverse()

def average_for_comp(df, comp):
    ordered = df[df['left_comp_type'] == comp[0]]
    ordered = ordered[ordered['right_comp_type'] == comp[1]]
    inverse = df[df['left_comp_type'] == comp[1]]
    inverse = inverse[inverse['right_comp_type'] == comp[0]]
    temp = pd.concat([ordered, inverse])
    corr = temp[temp['correct_side'] == temp['chosen_side']]
    proportion = (len(corr)) / len(temp)
    return proportion

def graph_for_distance(index, comparisons, distances, df):
    # for each comparison for this distance (i.e. 4 and 16) add the average to the y array in order (FOR COMP = DISTANCE, set to 0.5)
    y = []
    for i in range(len(distances)):
        if i == index:
            y.append(0.5)
        # Switch sign if distances list is reversed
        elif i > distances.index(distances[index]):
            y.append(average_for_comp(df, [distances[index], distances[i]]))
        else:
            y.append(average_for_comp(df, [distances[i], distances[index]]))
    x = distances

    # graph the line:
    color = 'black'
    marker = 'o'
    
    colors = ['black', 'm', 'blue', 'green', 'gold', 'tomato']
    color = colors[index]
    #markers = ['o', 'v', 's', 'P', 'd', 'X' ]
    #marker = markers[index]

    for i in range(len(y)):
        # can switch sign for different graph look
        if i < index:
            y[i] = 1 - y[i]

    # Graph line
    ax.plot(x, y, clip_on = False, color = color, marker = marker, label=distances[index])

fig, ax = plt.subplots()
plt.title('Cross Category Recency Judgements')
plt.ylabel('Proportion Correct')
plt.xlabel('Distance Compared To')
plt.xticks(range(0, len(distances)))
plt.ylim(0, 1)
plt.yticks(np.linspace(0,1,11))
ax.yaxis.set_ticks_position('both')

for i in range(len(distances)):
    graph_for_distance(i, comparisons, distances, df)

plt.legend()
plt.show()