import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_palette("colorblind")

frame = pd.read_csv('../results/dataset.csv')

counts = frame.groupby(['sound', 'page'])['value'].sum()
num_people = frame.groupby(['sound', 'page'])['submission_id'].nunique()

normalised_counts = (counts / num_people).reset_index(name='normalised_count')

medians = (
    normalised_counts.groupby('sound')
    .median().reset_index()
    .sort_values(by='normalised_count')
)

fig, ax = plt.subplots(figsize=(6, 4))

sns.boxplot(x='sound', y='normalised_count',
           order=medians.sound,
           data=normalised_counts,
           fliersize=0,
           ax=ax)

sns.swarmplot(x='sound', y='normalised_count',
             order=medians.sound,
             data=normalised_counts,
             color='0.3',
             size=8,
             ax=ax)

sns.despine(offset=5, trim=True)

ax.set_ylabel('Normalised count')
ax.set_xlabel('Algorithm')

plt.tight_layout()
plt.savefig('../results/algo_boxplots.pdf')
plt.show()
