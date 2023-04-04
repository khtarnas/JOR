This is a repository containing the code used to create version 2.0 of the Judgement of Recenecy experiment run on MTurk* for the purposes of data collection in the CML (Computational  Memory Lab) at the University of Pennsylvania.

The directory "experiment_creation" contains the code used to create the complicated design of the experiment and output a js file that can be used to communicate the order to the main experiment file that can be found at Psiturk_Compatible/static/js/task.js which is called from psiturk_compatible/templates/exp.html

The directory "psiturk_compatible" contains all the code necessary to run the experiment on a locally hosted psiturk server. In order to run the experiment on MTurk you would need a MTurk account and a server in order to receive the data on.

The directory "test_analysis" contains the files used to test the data gathered in this locally runnable JOR2.0 version. This analysis is done in order to ensure the correct functionality of this code so that it can be run on MTurk once perfected.

More information is available on both of these directories within the directories themselves.

Tip: In order to run the psiturk server and experiment with greater ease and without more knowledge about how to use psiturk, find the CML_helpful_programs repo on this same user account and download the Run_Live_Setup.zip file and follow the instructions given there.

*MTurk is Amazon's crowdsourcing website where many businesses (or even psychology labs such as CML) can pay MTurk users to complete tasks such as this experiment.
