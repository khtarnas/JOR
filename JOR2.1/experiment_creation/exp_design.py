'''
Goal:
    Get a number of lists. The first list will be the
    order in which words (index positions) are
    studied (this variable is called "study_order").
    The second list will be the order in which words
    (index positions) are tested (this variable is
    called "test_order"). The third will be a list indicating
    the correct side on a test card in the order of test
    cards. The fourth will be the type of comparison made
    (e.g. 4 vs. 16) on a test card in the order of test cards.
    The fifth will be the order of comparisons ordered in the
    way they were presented (e.g. 68 vs 2 OR 2 vs 68 depending
    on which item was on the left and right of the card).
    These can be used to order the study and test periods in
    the jsPsych experiment.
'''
import random
import numpy as np

# A wordpool of indices. Each value will correspond with a
# index in a real wordpool. So the item "19" will correspond
# to the item wordpool[19] in an array called wordpool that
# contains real words.
word_pool = range(88) #wordpool is of size 576, but length must be 88 so words are only selected from a wordpool of max lengths

'''
To aid in the goal, we will maintain a list of studied items:
    It will start with 25 items that haven't been studied,
    but are part of the "Many" list (these are words that
    will never actually be studied, but will be tested on
    -- they are called "many" because subjects are asked to
    treat them as if they occurred "many" items ago). There
    will be an associated list that tracks when the word was
    studied -- index positions in the two lists will be common
    for the item and its position. The "Many" list's associated
    position will be 0. The associated list will be called
    "card_nums".
'''
# An array of words that can be tested (i.e. are
# testable).
testable = []

# An array of card numbers. Each number represents the card
# a word was presented on and the index of that number will
# be the same as the index of the associated word in the
# "testable" array.
card_nums = []

# An array of words that need to be studied.
# The items in this list will be studied and then removed and
# place in the testable list. Therefore this is a list of word
# that are available to be studied (i.e. studiable).
studiable = list(word_pool)

# The order in which words were tested at the end of the
# experiment. This is one of our desired outputs.
test_order = []

# The order in which words were studied at the end of the
# experiment. This is one of our desired outputs.
study_order = []

# The order of test cards and which side is correct on them.
correct_side_order = []

# The order of comparison types on the test cards in order of test cards.
comparison_type_order = []

# The order of comparisons where the comparison is ordered with the one
# presented on the left being first rather than in order of recency.
ordered_comparison_order = []

# A counter to track which card we are currently on. We will start
# with the first card (1). Only counts study cards, test cards are not
# considered in card distance.
counter = 0

# Numbers to play with to get the best option for V2.1
study_length = 11 # Number of study trial preceeding the test period, 11 works (when counter += 2 in study block), 
blocks = 1 # Number of blocks in which there is a single presentation of each comparison

