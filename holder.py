# TEST PERIOD (5 sets of 15 sets of scored alternation 
# between study and test -- starting with study):
while True: # loop for entire test period
    for i in range(5): #5 different test periods
        print('entered BLOCK ' + str(i))

        # Make temporary list to hold comparisons
        temp = []
        temp.extend(comparisons)

        # A temporary holder for the test_order of the test period that can be reset if a deadend occurs
        final_temp_test = []

        failed = False # Boolean indicating whether a block failed
        success = False # Boolean indicating whether a block succeeded
        # Test Period (1 of 5 at a time) (scored alternation between study and test)
        while True: # loop for single block

            # If the block has covered all the comparisons, move on to the next block
            if success:
                break

            for i in range(15):

                if success:
                    break
                
                print()
                print('entered COMPARISON ' + str(i))

                # Study:
                study(study_order, studiable, testable, card_nums, counter)

                # Test:
                #print('Block Options: ' + str(temp))
                tries = []
                tries.extend(temp) # make a temp variable for the comparisons again specifically for this while true loop so we don't unnecessarily try a comparison that does not work twice.
                temp_test = [] # a temporary holder for the test_order of a specific test block that can be reset if a deadend occurs

                while True: # loop for a single comparison
                    #print('Comparison Options: ' + str(tries))
                    if not tries and temp: # no more tries...
                        print('no more tries...')
                        failed = True
                        break
                    elif not temp:
                        success = True
                        break
                    else:
                        failed = False

                    comp = random.choice(tries)
                    first, second = comp
                    #print('ATTEMPT')
                    #print(first)
                    #print(second)
                    #print('(BEFORE_COMP_CHECK: temp is currently: ' + str(temp))


                    # if the comparison is available, pop the comparison from the list 'temp' add it to the temporary testing list

                    if comp_available(counter, first, second, testable, card_nums):
                        temp.pop(temp.index(comp))
                        #print('(COMP_AVAILABLE: temp is currently: ' + str(temp))
                        print('success!')
                        #TODO: functionality of adding comp items to temp_test
                        break
                    # pop the comparison from the list 'tries' and try again
                    else:
                        print('failure...')
                        tries.pop(tries.index(comp))
                        #print('COMP_NOT_AVAILABLE: temp is currently : ' + str(temp))
                
                if (failed):
                    break

                # Increment counter (by 2, one for study one for test):
                counter+= 2 #TODO: make sure counter isn't messed up by errors












while True: # loop for a single comparison
                    #print('Comparison Options: ' + str(tries))
                    if not temp:
                        success = True
                        break

                    comp = random.choice(tries)
                    first, second = comp

                    # if the comparison is available, pop the comparison from the list 'temp' add it to the temporary testing list
                    if comp_available(counter, first, second, testable, card_nums):
                        temp.pop(temp.index(comp))
                        #print('(COMP_AVAILABLE: temp is currently: ' + str(temp))
                        print('success!')
                        #TODO: functionality of adding comp items to temp_test
                        break
                    # pop the comparison from the list 'tries' and try again
                    else:
                        raise ValueError('Some value did not match up...Rerun program.')
                
                if (failed):
                    break

                # Increment counter (by 2, one for study one for test):
                counter+= 2 #TODO: make sure counter isn't messed up by errors














        while True: # loop for single block

            # If the block has covered all the comparisons, move on to the next block
            if success:
                break
            
            print('greetings!')
            blah = False

            for i in range(15):

                if success:
                    break
                
                if i == 0:
                    print(blah)
                    if blah == True:
                        break
                    else:
                        blah = True
                
                print()
                print('entered COMPARISON ' + str(i))
                print(temp)

                # Study:
                study(study_order, studiable, testable, card_nums, counter)

                # Test:
                #print('Block Options: ' + str(temp))
                tries = []
                tries.extend(temp) # make a temp variable for the comparisons again specifically for this while true loop so we don't unnecessarily try a comparison that does not work twice.
                temp_test = [] # a temporary holder for the test_order of a specific test block that can be reset if a deadend occurs

                #while True: # loop for a single comparison
                #print('Comparison Options: ' + str(tries))
                if not temp:
                    success = True
                    #break

                comp = random.choice(temp)
                first, second = comp

                # if the comparison is available, pop the comparison from the list 'temp' add it to the temporary testing list
                if comp_available(counter, first, second, testable, card_nums):
                    temp.pop(temp.index(comp))
                    #print('(COMP_AVAILABLE: temp is currently: ' + str(temp))
                    print('success!')
                    #TODO: functionality of adding comp items to temp_test
                    #break
                # pop the comparison from the list 'tries' and try again
                else:
                    raise ValueError('Some value did not match up...Rerun program.')

                # Increment counter (by 2, one for study one for test):
                counter+= 2 #TODO: make sure counter isn't messed up by errors









# TEST PERIOD (5 sets of 15 sets of scored alternation 
# between study and test -- starting with study):
while True: # loop for entire test period
    for i in range(5): #5 different test periods
        print('entered BLOCK ' + str(i))

        # Make temporary list to hold comparisons -- passed by value (since I will be removing elements)
        temp = []
        temp.extend(comparisons)

        # A temporary holder for the test_order of the test period that can be reset if a deadend occurs TODO: need?
        final_temp_test = []

        failed = False # Boolean indicating whether a block failed
        success = False # Boolean indicating whether a block succeeded
        # Test Period (1 of 5 at a time) (scored alternation between study and test)

        # If the block has covered all the comparisons, move on to the next block
        if success:
            break
            
        print('greetings!')
        blah = False

        for i in range(15):

            if success:
                break
                
            if i == 0:
                print(blah)
                if blah == True:
                    break
                else:
                    blah = True
                
            print()
            print('entered COMPARISON ' + str(i))
            print(temp)

            # Study:
            study(study_order, studiable, testable, card_nums, counter)

            # Test:
            #print('Block Options: ' + str(temp))
            tries = []
            tries.extend(temp) # make a temp variable for the comparisons again specifically for this while true loop so we don't unnecessarily try a comparison that does not work twice.
            temp_test = [] # a temporary holder for the test_order of a specific test block that can be reset if a deadend occurs

            #while True: # loop for a single comparison
            #print('Comparison Options: ' + str(tries))
            if not temp:
                success = True
                #break

            comp = random.choice(temp)
            first, second = comp

            # if the comparison is available, pop the comparison from the list 'temp' add it to the temporary testing list
            if comp_available(counter, first, second, testable, card_nums):
                temp.pop(temp.index(comp))
                #print('(COMP_AVAILABLE: temp is currently: ' + str(temp))
                print('success!')
                #TODO: functionality of adding comp items to temp_test
                #break
            # pop the comparison from the list 'tries' and try again
            else:
                raise ValueError('Some value did not match up...Rerun program.')

            # Increment counter (by 2, one for study one for test):
            counter+= 2 #TODO: make sure counter isn't messed up by errors
