import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import pandas as pd
import matplotlib as mpl

plt.rc('text', usetex=False)
plt.rc('font', family='Times New Roman', size='6')
plt.rcParams['xtick.labelsize'] = 5
plt.rcParams['axes.labelsize'] = 6

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

'''
Add the objective scores
'''

data = data.sort_values(by=['song', 'sound'])
sdr = pd.read_csv('../results/sdr.csv').sort_values(by=['Song', 'Algo'])
ops = pd.read_csv('../results/ops.csv').sort_values(by=['Song', 'Algo'])

data['SDR'] = sdr['SDR'].values
data['OPS'] = ops['OPS'].values

# -> long
data = pd.melt(data,id_vars=['song', 'sound', 'value'],
               value_vars=['SDR', 'OPS'],
               var_name='metric',
               value_name='score')

metric_max = data[
    data.groupby(['song', 'metric'])['score'].transform(max) == data['score']
]

subject_max = data[
    data.groupby(['song'])['value'].transform(max) == data['value']
]


sdr_max_matches = sum(
    metric_max.query("metric == 'SDR'").index.isin(
        subject_max.query("metric == 'SDR'").index
    )
)

ops_max_matches = sum(
    metric_max.query("metric == 'OPS'").index.isin(
        subject_max.query("metric == 'OPS'").index
    )
)

print(f'SDR matches subjsec max in {sdr_max_matches} cases')
print(f'OPS matches subject max in {ops_max_matches} cases')

'''
Run the correlations
'''

corrs = data.groupby(['song', 'metric']).apply(
    lambda g: spearmanr(g['value'], g['score'])[0]
).reset_index(name='rho')

# OPS didn't agree with subjects on this one:
print(data[data.song == 'Tom McKenzie - Directions'])

'''
The plot
'''

fig, ax = plt.subplots(figsize=(3.3, 2.5))

colors = sns.color_palette("PuOr", 10)
plot = sns.stripplot(y='song', x='rho',
                     marker='s',
                     alpha=0.8,
                     color=colors[2],
                     data=corrs.query("metric == 'OPS'"),
                     label='OPS',
                     ax=ax)

plot = sns.stripplot(y='song', x='rho',
                     marker='o',
                     alpha=0.8,
                     color=colors[6],
                     data=corrs.query("metric == 'SDR'"),
                     label='SDR',
                     ax=ax)

handles, labels = ax.get_legend_handles_labels()
handles = [handles[0], handles[-1]]
labels = [labels[0], labels[-1]]
ax.legend(handles, labels, loc='upper left')

songs = [_.replace('_', '\'') for _ in songs]
songs[7] = songs[7].replace('\'', ' & ')
ax.set_ylabel('')
ax.set_xlabel('Spearman correlation')
ax.set_yticklabels(songs)
plt.setp(ax.yaxis.get_majorticklabels(), ha='right')
plt.yticks(rotation=0, fontsize=4)
plt.tight_layout(pad=0.25)
plt.savefig('../results/correlations.pdf')
plt.show()
