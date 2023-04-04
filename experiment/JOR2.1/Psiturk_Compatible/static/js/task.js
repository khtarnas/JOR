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

// the following two variables are passed by the psiturk server
// they tell you which condition you have been assigned to
let mycondition = condition;
let mycounterbalance = counterbalance; // we are only using this
//console.log(mycounterbalance);

// If we don't have a counterbalance from psiTurk (testing only)
let testing = false;
if (testing) {
    mycounterbalance = Math.floor(Math.random() * 100);
}

// This is the function that will be called from JOR/templates/exp.html
let run_exp = function() {

    // shuffle the input wordpool
    wordpool = jsPsych.randomization.repeat(wordpool, 1);
    max_counterbalance = 100

    // Trial 1 Variables
    wordpool1 = wordpool.slice(0, 88);
    study_order1 = all_study_orders[mycounterbalance]
    test_order1 = all_test_orders[mycounterbalance]
    correct_side_order1 = all_correct_sides[mycounterbalance]
    comparison_type_order1 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order1 = all_ordered_comparison_orders[mycounterbalance]
    //console.log("mycounterbalance = " + mycounterbalance);
    //console.log("wordpool1 = " + wordpool1);

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

    // Trial 2 Variables
    wordpool2 = wordpool.slice(88, 176);
    study_order2 = all_study_orders[mycounterbalance]
    test_order2 = all_test_orders[mycounterbalance]
    correct_side_order2 = all_correct_sides[mycounterbalance]
    comparison_type_order2 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order2 = all_ordered_comparison_orders[mycounterbalance]

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

    // Trial 3 Variables
    wordpool3 = wordpool.slice(176, 264);
    study_order3 = all_study_orders[mycounterbalance]
    test_order3 = all_test_orders[mycounterbalance]
    correct_side_order3 = all_correct_sides[mycounterbalance]
    comparison_type_order3 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order3 = all_ordered_comparison_orders[mycounterbalance]

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

    // Trial 4 Variables
    wordpool4 = wordpool.slice(264, 352);
    study_order4 = all_study_orders[mycounterbalance]
    test_order4 = all_test_orders[mycounterbalance]
    correct_side_order4 = all_correct_sides[mycounterbalance]
    comparison_type_order4 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order4 = all_ordered_comparison_orders[mycounterbalance]

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

    // Trial 5 Variables
    wordpool5 = wordpool.slice(352, 440);
    study_order5 = all_study_orders[mycounterbalance]
    test_order5 = all_test_orders[mycounterbalance]
    correct_side_order5 = all_correct_sides[mycounterbalance]
    comparison_type_order5 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order5 = all_ordered_comparison_orders[mycounterbalance]

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

    // Trial 6 Variables
    wordpool6 = wordpool.slice(440, 528);
    study_order6 = all_study_orders[mycounterbalance]
    test_order6 = all_test_orders[mycounterbalance]
    correct_side_order6 = all_correct_sides[mycounterbalance]
    comparison_type_order6 = all_comparison_type_orders[mycounterbalance]
    ordered_comparison_order6 = all_ordered_comparison_orders[mycounterbalance]

    mycounterbalance++;
    if (mycounterbalance >= max_counterbalance) {
      mycounterbalance = 0;
    }

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
        stimulus: "Welcome to the <strong>Judgment of Recency</strong> experiment! <p>Press the <strong>Space Bar</strong> for a brief survey before the instructions.</p>",
        choices: [' '],
        on_finish: function(data) {psiturk.finishInstructions();}
    };

    // Instructions event
    let instructions = {
        type: "html-keyboard-response",
        stimulus: "<p>In this experiment, you will encounter a number of study and test trials." +
        "<p>The study trials will present two words on the screen, one above the other. Take note of these words; you will" +
        " be asked to judge how recently you have seen them. Each study trial will last for " + length + "." +
        " Please do NOT write down the words that you study.</p>" +

        "<p>The test trials will also show you two words, but they will be side by side with a red question mark between the words to show" +
        " that it is a test trial. When you encounter a test trial, indicate which of the two words shown have been" +
        " seen on a study trial most recently. Sometimes one of the words on a test trial will not have been presented in the task before." +
        " In this case, you should always choose the one you've previously seen in the task." +
        " You will indicate which word occurred most recently with the" +
        " <strong>‘z’ key</strong> for the word on the left side and the <strong>‘.’ key</strong> (i.e. the period key) for the word on the right side." +
        " Take a moment to find these on your keyboard now.</p>" +

        "<p>Each word will be seen at most twice: once during a study trial and once during a test trial.</p>" +

        "<p>There will be two blocks (each around 10 - 15 minutes long) with a break in between." +
        " There will be no overlapping words between the two blocks.</p>" +

        "<p>Before the first block begins, there will be a short practice block to ensure that the instructions are clear." +

        "<p>Press the <strong>Space Bar</strong> to continue to the practice block.</p>",
        choices: [' '],
        post_trial_gap: 200,

    };

      /****************************************************************************************
       **************************** Practice Block Begins *************************************
      ****************************************************************************************/

      // Block 0 Label Warning
          let block_zero = {
              type: "html-keyboard-response",
              stimulus: "<p>The Practice Block will begin in 5 seconds.</p>",
              choices: jsPsych.NO_KEYS,
              trial_duration: 5000,
              post_trial_gap: gap
          };

          // Practice Block Words:

          let prac_word_0 = wordpool[522];
          let prac_word_1 = wordpool[523];
          let prac_word_2 = wordpool[524];
          let prac_word_3 = wordpool[525];
          let prac_word_4 = wordpool[526];
          let prac_word_5 = wordpool[527];
          let prac_word_6 = wordpool[528];
          let prac_word_7 = wordpool[529];
          let prac_word_8 = wordpool[530];
          let prac_word_9 = wordpool[531];
          let prac_word_10 = wordpool[532];

          // Hard-coded Practice Trials:

          /*
          * Forced Choice Demonstration
          */

          let prac_study_0 = {
              trial: 0, //could result in a problem using 0?
              type: 'html-keyboard-response',
              stimulus: '<h1 style="font-size: 35px">' + prac_word_0 + '</h1>' +
              '<h1 style="font-size: 35px; margin-top: 45px;">' + prac_word_1 + '</h1>',
              choices: jsPsych.NO_KEYS,
              trial_duration: time,
              post_trial_gap: gap,
              data: {block_number: 0,
                  left_word_study: prac_word_0,
                  right_word_study: prac_word_1
              }
          }

          let prac_study_1 = {
              trial: 0,
              type: 'html-keyboard-response',
              stimulus: '<h1 style="font-size: 35px">' + prac_word_2 + '</h1>' +
              '<h1 style="font-size: 35px; margin-top: 45px;">' + prac_word_3 + '</h1>',
              choices: jsPsych.NO_KEYS,
              trial_duration: time,
              post_trial_gap: gap,
              data: {block_number: 0,
                  left_word_study: prac_word_2,
                  right_word_study: prac_word_3
              }
          }

          let prac_test_0 = {
              trial: 0,
              type: 'html-keyboard-response',
              prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>" +
              "<p>The correct decision here is the left word before it was seen more recently. Press the 'z' key to indicate this.</p>",
              stimulus: '<h1 style="font-size: 35px;">' + prac_word_2 +
              '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
              prac_word_1 + '</h1>',
              choices: ['z', 'Z'],
              post_trial_gap: gap,
              data: {block_number: 0,
                  trial_period: "practice",
                  left_word_test: prac_word_1,
                  right_word_test: prac_word_2,
              },
              on_finish: function(data) {
                  if (data.key_press == 'z' || data.key_press == 'Z'){
                      data.chosen_side = 0;
                  } else if (data.key_press == '.') {
                      data.chosen_side = 1;
                  }
              }
          };

          /*
          * Practice making correct judgment
          */

          let prac_study_2 = {
              trial: 0, //could result in a problem using 0?
              type: 'html-keyboard-response',
              stimulus: '<h1 style="font-size: 35px">' + prac_word_4 + '</h1>' +
              '<h1 style="font-size: 35px; margin-top: 45px;">' + prac_word_5 + '</h1>',
              choices: jsPsych.NO_KEYS,
              trial_duration: time,
              post_trial_gap: gap,
              data: {block_number: 0,
                  left_word_study: prac_word_4,
                  right_word_study: prac_word_5
              }
          }

          let prac_study_3 = {
              trial: 0,
              type: 'html-keyboard-response',
              stimulus: '<h1 style="font-size: 35px">' + prac_word_6 + '</h1>' +
              '<h1 style="font-size: 35px; margin-top: 45px;">' + prac_word_7 + '</h1>',
              choices: jsPsych.NO_KEYS,
              trial_duration: time,
              post_trial_gap: gap,
              data: {block_number: 0,
                  left_word_study: prac_word_6,
                  right_word_study: prac_word_7
              }
          }

          let prac_test_1 = {
              trial: 0,
              type: 'html-keyboard-response',
              prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
              stimulus: '<h1 style="font-size: 35px;">' + prac_word_5 +
              '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
              prac_word_6 + '</h1>',
              choices: ['z', 'Z', '.'],
              post_trial_gap: gap,
              data: {block_number: 0,
                  trial_period: "practice",
                  left_word_test: prac_word_5,
                  right_word_test: prac_word_6,
              },
              on_finish: function(data) {
                  if (data.key_press == 'z' || data.key_press == 'Z'){
                      data.chosen_side = 0;
                  } else if (data.key_press == '.') {
                      data.chosen_side = 1;
                  }
              }
          };

          // Failure screen
          let failure = {
            type: "html-keyboard-response",
            stimulus: "<p>You have failed the experiment.</p>" +
            "<p>Because you were unable to learn the rules of experiment," +
            " you will be unable to continue." +
            "<p>If you feel like this is an error, please email us at kahanalab@gmail.com</p>",
            choices: [],
          }

          // Conditional Failure due to too many tries at practice block:
          let conditional_failure_0 = {
            timeline: [failure],
            conditional_function: function() {
              let data = jsPsych.data.get().values();
              // Check whether the last trial was wrong and it's been at least one wrong answer to each before this (the length check)
              if (data[data.length - 1].key_press == 'z' || data[data.length - 1].key_press == 'Z') {
                if (data.length >= 18) {
                  return true;
                } else {
                  return false;
                }
              } else {
                return false;
              }
            }
          }

          let after_conditional_0 = {
            type: 'html-keyboard-response',
            stimulus: '<p>That is the wrong answer.</p>' +
              '<p> You should try to select the word that you have seen MORE recently. </p>' +
              '<p> Please repeat the previous study and test trials by pressing any button.' +
              "<p> If you would like to re-read the instructions, press the <strong>Space Button</strong>."
          };

          let conditional_loop_0 = {
            timeline: [after_conditional_0],
            conditional_function: function() {
              let data = jsPsych.data.get().last(1).values()[0];
              if(data.key_press == 'z' || data.key_press == 'Z'){
                  return true;
              } else if(data.key_press == '.'){
                  return false;
              }
            },
          };

          let optional_instructions = {
            type: "html-keyboard-response",
            stimulus: "<p>In this experiment, you will encounter a number of study and test trials." +
                    "<p>The study trials will present two words on the screen, one above the other. Take note of these words; you will" +
                    " be asked to judge how recently you have seen them. Each study trial will last for " + length + "." +
                    " Please do NOT write down the words that you study.</p>" +

                    "<p>The test trials will also show you two words, but they will be side by side with a red question mark between the words to show" +
                    " that it is a test trial. When you encounter a test trial, indicate which of the two words shown have been" +
                    " seen on a study trial most recently. Sometimes one of the words on a test trial will not have been presented in the task before." +
                    " In this case, you should always choose the one you've previously seen in the task." +
                    " You will indicate which word occurred most recently with the" +
                    " <strong>‘z’ key</strong> for the word on the left side and the <strong>‘.’ key</strong> (i.e. the period key) for the word on the right side." +
                    " Take a moment to find these on your keyboard now.</p>" +

                    "<p>Each word will be seen at most twice: once during a study trial and once during a test trial.</p>" +

                    "<p>Recall that there will be two blocks (each around 15 - 20 minutes long) with a break in between" +
                    " and that there will be no overlapping words between the two blocks.</p>" +

                    "<p>After completing this short practice block, the experiment will move on to Block 1." +

                    "<p>Press the <strong>Space Bar</strong> to retry the practice block.</p>",
            choices: [' '],
            post_trial_gap: 200
          };

          let conditional_loop_1 = {
            timeline: [optional_instructions],
            conditional_function: function() {
              let data = jsPsych.data.get().last(1).values()[0];
              if(data.key_press == ' '){
                  return true;
              } else {
                  return false;
              }
            }
          };

          let loop_node_0 = {
            timeline: [block_zero, prac_study_0, prac_study_1, prac_test_0, prac_study_2, prac_study_3, prac_test_1, conditional_failure_0, conditional_loop_0, conditional_loop_1],
            loop_function: function(data){
              if(data.values()[6].key_press == 'z' || data.values()[6].key_press == 'Z'){
                  return true;
              } else if(data.values()[6].key_press == '.'){
                  return false;
              }
            }
          };

          /*
          * Practice making correct decision when facing a "many" word
          */

          let prac_study_4 = {
              trial: 0,
              type: 'html-keyboard-response',
              stimulus: '<h1 style="font-size: 35px">' + prac_word_8 + '</h1>' +
              '<h1 style="font-size: 35px; margin-top: 45px;">' + prac_word_9 + '</h1>',
              choices: jsPsych.NO_KEYS,
              trial_duration: time,
              post_trial_gap: gap,
              data: {block_number: 0,
                  left_word_study: prac_word_8,
                  right_word_study: prac_word_9
              }
          }

          let prac_test_2 = {
              trial: 0,
              type: 'html-keyboard-response',
              prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
              stimulus: '<h1 style="font-size: 35px;">' + prac_word_9 +
              '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
              prac_word_10 + '</h1>',
              choices: ['z', 'Z', '.'],
              post_trial_gap: gap,
              data: {block_number: 0,
                  trial_period: "practice",
                  left_word_test: prac_word_9,
                  right_word_test: prac_word_10,
              },
              on_finish: function(data) {
                  if (data.key_press == 'z' || data.key_press == 'Z'){
                      data.chosen_side = 0;
                  } else if (data.key_press == '.') {
                      data.chosen_side = 1;
                  }
              }
          };

          let after_conditional_1 = {
            type: 'html-keyboard-response',
            stimulus: '<p>That is the wrong answer.</p>' +
              '<p> One of the words on the last test trial had not previously been seen on a study trial meaning that you should NOT select it. </p>' +
              '<p> Please repeat the previous study and test trials by pressing any button.' +
              "<p> If you would like to re-read the instructions, press the <strong>Space Button</strong>."
          };

          // Conditional Failure due to too many tries at practice block:
          let conditional_failure_1 = {
            timeline: [failure],
            conditional_function: function() {
              let data = jsPsych.data.get().values();

              // Check whether the last trial was wrong and it's been at least one wrong answer to each before this (the length check)
              if (data[data.length - 1].key_press == '.') {
                if (data.length >= 24) {
                  return true;
                } else {
                  return false;
                }
              } else {
                return false;
              }
            }
          }

          let conditional_loop_2 = {
            timeline: [after_conditional_1],
            conditional_function: function() {
              let data = jsPsych.data.get().last(1).values()[0];
              if(data.key_press == 'z' || data.key_press == 'Z'){
                  return false;
              } else if(data.key_press == '.'){
                  return true;
              }
            }
          };

          let conditional_loop_3 = {
            timeline: [optional_instructions],
            conditional_function: function() {
              let data = jsPsych.data.get().last(1).values()[0];
              if(data.key_press == ' '){
                  return true;
              } else {
                  return false;
              }
            }
          };

          let loop_node_1 = {
            timeline: [loop_node_0, prac_study_4, prac_test_2, conditional_failure_1, conditional_loop_2, conditional_loop_3],
            loop_function: function(data){
              if(data.values()[data.values().length - 2].key_press == '.') {
                return true;
              } else if (data.values()[data.values().length - 1].key_press == 'z' || data.values()[data.values().length - 1].key_press == 'Z') {
                return false;
              } else {
                return true;
              }
            }
          };

          // Warning event
          let warning = {
              type: "html-keyboard-response",
              stimulus: "<p>Block 1 will last approximately 10 - 15 minutes." +
                      "<p>Please make sure you will not need to leave during that duration before starting.<p>" +
                      "<p>To begin <Strong>Block 1</Strong>, press the Space Bar.</p>",
              choices: [' '],
              post_trial_gap: 200
          };

          // Create a timeline and add events:
          let timeline = [];
          timeline.push(enter_name);
          timeline.push(welcome);
          timeline.push(jsPsychUtils.get_attention_check());
          timeline.push(instructions);
          timeline.push(loop_node_1);
          timeline.push(warning);

    /****************************************************************************************
     ****************************** Block 1 Begins ******************************************
    ****************************************************************************************/

    // Block 1 Label Warning
    let block_one = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 1 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(block_one);

    //First 6 are study cards, then rest alternate
    for (let i = 0; i < 10; i++) {

        console.log(wordpool1);
        // Grab two words to be studied in the right order
        let one = study_order1.shift();
        console.log(one);
        one = wordpool1[one];
        console.log(one);
        let two = study_order1.shift();
        two = wordpool1[two];

        // Create a study event and add it to the timeline
        let study_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {block_number: 1,
                left_word_study: one,
                right_word_study: two,
                trial_period: "study"
            }
        }
        timeline.push(study_trial);
    }

    // Test Period: alternate study and test for the final 75 trials:
    for (let i = 0; i < 34; i++) {

      // Grab two words to be studied in the right order
      let one = study_order1.shift();
      one = wordpool1[one];
      let two = study_order1.shift();
      two = wordpool1[two];

      // Create a study event and add it to the timeline
      let study_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
          '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
          choices: jsPsych.NO_KEYS,
          trial_duration: time,
          post_trial_gap: gap,
          data: {block_number: 1,
              trial_period: "study",
              left_word_study: one,
              right_word_study: two
          }
      };
      timeline.push(study_trial);

      // Grab two words to be tested in the right order
      one = test_order1.shift();
      one = wordpool1[one];
      two = test_order1.shift();
      two = wordpool1[two];

      // Grab the comparison type and correct answer side:
      comp = comparison_type_order1.shift();
      side = correct_side_order1.shift();
      ordered_comp = ordered_comparison_order1.shift();
      first_comp = ordered_comp[0]
      second_comp = ordered_comp[1]

      let test_question_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
          stimulus: '<h1 style="font-size: 35px;">' + one +
          '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
          two + '</h1>',
          choices: ['z', 'Z', '.'],
          post_trial_gap: gap,
          data: {block_number: 1,
              trial_period: "test",
              comparison_type: comp,
              left_word_test: one,
              right_word_test: two,
              left_comp_type: first_comp,
              right_comp_type: second_comp,
              correct_side: side
          },
          on_finish: function(data) {
              if (data.key_press == 'z' || data.key_press == 'Z'){
                  data.chosen_side = 0;
              } else if (data.key_press == '.') {
                  data.chosen_side = 1;
              }
          }
      };
      timeline.push(test_question_trial)

    }

    /****************************************************************************************
     ****************************** Block 2 Begins ******************************************
    ****************************************************************************************/

    // Warning event
    let warning_two = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 2 will last approximately 10 - 15 minutes." +
                "<p>Please make sure you will not need to leave during that duration before starting.<p>" +
                "<p>To begin <Strong>Block 2</Strong>, press the Space Bar.</p>",
        choices: [' '],
        post_trial_gap: 200
    };
    timeline.push(warning_two);

    // Block 2 Label Warning
    let block_two = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 2 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(block_two);

    //First 6 are study cards, then rest alternate
    for (let i = 0; i < 10; i++) {

        // Grab two words to be studied in the right order
        let one = study_order2.shift();
        one = wordpool2[one];
        let two = study_order2.shift();
        two = wordpool2[two];

        // Create a study event and add it to the timeline
        let study_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {block_number: 2,
                left_word_study: one,
                right_word_study: two,
                trial_period: "study"
            }
        };
        timeline.push(study_trial);
    }

    // Test Period: alternate study and test for the final 75 trials:
    for (let i = 0; i < 34; i++) {

      // Grab two words to be studied in the right order
      let one = study_order2.shift();
      one = wordpool2[one];
      let two = study_order2.shift();
      two = wordpool2[two];

      // Create a study event and add it to the timeline
      let study_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
          '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
          choices: jsPsych.NO_KEYS,
          trial_duration: time,
          post_trial_gap: gap,
          data: {block_number: 2,
              trial_period: "study",
              left_word_study: one,
              right_word_study: two
          }
      };
      timeline.push(study_trial);

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

      let test_question_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
          stimulus: '<h1 style="font-size: 35px;">' + one +
          '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
          two + '</h1>',
          choices: ['z', 'Z', '.'],
          post_trial_gap: gap,
          data: {block_number: 2,
              trial_period: "test",
              comparison_type: comp,
              left_word_test: one,
              right_word_test: two,
              left_comp_type: first_comp,
              right_comp_type: second_comp,
              correct_side: side
          },
          on_finish: function(data) {
              if (data.key_press == 'z' || data.key_press == 'Z'){
                  data.chosen_side = 0;
              } else if (data.key_press == '.') {
                  data.chosen_side = 1;
              }
          }
      };
      timeline.push(test_question_trial)

    }

    /****************************************************************************************
     ****************************** Block 3 Begins ******************************************
    ****************************************************************************************/
    /**
    // Warning event
    let warning_three = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 3 will last approximately 10 - 15 minutes." +
                "<p>Please make sure you will not need to leave during that duration before starting.<p>" +
                "<p>To begin <Strong>Block 3</Strong>, press the Space Bar.</p>",
        choices: [' '],
        post_trial_gap: 200
    };
    timeline.push(warning_three);

    // Block 3 Label Warning
    let block_three = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 3 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(block_three);

    //First 6 are study cards, then rest alternate
    for (let i = 0; i < 10; i++) {

        // Grab two words to be studied in the right order
        let one = study_order3.shift();
        one = wordpool3[one];
        let two = study_order3.shift();
        two = wordpool3[two];

        // Create a study event and add it to the timeline
        let study_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {block_number: 3,
                left_word_study: one,
                right_word_study: two,
                trial_period: "study"
            }
        };
        timeline.push(study_trial);
    }

    // Test Period: alternate study and test for the final 75 trials:
    for (let i = 0; i < 34; i++) {

      // Grab two words to be studied in the right order
        let one = study_order3.shift();
        one = wordpool3[one];
        let two = study_order3.shift();
        two = wordpool3[two];

        // Create a study event and add it to the timeline
        let study_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {block_number: 3,
                trial_period: "study",
                left_word_study: one,
                right_word_study: two
            }
        };
        timeline.push(study_trial);

        // Grab two words to be tested in the right order
        one = test_order3.shift();
        one = wordpool3[one];
        two = test_order3.shift();
        two = wordpool3[two];

        // Grab the comparison type and correct answer side:
        comp = comparison_type_order3.shift();
        side = correct_side_order3.shift();
        ordered_comp = ordered_comparison_order3.shift();
        first_comp = ordered_comp[0]
        second_comp = ordered_comp[1]

        let test_question_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
            stimulus: '<h1 style="font-size: 35px;">' + one +
            '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
            two + '</h1>',
            choices: ['z', 'Z', '.'],
            post_trial_gap: gap,
            data: {block_number: 3,
                trial_period: "test",
                comparison_type: comp,
                left_word_test: one,
                right_word_test: two,
                left_comp_type: first_comp,
                right_comp_type: second_comp,
                correct_side: side
            },
            on_finish: function(data) {
                if (data.key_press == 'z' || data.key_press == 'Z'){
                    data.chosen_side = 0;
                } else if (data.key_press == '.') {
                    data.chosen_side = 1;
                }
            }
        };
        timeline.push(test_question_trial);

    }
    **/
    /****************************************************************************************
     ****************************** Block 4 Begins ******************************************
    ****************************************************************************************/
    /**

    // Warning event
    let warning_four = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 4 will last approximately 10 - 15 minutes." +
                "<p>Please make sure you will not need to leave during that duration before starting.<p>" +
                "<p>To begin <Strong>Block 4</Strong>, press the Space Bar.</p>",
        choices: [' '],
        post_trial_gap: 200
    };
    timeline.push(warning_four);

    // Block 4 Label Warning
    let block_four = {
        type: "html-keyboard-response",
        stimulus: "<p>Block 4 will begin in 5 seconds.</p>",
        choices: jsPsych.NO_KEYS,
        trial_duration: 5000,
        post_trial_gap: gap
    };
    timeline.push(block_four);

    //First 11 are study cards, then rest alternate
    for (let i = 0; i < 10; i++) {

        // Grab two words to be studied in the right order
        let one = study_order4.shift();
        one = wordpool4[one];
        let two = study_order4.shift();
        two = wordpool4[two];

        // Create a study event and add it to the timeline
        let study_trial = {
            trial: 1,
            type: 'html-keyboard-response',
            stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
            '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
            choices: jsPsych.NO_KEYS,
            trial_duration: time,
            post_trial_gap: gap,
            data: {block_number: 4,
                left_word_study: one,
                right_word_study: two,
                trial_period: "study"
            }
        };
        timeline.push(study_trial);
    }

    // Test Period: alternate study and test for the final 34 trials:
    for (let i = 0; i < 34; i++) {

      // Grab two words to be studied in the right order
      let one = study_order4.shift();
      one = wordpool4[one];
      let two = study_order4.shift();
      two = wordpool4[two];

      // Create a study event and add it to the timeline
      let study_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          stimulus: '<h1 style="font-size: 35px">' + one + '</h1>' +
          '<h1 style="font-size: 35px; margin-top: 45px;">' + two + '</h1>',
          choices: jsPsych.NO_KEYS,
          trial_duration: time,
          post_trial_gap: gap,
          data: {block_number: 4,
              trial_period: "study",
              left_word_study: one,
              right_word_study: two
          }
      };
      timeline.push(study_trial);

      // Grab two words to be tested in the right order
      one = test_order4.shift();
      one = wordpool4[one];
      two = test_order4.shift();
      two = wordpool4[two];

      // Grab the comparison type and correct answer side:
      comp = comparison_type_order4.shift();
      side = correct_side_order4.shift();
      ordered_comp = ordered_comparison_order4.shift();
      first_comp = ordered_comp[0]
      second_comp = ordered_comp[1]

      let test_question_trial = {
          trial: 1,
          type: 'html-keyboard-response',
          prompt: "<p>Select the left item using the 'z' key or the right item using the '.' key.</p>",
          stimulus: '<h1 style="font-size: 35px;">' + one +
          '<span style="color: #ff0000; padding-left: 50px; padding-right: 50px;"> ? </span>' +
          two + '</h1>',
          choices: ['z', 'Z', '.'],
          post_trial_gap: gap,
          data: {block_number: 4,
              trial_period: "test",
              comparison_type: comp,
              left_word_test: one,
              right_word_test: two,
              left_comp_type: first_comp,
              right_comp_type: second_comp,
              correct_side: side
          },
          on_finish: function(data) {
              if (data.key_press == 'z' || data.key_press == 'Z'){
                  data.chosen_side = 0;
              } else if (data.key_press == '.') {
                  data.chosen_side = 1;
              }
          }
      };
      timeline.push(test_question_trial);

    }
    **/
    /****************************************************************************************
     ******************************* Final Questions ****************************************
    ****************************************************************************************/

    let did_you_write = {
          type: 'html-button-response',
          stimulus: "<p>Congratulations on finishing the experiment!</p>" +
          "<p>There is one final question before this HIT ends: Did you write down the words you studied to more easily answer the test trials? </p>"
          + "<p>Note that your HIT will be accepted and you will be paid no matter what choice you choose.",
          choices: ['yes', 'no'],
          data: {block_number: 3,
          },
          on_finish: function(data) {
              if (data.button_pressed == '0') {
                  data.subj_wrote_words = 'yes';
              } else if (data.button_pressed = '1')  {
                  data.subj_wrote_words = 'no';
              }
          }
        };
        timeline.push(did_you_write);

    // let ending_block = {
    //     type: 'instructions',
    //     pages: ['You have now completed the study. Thank you for participating! ' +
    //     'You will need to copy down your unique ID to give to your TA. Your ID is ' + uniqueId + ' . ' +
    //     'Once you have copied it, press the right arrow key to submit your data and complete the task!']
    //   };

    //timeline.push(ending_block);

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

run_exp();
