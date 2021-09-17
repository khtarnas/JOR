import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

from db_conversion import df

def make_graph(df):
    # Set distances and comparisons
    distances = [4, 6, 8, 10, 14, 18, 22, 28, 34, 40]
    comparisons = []
    for i in distances:
        for j in distances:
            if i < j:
                comp = (i, j)
                comparisons.append(comp)

    print(comparisons)

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
        x = list(range(1,11))

        # graph the line:
        color = 'black'
        marker = 'o'

        #colors = ['black', 'm', 'blue', 'green', 'gold', 'tomato']
        colors = ['black', 'gray', 'black', 'gray', 'black', 'gray', 'black', 'gray', 'black', 'gray']
        color = colors[index]
        linestyles = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--']
        linestyle = linestyles[index]

        for i in range(len(y)):
            # can switch sign for different graph look
            if i < index:
                y[i] = 1 - y[i]

        # Graph line
        ax.plot(x, y, clip_on = False, linestyle = linestyle, color = color, marker = marker, label=distances[index])
        plt.text(x[index],
                 y[index],
                 '  ' + str(distances[index]),
                 verticalalignment = 'top')

    fig, ax = plt.subplots()
    plt.title('Cross Category Recency Judgements')
    plt.ylabel("Probability of Judging 'A' More Recent")
    plt.xlabel("Cards Since 'A'")
    #plt.xticks(range(0, len(distances)))
    plt.ylim(0, 1)
    plt.yticks(np.linspace(0,1,9))
    plt.xlim(0.4, 10.4)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], distances)
    ax.yaxis.set_ticks_position('both')

    for i in range(len(distances)):
        graph_for_distance(i, comparisons, distances, df)
        # ax.plot(range(list(1, 11)),
        #         [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        #         marker = '.',
        #         color = 'white',
        #         linestyle = 'None')

    plt.text(11 - 0.575, 0.325, 'Cards')
    plt.text(11 - 0.675, 0.275, "Since 'B'")
    #plt.savefig('jor_mimic.pdf', format='pdf', dpi=1200)
    plt.show()

#print(df)

#Call the function
make_graph(df)
