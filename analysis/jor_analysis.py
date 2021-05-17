'''
Goal: TODO
'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from db_conversion import df

# Import Data

comparisons = [(0, 2), (0, 4), (0, 16), (0, 68), (0, "many"), (2, 4), (2, 16), (2, 68), (2, "many"), (4, 16), (4, 68), (4, "many"), (16, 68), (16, "many"), (68, "many")]
distances = [0, 2, 4, 16, 68, 'many']

def average_for_comp(df, comp):
    ordered = df[df['left_comp_type'] == comp[0]]
    ordered = ordered[ordered['right_comp_type'] == comp[1]]
    inverse = df[df['left_comp_type'] == comp[1]]
    inverse = inverse[inverse['right_comp_type'] == comp[0]]
    temp = pd.concat([ordered, inverse])
    corr = temp[temp['correct_side'] == temp['chosen_side']]
    proportion = (len(corr)) / len(temp)
    return proportion

def graph_for_distance(distance, comparisons, distances, df):
    # for each comparison for this distance (i.e. 4 and 16) add the average to the y array in order (FOR COMP = DISTANCE, set to 0.5)
    y = []
    for i in range(len(distances)):
        if distances[i] == distance:
            y.append(0.5)
        elif i > distances.index(distance):
            y.append(average_for_comp(df, [distance, distances[i]]))
        else:
            y.append(average_for_comp(df, [distances[i], distance]))
    x = distances
    print(y)

    # graph the line:
    colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange']
    color = colors[distances.index(distance)]
    color = 'black' #TODO if don't want, remove

    # Set up graph
    # TEMPORARY SET UP
    fig, ax = plt.subplots()
    #plt.title('Cross Category Recency Judgements')
    plt.ylabel('Proportion Correct')
    plt.xlabel('Distance Compared To')
    plt.xticks(range(0, len(distances)))
    plt.ylim(0, 1)
    plt.yticks(np.linspace(0,1,11))
    ax.yaxis.set_ticks_position('both')
    ax.plot(x, y, clip_on = False, color = color, marker = 'o', label=distance)
    plt.legend()
    plt.show()

for i in distances:
    graph_for_distance(i, comparisons, distances, df)