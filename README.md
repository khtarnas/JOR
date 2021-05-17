# Recreating_JOR
A modern-day recreation of the Yntema and Trask's 1963 Judgment of Recency (JOR) experiment using the JsPsych library, run on MTurk and stored on a MySQL table.

Since this experiment is run through the University of Pennsylvania's CML (Computational Memory Lab: http://memory.psych.upenn.edu/Main_Page), the semantics
dealing with MTurk and the formal analysis of the data are saved on the lab's github and server on JupyterLab. There are sample analyses done on test data sets
in this repo, but these do not represent a final product. The experiment design file (experiment_creation/exp_design.py) and the actual experiment that can be 
run (JOR.html) are final products and present in this repo. 

To fully understand why the experiment design is as complex as it is for an experiment that seems simple on the surface level, one can either read through the
comments in the exp_design.py file or read the following:

TODO

The original paper can be found here: https://www.sciencedirect.com/science/article/pii/S0022537163800699 and this is specificall a recreation of their experiment II.
