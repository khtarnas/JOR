'''
Import Statements:
'''

# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''
Changing sqlite db into a pandas dataframe
'''

# Set the main variables to the correct values
db_url = 'sqlite+pysqlite:////Users/khtarnas/Documents/JOR1.1/JOR2.1/Psiturk_Compatible/test.db' # Change based on computer being used with
table_name = 'test'
data_column_name = 'datastring'

# boilerplace sqlalchemy setup
engine = create_engine(db_url)
metadata = MetaData()
metadata.bind = engine
table = Table(table_name, metadata, autoload=True)

# make a query and loop through
s = table.select()
rows = s.execute()

data = []

# Status codes of subjects who completed experiment
# NOT_ACCEPTED = 0
# ALLOCATED = 1
# STARTED = 2
# COMPLETED = 3
# SUBMITTED = 4
# CREDITED = 5
# QUITEARLY = 6
# BONUSED = 7
statuses = [0,1,2,3,4,5,6,7]
#conditions = [] #Can be used to look at specifics to do with participant data outside of jspsych
exclude = [] # exclude workers with their worker ids here

for row in rows:
    # only use subjects who fit the selected status codes and aren't excluded
    if row['status'] in statuses and row['uniqueid'] not in exclude:
        # conditions.append({
        #         'uniqueid': row['uniqueid'],
        #         'beginhit': row['beginhit'],
        #         'endhit': row['endhit'],
        #         'status': row['status'],
        #         'counterbalance': row['counterbalance'],
        #         'workerid': row['workerid']
        #     })
        data.append(row[data_column_name])

#condition_frame = pd.DataFrame(conditions)
#print(condition_frame.sort_values('beginhit')) #print the gathered information about test participants

# Now we have all participant datastrings in a list.
# To make it a bit easier to work with:
# parse each participant's datastring as json object and take the 'data' sub-object
subject_data = []
for subject_json in data:
    try:
        subject_dict = json.loads(subject_json)
        subject_data.append(subject_dict['data'])
    except:
        continue

# Insert uniqueid field into trialdata in case it wasn't added in experiment:
for part in subject_data:
    for record in part:
        record['trialdata']['uniqueid'] = record['uniqueid']

# Flatten nested list so we just have a list of the trialdata recorded each time psiturk.recordTrialData(trialdata) was called.
trialdata = []
for part in subject_data:
    for record in part:
        trialdata.append(record['trialdata'])

# Put all subjects' trial data into a dataframe object from the
# 'pandas' python library: one option among many for analysis
df = pd.DataFrame(trialdata)
# print(df)
#print(df.columns)
