import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math

from db_conversion import df

# Create distance variables
first_distances = [4, 6, 8, 10, 14, 18, 22, 28, 34]
second_distances = [6, 8, 10, 16, 22, 30, 40]
comparisons = [
    [4,6],
    [4,8],
    [4,10],
    [4,16],
    [4,22],
    [4,30],
    [4,40],
    [6,8],
    [6,10],
    [6,16],
    [6,22],
    [6,30],
    [6,40],
    [8,10],
    [8,16],
    [8,22],
    [8,30],
    [8,40],
    [10,16],
    [10,22],
    [10,30],
    [10,40],
    [14,16],
    [14,22],
    [14,30],
    [14,40],
    [18,22],
    [18,30],
    [18,40],
    [22,30],
    [22,40],
    [28,30],
    [28,40],
    [34,40]
]

'''
    Recreating the accuracy graph from the JOI vs JOR paper by Mark Howard

    Takes in a specified pandas dataframe with the correct fields from
    the JOR v1.0 or v1.1 experiment and outputs a correctness graph in the
    manner of the JOI vs JOR paper.
'''

def recreate_accuracy_graph(df, comparisons, first_distances, second_distances):

    '''
    Computes the proportion correct across all subjects
    (an average correct per comparison)
    '''
    def average_for_comp(df, comp):
        ordered = df[df['left_comp_type'] == comp[0]]
        ordered = ordered[ordered['right_comp_type'] == comp[1]]
        inverse = df[df['left_comp_type'] == comp[1]]
        inverse = inverse[inverse['right_comp_type'] == comp[0]]
        temp = pd.concat([ordered, inverse])

        if len(temp) == 0:
            return 0.5

        corr = temp[temp['correct_side'] == temp['chosen_side']]
        proportion = (len(corr)) / len(temp)
        return proportion
    
    
    '''
    NOTE: this is standard error of the mean over subjects
    '''
    def ste_for_comp(df, comp):
        
        means = []
        for i in df['uniqueid'].unique():
            temp_df = df[df['uniqueid'] == i]
            means.append(average_for_comp(temp_df, comp))
        
        return stats.sem(means)
    
    '''
    '''
    def graph_for_first_distance(df, second_distances, dist):
        
        # Create lists to be filled and graphed
        x = []
        y = []
        yerr = []

        for i in second_distances:
            if i > dist:
                x.append(i)
                y.append(average_for_comp(df, [dist, i]))
                yerr.append(ste_for_comp(df, [dist, i]))

        x = np.array(x)
        y = np.array(y)
        yerr = np.array(yerr)
        
        # Set color and marker:
        color = 'black'
        marker = 'o'
        index = first_distances.index(dist)
        colors = ['lightgray', 'silver', 'darkgrey', 'gray', 'dimgrey', 'black', 'darkblue', 'coral', 'lightpink']
        color = colors[index]
        # markers = ['o', 'v', 's', 'P', 'd', 'X' ]
        # marker = markers[index]
        ax.plot(x, y, clip_on = False, color = color, marker = marker, label=dist)
        # ax.errorbar(x, y, yerr=yerr, clip_on = False, color = color, marker = marker, label=dist)

    # Create a plot to add lines to 
    fig, ax = plt.subplots()
    #plt.ylim(0, 1)
    plt.title('Accuracy In Cross Category Judgments')
    plt.ylabel('Accuracy')
    plt.xlabel('Lag to the less recent probe')
    ax.yaxis.set_ticks_position('both')

    # Graph each line
    for i in first_distances:
        graph_for_first_distance(df, second_distances, i)

    # Finish and show the plot
    lgd = plt.legend(title = 'Lag to the more\n  recent probe', fancybox=True, bbox_to_anchor=(1.32, 1))
    #plt.savefig('joir_accuracy_mimic.pdf', format='pdf', dpi=1200, bbox_extra_artists=[lgd], bbox_inches='tight')
    plt.show()


# Call function to create accuracy graph
recreate_accuracy_graph(df, comparisons, first_distances, second_distances)









