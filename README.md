# **Project Description**

A project done for my work in the Computational Memory Lab in the summer of 2021. 
Every version _base_ exists in this repository. 
All folders are overly simplistic versions of what is actually released. 
This is because much of the code in the file project was adapted from legacy lab code. 
A lot of smaller edits (like going between version 1.0 and 1.1 were also only worked into the repositories hosted on the server from which the code was deployed. 
Nevertheless, you can see some the code used to create the structure of the experiment (in "experiment_creation" within each version folder), the code used to create the runnable experiment ("JOR.html" or "Psiturk_Compatible") and some of the first analyses I wrote to analyze data that I got (in "analysis" or "test_analysis").

## Experiment Description

A modern-day recreation of the Yntema and Trask's 1963 Judgment of Recency (JOR) experiment using the JsPsych library, run on MTurk and stored on a MySQL table.

Since this experiment is run through the University of Pennsylvania's CML (Computational Memory Lab: http://memory.psych.upenn.edu/Main_Page), the semantics
dealing with MTurk and the formal analysis of the data are saved on the lab's github and server on JupyterLab. There are sample analyses done on test data sets
in this repo, but these do not represent a final product. The experiment design file (experiment_creation/exp_design.py) and the actual experiment that can be 
run (JOR.html) are final products and present in this repo. 

To fully understand why the experiment design is as complex as it is for an experiment that seems simple on the surface level, one can either read through the
comments in the exp_design.py file or read the original paper (this would be much easier).

The original paper can be found here: https://www.sciencedirect.com/science/article/pii/S0022537163800699 and this is specifically a recreation of their experiment II.
