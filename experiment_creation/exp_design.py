'''
Goal:
    Get two lists. The first list will be the
    order in which words (index positions) are 
    studied (this variable is called "study_order").
    The second list will be the order in which words
    (index positions) are tested (this variable is
    called "test_order"). These can be used to order
    the study and test periods in the jsPsych experiment.
'''
import random

# A wordpool of indices. Each value will correspond with a
# index in a real wordpool. So the item "19" will correspond
# to the item wordpool[19] in an array called wordpool that 
# contains real words.
word_pool = range(261)

'''
List of studied items:
    It will start with 25 items that haven't
    been studied, but are part of the "Many"
    list. There will be an associated that
    tracks when the word was studied -- index
    position will be common for the item and
    its position. The "Many" list's associated
    position will be 0.
'''
# An array of words that can be tested (i.e. are
# testable). This will start with 25 items ("Many" words).
testable = random.sample(word_pool, 25)

# An array of card numbers. Each number represents the card
# a word was presented on and the index of that number will
# be the same as the index of the associated word in the
# "testable" array. This will start with 25 items (asociated
# with the "Many" words and indicating that they did not
# appear on any card or they appeared on the 0th card)
card_nums = [0] * 25

# A list of words remaining in the wordpool after 25 were removed
remaining = [x for x in word_pool if x not in testable]

# we need 10 'many' words that will not be studied for the prep period
# (in order to ensure that the 'many' words are appropriately distributed).
# There will be 5 'many' words for every 15 cards during the test period so
# 1/3 of cards in the prep period should have one 'many' word. With 32 cards
# in the prep period, this means we will have 10 'many' words appearing once every three cards.
prep_manys = random.sample(remaining, 10)

# An array of words that need to be studied.
# The items in this list will be studied and then removed and
# place in the testable list. Therefore this is a list of word
# that are available to be studied (i.e. studiable).
studiable = [x for x in remaining if x not in prep_manys]

# The order in which words were tested at the end of the
# experiment. This is one of our desired outputs.
test_order = []

# The order in which words were studied at the end of the
# experiment. This is one of our desired outputs.
study_order = []

# TODO description: the order of test cards and which side is correct on them
correct_side_order = []

# TODO description: the order of comparison types on the test cards
comparison_type_order = []

#TODO description: the order of comparisons with which one went first (on the left)
ordered_comparison_order = []

# A counter to track which card we are currently on. We will start
# with the first card (1). Only counts study cards, test cards are not
# considered in card distance.
counter = 1

#TODO: description
comparisons = [
    (0, 2),
    (0, 4),
    (0, 16),
    (0, 68),
    (0, "many"),
    (2, 4),
    (2, 16),
    (2, 68),
    (2, "many"),
    (4, 16),
    (4, 68),
    (4, "many"),
    (16, 68),
    (16, "many"),
    (68, "many")
] 

'''
Methods for experiment periods:
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

# A helper function to determine whether a word is usable for test in the
# prep period. We DO want to test "many" words, but that functionality is dealt
# with using a delay and the list called 'prep_manys'. This is the situation in
# which we are currently NOT doing a many word SO: if a many word is selection we
# will return False. Also, if there is only one item on the card that we are currently
# looking at then we'll return False. O.W. we'll return true.
def word_usable(card_nums, index, prev):
    #print(card_nums)
    #print(index == 0)
    #print(card_nums.count(index) == 1)

    # make sure a test card does not have two items from the same study card
    if (index == prev):
        return False
    
    # If even index, return true
    if (index == 0):
        return False
    else:
        if (index % 2 == 0 or index == 1):
            return True
        else:
            # If two of this index left, return true
            if (card_nums.count(index) == 2):
                return True
            else:
                # If one of the close cards indexes is empty, return false
                if ((index + 2) not in card_nums or (index - 2) not in card_nums):
                    return False
                else:
                    return True


'''
Experiment:
'''

#STUDY PERIOD (present six study cards in a row):
for i in range(1, 7):
    study(study_order, studiable, testable, card_nums, i)
    counter+= 1

# PREP PERIOD (32 sets of unscored alternation between study
# and test -- starting with study):
delay = 0 # setting the delay for 'many' items in the prep period
for i in range(counter, 32 + counter):

    # Study
    study(study_order, studiable, testable, card_nums, counter)

    # Test
    prev = 0 #previous item added to a test card
    for i in range(2):
        if (i == 0): #if this is the first item on the test card, we don't care
            prev = 0
        
        if (delay == 0):
            delay = 6
            item = random.choice(prep_manys)
            prep_manys.pop(prep_manys.index(item))
        else:
            while True:
                # Get a random item from the testable list and its position in the list
                item = random.choice(testable)
                pos = testable.index(item)
                #print('pos = ' + str(pos))

                # Get the associated card number for the randomly choosen testable item
                test = card_nums[pos]

                if word_usable(card_nums, test, prev):
                    prev = test #set prev to the test card so on the second item of a test card we can make sure it does not come from the same study card
                    break
            #once we get to this point, we have a valid testable item, 'item'
            testable.pop(pos)
            card_nums.pop(pos)
            delay = delay - 1
        test_order.append(item)

    #Increment counter
    counter += 2 #one for study and one for test (although test cards will not be recorded and their count will not be needed)

# TEST PERIOD (5 sets of 15 sets of scored alternation 
# between study and test -- starting with study):
for i in range(5): #5 different test periods
    #print()
    #print('entered BLOCK ' + str(i))

    # Variables for the block
    failed = False # Boolean indicating whether a block failed
    success = False # Boolean indicating whether a block succeeded
    # Create temporary variables for a reset
    count_tracker = 0
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
    while True: # loop for single block

        # If the block has covered all the comparisons, move on to the next block
        if success:

            # Make temp changes permanent
            study_order = []
            study_order.extend(temp_study_order)
            studiable = []
            studiable.extend(temp_studiable)
            testable = []
            testable.extend(temp_testable)
            card_nums = []
            card_nums.extend(temp_card_nums)
            test_order = []
            test_order.extend(temp_test_order)
            correct_side_order = []
            correct_side_order.extend(temp_correct_side_order)
            comparison_type_order = []
            comparison_type_order.extend(temp_comparison_type_order)
            ordered_comparison_order = []
            ordered_comparison_order.extend(temp_ordered_comparison_order)

            break

        if failed:
            #reset counter
            counter = counter - count_tracker
            count_tracker = 0
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
        for j in range(15):
            
            #print()
            #print('in BLOCK ' + str(i))
            #print(temp_card_nums)
            #print('entered COMPARISON ' + str(j))
            #print(temp_comparisons)

            if failed:
                break
            
            # Study:
            study(temp_study_order, temp_studiable, temp_testable, temp_card_nums, counter)

            # Test:
            #print('Block Options: ' + str(temp))
            tries = []
            tries.extend(temp_comparisons) # make a temp variable for the comparisons again specifically for this while true loop so we don't unnecessarily try a comparison that does not work twice.

            while True: # loop for a single comparison

                comp = random.choice(tries)
                l = list(comp)
                random.shuffle(l)
                first, second = tuple(l)

                # Get the card numbers of the items
                if first == 'many':
                    first = 0
                else:
                    first = counter - first

                if second == 'many':
                    second = 0
                else:
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
                    else:
                        temp_testable.pop(j_pos)
                        temp_testable.pop(i_pos)

                    temp_card_nums.pop(i_pos)
                    temp_card_nums.pop(j_pos)

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

# Note: this should be called from trial_creation.py