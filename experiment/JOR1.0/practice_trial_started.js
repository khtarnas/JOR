/*
 * Requires:
 *     wordpool.js
 *     exp_orders.js
 */

let psiturk = new PsiTurk(uniqueId, adServerLoc, mode);

// Record screen resolution & available screen size
psiturk.recordUnstructuredData('screen_width', screen.width)
psiturk.recordUnstructuredData('screen_height', screen.height)
psiturk.recordUnstructuredData('avail_screen_width', screen.availWidth)
psiturk.recordUnstructuredData('avail_screen_height', screen.availHeight)
psiturk.recordUnstructuredData('color_depth', screen.colorDepth)
psiturk.recordUnstructuredData('pixel_depth', screen.pixelDepth)

let mycondition = condition;  // these two variables are passed by the psiturk server process
let mycounterbalance = counterbalance;  // they tell you which condition you have been assigned to

// If we don't have a counterbalance from psiTurk during testing
let testing = true;
if (testing) {
    mycounterbalance = Math.floor(Math.random() * 100);
}

let run_exp = function() {
    wordpool = jsPsych.randomization.repeat(wordpool, 1);

    // Trial 1 Variables
    wordpool1 = wordpool.slice(0, 261);
    counterbalance1 = mycounterbalance;
    study_order = all_study_orders[counterbalance1]
    test_order = all_test_orders[counterbalance1]
    correct_side_order = all_correct_sides[counterbalance1]
    comparison_type_order = all_comparison_type_orders[counterbalance1]
    ordered_comparison_order = all_ordered_comparison_orders[counterbalance1]

    // Trial 2 Variables
    wordpool2 = wordpool.slice(261, 522);
    counterbalance2 = 99 - mycounterbalance;
    study_order2 = all_study_orders[counterbalance2]
    test_order2 = all_test_orders[counterbalance2]
    correct_side_order2 = all_correct_sides[counterbalance2]
    comparison_type_order2 = all_comparison_type_orders[counterbalance2]
    ordered_comparison_order2 = all_ordered_comparison_orders[counterbalance2]

    // Practice list Variables
    practice_wordpool = wordpool.slice(522, 562); // the word pool for the practice list
    practice_studied = wordpool.slice(562, 569); // the studied items for the practice list (initially contains 7 "many" items)

    //Time of study
    let length = "four seconds";
    let time = 4000; // the number of millisecond of the above string, normal value = 4000
    let gap = 750; // the length of the gap of time after each card is present (in milliseconds), normal value: 750

    /****************************************************************************************
     ****************************** Experiment Begins ***************************************
    ****************************************************************************************/

    let enter_name = {
        type: 'survey-html-form',
        post_trial_gap: 200,
        response_ends_trial: true,
        timeline: [{preamble: "<p>Please enter your name: </p>", html:'<p><input type="text" id="name" name="name" autocomplete="off" required></p>', data: {type: 'NAME'}}],
    };

    // Welcome event
    let welcome = {
        type: "html-keyboard-response",
        post_trial_gap: 200,
        stimulus: "Welcome to the <strong>Judgment of Recency</strong> experiment! <p>Press the Space Bar to see the instructions.</p>",
        choices: [' ']
    };

    // Instructions event
    let instructions = {
        type: "html-keyboard-response",
        stimulus: "<p>In this experiment, you will encounter a number of study and question cards." + 
                "<p>The <strong>study cards</strong> will have two words on them. Take note of these words; you will" + 
                " be asked to judge how recently you have seen them. You will have " + length + " to look at each study card." + "</p>" +

                "<p>The <strong>question cards</strong> will also show you two words (with a red question mark between the words to show" + 
                " that it is a question card). When you encounter a question card, indicate which of the two words shown have been" + 
                " seen on a study card most recently. If a word has not been seen on a study card yet, treat the word " + 
                "as if it occurred a very long time ago. You will indicate which word occurred most recently with the " +
                "‘A’ key for the word on the left side and the ‘L’ key for the word on the right side (not case sensitive).</p>" +

                "<p>Each word will be seen at most twice: once on a study card and once on a question card.</p>" +

                "<p>There will be two trials (each around 15 - 20 minutes long) with a break in between.</p>" +

                "<p>Press the Space Bar to continue.</p>",
        choices: [' '],
        post_trial_gap: 200
        };

    // Warning event
    let warning = {
        type: "html-keyboard-response",
        stimulus: "<p>Trial 1 will last approximately 15 - 20 minutes." + 
                "<p>Please make sure you will not need to leave during that duration before starting.<p>" + 
                "<p>To begin <Strong>Trial 1</Strong>, press the Space Bar.</p>",
        choices: [' '],
        post_trial_gap: 200
    };

    // Create a timeline and add events:
    let timeline = [];
    timeline.push(enter_name);
    timeline.push(welcome);
    timeline.push(jsPsychUtils.get_attention_check());
    timeline.push(instructions);
    timeline.push(warning);

    /****************************************************************************************
     ************************** Practice Trial Begins ***************************************
    ****************************************************************************************/

    // Practice Trials Label Warning
    let practice_trial = {
        type: "html-keyboard-response",
        stimulus: "<p>The practice trial will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(practice_trial);

    // First 5 are study cards, then rest alternate
    for (let i = 0; i < 5; i++) { 

        // Grab two words to be studied in the right order
        let one = practice_wordpool.shift();
        let two = practice_wordpool.shift();
        practice_studied.push(one);
        practice_studied.push(two);

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card);
    }

    // Prep Period: alternate study and test (no special comparisons or correct answers):
    while (practice_wordpool.length > 0 && practice_studied.length > 0) {

        // Grab two words to be studied in the right order
        let one = practice_wordpool.shift();
        let two = practice_wordpool.shift();
        practice_studied.push(one);
        practice_studied.push(two);

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)

        // Grab two words to be tested in the right order
        let index = Math.floor(Math.random() * practice_studied.length);
        one = practice_studied[index];
        practice_studied.splice(index, 1);

        index = Math.floor(Math.random() * practice_studied.length);
        two = practice_studied[index];
        practice_studied.splice(index, 1);

        let prep_question_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px;">' + one + 
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['a', 'l'],
            post_trial_gap: gap,
            data: {trial_type: "practice",
                left_word_test: one,
                right_word_test: two
            }
        }
        timeline.push(prep_question_card)
    }

    /****************************************************************************************
     ****************************** Trial 1 Begins ******************************************
    ****************************************************************************************/

    // Trial 1 Label Warning
    let trial_one = {
        type: "html-keyboard-response",
        stimulus: "<p>Trial 1 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(trial_one);

    //First 6 are study cards, then rest alternate
    for (let i = 0; i < 6; i++) { 

        // Grab two words to be studied in the right order
        let one = study_order.shift();
        one = wordpool1[one];
        let two = study_order.shift();
        two = wordpool1[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)
    }

    // Prep Period: alternate study and test for the next 32 trials (no special comparisons or correct answers):
    for (let i = 0; i < 32; i++) {

        // Grab two words to be studied in the right order
        let one = study_order.shift();
        one = wordpool1[one];
        let two = study_order.shift();
        two = wordpool1[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)

        // Grab two words to be tested in the right order
        one = test_order.shift();
        one = wordpool1[one];
        two = test_order.shift();
        two = wordpool1[two];

        let prep_question_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px;">' + one + 
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['a', 'l'],
            post_trial_gap: gap,
            data: {trial_type: "prep",
                left_word_test: one,
                right_word_test: two
            }
        }
        timeline.push(prep_question_card)
    }

    // Test Period: alternate study and test for the final 75 trials:
    for (let i = 0; i < 75; i++) {

        // Grab two words to be studied in the right order
        let one = study_order.shift();
        one = wordpool1[one];
        let two = study_order.shift();
        two = wordpool1[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)

        // Grab two words to be tested in the right order
        one = test_order.shift();
        one = wordpool1[one];
        two = test_order.shift();
        two = wordpool1[two];

        // Grab the comparison type and correct answer side:
        comp = comparison_type_order.shift();
        side = correct_side_order.shift();
        ordered_comp = ordered_comparison_order.shift();
        first_comp = ordered_comp[0]
        second_comp = ordered_comp[1]

        let test_question_card = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px;">' + one + 
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['a', 'l'],
            post_trial_gap: gap,
            data: {trial_type: "test",
                comparison_type: comp,
                left_word_test: one,
                right_word_test: two,
                left_comp_type: first_comp,
                right_comp_type: second_comp,
                correct_side: side
            },
            on_finish: function(data) {
                if (data.key_press == 65){
                    data.chosen_side = 0;
                } else if (data.key_press == 76) {
                    data.chosen_side = 1; 
                } else {
                    data.chosen_side = null;
                }
            }
        };
        timeline.push(test_question_card)

    }

    /****************************************************************************************
     ****************************** Trial 2 Begins ******************************************
    ****************************************************************************************/

    // Trial 2 Label
    let trial_two = {
        type: "html-keyboard-response",
        stimulus: "<p>Congratulations on completing the first trial!</p>" + 
            "<p>Feel free to take a short break here and begin the next trial when you are ready.</p>" +
            "<p>To begin Trial 2, press the Space Bar.</p>",
        choices: [' '],
        post_trial_gap: gap
    };
    timeline.push(trial_two);

    // Trial 1 Label Warning
    let trial_two_warning = {
        type: "html-keyboard-response",
        stimulus: "<p>Trial 2 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(trial_two_warning);

    //First 6 are study cards, then rest alternate
    for (let i = 0; i < 6; i++) { 

        // Grab two words to be studied in the right order
        let one = study_order2.shift();
        one = wordpool2[one];
        let two = study_order2.shift();
        two = wordpool2[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 2,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)
    }

    // Prep Period: alternate study and test for the next 32 trials (no special comparisons or correct answers):
    for (let i = 0; i < 32; i++) {

        // Grab two words to be studied in the right order
        let one = study_order2.shift();
        one = wordpool2[one];
        let two = study_order2.shift();
        two = wordpool2[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 2,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)

        // Grab two words to be tested in the right order
        one = test_order2.shift();
        one = wordpool2[one];
        two = test_order2.shift();
        two = wordpool2[two];

        let prep_question_card = {
            trial: 2,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px;">' + one + 
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['a', 'l'],
            post_trial_gap: gap,
            data: {trial_type: "prep",
                left_word_test: one,
                right_word_test: two
            }
        }
        timeline.push(prep_question_card)
    }

    // Test Period: alternate study and test for the final 75 trials:
    for (let i = 0; i < 75; i++) {

        // Grab two words to be studied in the right order
        let one = study_order2.shift();
        one = wordpool2[one];
        let two = study_order2.shift();
        two = wordpool2[two];

        // Create a study event and add it to the timeline
        let study_card = {
            trial: 2,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {left_word_study: one,
                right_word_study: two
            }
        }
        timeline.push(study_card)

        // Grab two words to be tested in the right order
        one = test_order2.shift();
        one = wordpool2[one];
        two = test_order2.shift();
        two = wordpool2[two];

        // Grab the comparison type and correct answer side:
        comp = comparison_type_order2.shift();
        side = correct_side_order2.shift();
        ordered_comp = ordered_comparison_order2.shift();
        first_comp = ordered_comp[0]
        second_comp = ordered_comp[1]

        let test_question_card = {
            trial: 2,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px;">' + one + 
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['a', 'l'],
            post_trial_gap: gap,
            data: {trial_type: "test",
                comparison_type: comp,
                left_word_test: one,
                right_word_test: two,
                left_comp_type: first_comp,
                right_comp_type: second_comp,
                correct_side: side
            },
            on_finish: function(data) {
                if (data.key_press == 65){
                    data.chosen_side = 0;
                } else if (data.key_press == 76) {
                    data.chosen_side = 1; 
                } else {
                    data.chosen_side = null;
                }
            }
        };
        timeline.push(test_question_card)
    }

    /****************************************************************************************
     ***************************** Experiment Finished **************************************
    ****************************************************************************************/

    // Call jsPsych function:
    jsPsych.init({
        timeline: timeline,
        on_finish: function() {
            psiturk.saveData({
                success: function() { psiturk.completeHIT(); }
            });
        },
        on_data_update: function(data) {
            psiturk.recordTrialData(data);
            psiturk.saveData();
        },
        exclusions: {
            min_width: 800,
            min_height: 600
          }
    });
}