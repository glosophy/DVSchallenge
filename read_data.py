import pandas as pd
import os

cwd = os.getcwd()

df = pd.read_csv(cwd + '/data_2021_main_dvs-soti_v1.1.csv')

# select columns to analyse
df = df[['HobbyTime', 'HobbyEnjoyment', 'HobbyPortfolio', 'HobbyVolunteer', 'HobbyShareMessages', 'HobbyBuildSkills',
         'TopMethodsDVEduc_Books', 'TopMethodsDVEduc_Workshops', 'TopMethodsDVEduc_Examples', 'TopMethodsDVEduc_VideoTutorials',
         'TopMethodsDVEduc_CollaborateWithMoreSkilled', 'TopMethodsDVEduc_WorkThroughProject',	'TopMethodsDVEduc_MentororTeach',
         'TopMethodsDVEduc_Podcasts', 'TopMethodsDVEduc_InPersonFormats', 'TopMethodsDVEduc_VirtualFormats']]

# see length of df and count NaNs
print('People who took the survey:', len(df))
print('People who did not answer these questions:\n', df.isna().sum())

# clean df slice
df = df[df['HobbyTime'].notna()]

print('Total answers after cleaning:', len(df))

# count each occurence in each column
for i in df.columns:
    print('Occurences in column {}'.format(i))
    print(df[i].value_counts())

df.to_csv('clean_data.csv')