# All of the possible comparisons that can and need to be made in each test block
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
Functions for experiment periods:
'''

# A helper function used for each study card. It will do the following
# twice as there are two words per card: A random item will be chosen
# from the list of studiable words. The item will be added to the list of
# testable words and to the list of the order in which the items were studied.
# The current card number (held by the variable counter) will be added to the
# list of card numbers so it is at the same index as the word is in the list
# "testable". Finally, the word will be removed from the studiable list as
# it is no longer studiable.
def study(study_order, studiable, testable, card_nums, index):
    for _ in range(2):
        val = random.choice(studiable)
        testable.append(val)
        study_order.append(val)
        card_nums.append(index)
        studiable.remove(val)


'''
Experiment:
'''

#STUDY PERIOD (present n study cards in a row):
for i in range(1, study_length):
    study(study_order, studiable, testable, card_nums, counter)
    counter+= 2 #changing this to be 1 means every other studied item will not be tested, but this will mean less context interferences

# TEST PERIOD (1 set of all comparisons -- scored alternation
# between study and test -- starting with study):
loops = 0
done = False
success = False

# Forever loop
while True: # loop for single block

    failed = False

    # If the variable 'done' get set to true then we can leave the forever loop
    if done:
        study_order = []
        study_order.extend(holder_study_order)
        studiable = []
        studiable.extend(holder_studiable)
        testable = []
        testable.extend(holder_testable)
        card_nums = []
        card_nums.extend(holder_card_nums)
        test_order = []
        test_order.extend(holder_test_order)
        correct_side_order = []
        correct_side_order.extend(holder_correct_side_order)
        comparison_type_order = []
        comparison_type_order.extend(holder_comparison_type_order)
        ordered_comparison_order = []
        ordered_comparison_order.extend(holder_ordered_comparison_order)

        break #correctly breaks

    # Set holder values to hold, but not change all the important variables
    holder_study_order = []
    holder_study_order.extend(study_order)
    holder_studiable = []
    holder_studiable.extend(studiable)
    holder_testable = []
    holder_testable.extend(testable)
    holder_card_nums = []
    holder_card_nums.extend(card_nums)
    holder_test_order = []
    holder_test_order.extend(test_order)
    holder_comparisons = []
    holder_comparisons.extend(comparisons)
    holder_correct_side_order = []
    holder_correct_side_order.extend(correct_side_order)
    holder_comparison_type_order = []
    holder_comparison_type_order.extend(comparison_type_order)
    holder_ordered_comparison_order = []
    holder_ordered_comparison_order.extend(ordered_comparison_order)

    #Only try certain amount of times
    loops += 1
    if loops >= 1000:
        raise ValueError(str(loops) + ' loops failed.')

    for i in range(blocks): #loop through every block

        if failed:
            break

        # Variables for the block
        failed = False # Boolean indicating whether a block failed
        success = False # Boolean indicating whether a block succeeded
        done = False
        inner_loops = 0

        # Create temporary variables for a reset
        count_tracker = 0
        temp_study_order = []
        temp_study_order.extend(holder_study_order)
        temp_studiable = []
        temp_studiable.extend(holder_studiable)
        temp_testable = []
        temp_testable.extend(holder_testable)
        temp_card_nums = []
        temp_card_nums.extend(holder_card_nums)
        temp_test_order = []
        temp_test_order.extend(holder_test_order)
        temp_comparisons = []
        temp_comparisons.extend(holder_comparisons)
        temp_correct_side_order = []
        temp_correct_side_order.extend(holder_correct_side_order)
        temp_comparison_type_order = []
        temp_comparison_type_order.extend(holder_comparison_type_order)
        temp_ordered_comparison_order = []
        temp_ordered_comparison_order.extend(holder_ordered_comparison_order)

        # Test Period (1 block at a time) (scored alternation between study and test)
        while True: # loop for single block

            # If the block has covered all the comparisons, move on to the next block
            if success:

                # Make temp changes permanent
                holder_study_order = []
                holder_study_order.extend(temp_study_order)
                holder_studiable = []
                holder_studiable.extend(temp_studiable)
                holder_testable = []
                holder_testable.extend(temp_testable)
                holder_card_nums = []
                holder_card_nums.extend(temp_card_nums)
                holder_test_order = []
                holder_test_order.extend(temp_test_order)
                holder_correct_side_order = []
                holder_correct_side_order.extend(temp_correct_side_order)
                holder_comparison_type_order = []
                holder_comparison_type_order.extend(temp_comparison_type_order)
                holder_ordered_comparison_order = []
                holder_ordered_comparison_order.extend(temp_ordered_comparison_order)

                done = True

                break

            if failed:
                #reset counter
                counter = counter - count_tracker
                count_tracker = 0
                inner_loops += 1
                #print(inner_loops)
                if inner_loops >= 1000:
                    done = False
                    break

            failed = False


            #set temp variables
            temp_study_order = []
            temp_study_order.extend(study_order)
            temp_studiable = []
            temp_studiable.extend(studiable)
            temp_testable = []
            temp_testable.extend(testable)
            temp_card_nums = []
            temp_card_nums.extend(card_nums)
            temp_test_order = []
            temp_test_order.extend(test_order)
            temp_comparisons = []
            temp_comparisons.extend(comparisons)
            temp_correct_side_order = []
            temp_correct_side_order.extend(correct_side_order)
            temp_comparison_type_order = []
            temp_comparison_type_order.extend(comparison_type_order)
            temp_ordered_comparison_order = []
            temp_ordered_comparison_order.extend(ordered_comparison_order)

            # Test Period (1 of 5 at a time) (scored alternation between study and test)
            for j in range(len(comparisons)):

                if failed:
                    break
                
                # Study:
                study(temp_study_order, temp_studiable, temp_testable, temp_card_nums, counter)

                # Test:
                tries = []
                tries.extend(temp_comparisons) # make a temp variable for the comparisons again specifically for this while true loop so we don't unnecessarily try a comparison that does not work twice.

                while True: # loop for a single comparison

                    comp = random.choice(tries)
                    l = list(comp)
                    random.shuffle(l)
                    first, second = tuple(l)

                    # Get the card numbers of the items
                    first = counter - first
                    second = counter - second

                    # if the comparison is available, pop the comparison from the list 'temp' add it to the temporary testing list
                    if first in temp_card_nums and second in temp_card_nums:
                        temp_comparisons.pop(temp_comparisons.index(comp))
                        if(temp_comparisons == []):
                            success = True

                        # Find positions of card nums
                        i_pos = temp_card_nums.index(first)
                        j_pos = temp_card_nums.index(second)

                        # Add comparison to comparison order and correct side to correct side order
                        temp_comparison_type_order.append(list(comp))
                        temp_ordered_comparison_order.append(l)
                        if (first > second):
                            temp_correct_side_order.append(0) #0 if the left one is more recent
                        else:
                            temp_correct_side_order.append(1) #1 if the right one is more recent

                        # Add the accepted items to test_order
                        temp_test_order.append(temp_testable[i_pos]) #add the item in the right position to test_order
                        temp_test_order.append(temp_testable[j_pos])
                        
                        #remove items from testable and card_nums
                        if (i_pos > j_pos):
                            temp_testable.pop(i_pos)
                            temp_testable.pop(j_pos)

                            temp_card_nums.pop(i_pos)
                            temp_card_nums.pop(j_pos)
                        else:
                            temp_testable.pop(j_pos)
                            temp_testable.pop(i_pos)

                            temp_card_nums.pop(j_pos)
                            temp_card_nums.pop(i_pos)

                        

                        break
                    # pop the comparison from the list 'tries' and try again
                    else:
                        tries.pop(tries.index(comp))
                        if(tries == []):
                            failed = True
                            break

                # Increment counter (by 2, one for study one for test):
                counter += 2
                count_tracker += 2

print("done")
