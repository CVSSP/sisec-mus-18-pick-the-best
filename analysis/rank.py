import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import pandas as pd
import matplotlib as mpl

'''
plt.rc('text', usetex=False)
plt.rc('font', family='Times New Roman', size='6')
plt.rcParams['xtick.labelsize'] = 5
plt.rcParams['axes.labelsize'] = 6
'''

frame = pd.read_csv('../results/dataset.csv')

# Parse the artist and song from the url
frame['song'] = frame['url'].apply(lambda x: x.split('/')[1])

# limit the anlaysis to only those listeners who did the entire test
songs = pd.unique(frame['song'].sort_values())

num_songs = len(songs)

completed_n_songs = frame.groupby(['submission_id'])['value'].sum()

frame = frame[
    frame.submission_id.isin(
        completed_n_songs[(completed_n_songs >= 13)].index
    )
]

# number of times each sound was picked for a given song
data = frame.groupby(['song', 'sound'])['value'].sum().reset_index()

maxes = data.groupby('song')['value'].transform(max) == data['value']

print(data[maxes])

maxes = data.groupby('sound')['value'].max().sort_values()
means = data.groupby('sound')['value'].mean().sort_values()

print(means)
