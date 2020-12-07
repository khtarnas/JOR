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
word_pool = range(251)

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
card_num = [0] * 25

# An array of words that need to be both studied and tested.
# The items in this list will be studied and then removed and
# place in the testable list. Therefore this is a list of word
# that are available to be studied (i.e. studiable).
studiable = [x for x in word_pool if x not in testable]

# The order in which words were tested at the end of the
# experiment. This is one of our desired outputs.
test_order = []

# The order in which words were studied at the end of the
# experiment. This is one of our desired outputs.
study_order = []

# A counter to track which card we are currently on. We will start
# with the first card.
counter = 1

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
def study(study_order, studiable, testable, card_num, index):
    for _ in range(2):
            val = random.choice(studiable)
            testable.append(val)
            study_order.append(val)
            card_num.append(index)
            studiable.remove(val)

# A helper function to determine whethere a word is usable for test in the
# prep period. If the word is a "many" word (i.e. the value at the associated
# index on the card_num that indicates what card it appears on is zero) or if
# there is only one item from a particular card (meaning in the card_num list
# there is only one item with a specific number on it) then it is NOT a usable
# word, o.w. it is. TODO: we actually do want to include SOME "many" words.
def usable(card_num, index):
    if (index == 0) or (card_num.count(index) == 1)
        return False
    else:
        return True

'''
Experiment:
'''

#STUDY PERIOD (present six study cards in a row):
for i in range(1, 7):
    study(study_order, studiable, testable, card_num, i)
    counter+= 1

# PREP PERIOD (32 sets of unscored alternation between study
# and test -- starting with study):
for i in range(counter, 32 + counter):
    study(study_order, studiable, testable, card_num, i)
        
    for _ in range(2):
        #Test:
        while True: #replace this with a list of just one word per list.
            pos = testable.index(random.choice(testable))
            test = card_num[pos] #get the counted value associated with a randomly choosen studied item
            if usable(card_num, test): #if there are two values that 
                break
            
        #test is a valid index that we can use
        test_order.append(test)
        testable.pop(pos)
    
    #Increment counter
    counter += 1

# TEST PERIOD 
for i in range(5): #5 different test periods 
    #Test Period (1 of 5 at a time) (scored alternation between study and test)
    for i in range(counter, 15 + counter):
        #Study:
        study(study_order, studiable, testable, card_num, i)

        #Test:
        #Plan: Nested While True loops. On each card: If a comparison exists, continue to the next card, if it doesn't try a differnt comparison.
        #Comparisons

        #Increment counter:
        counter+= 1