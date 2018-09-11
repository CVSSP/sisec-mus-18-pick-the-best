import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

np.random.seed(0)
rcParams['text.usetex'] = True
rcParams['lines.linewidth'] = 0.2

def plot(path):

    frame = pd.read_csv('../results/dataset.csv')

    # limit the anlaysis to only those listeners who did the entire test

    completed_n_songs = frame.groupby(['submission_id'])['value'].sum()

    frame = frame[
        frame.submission_id.isin(
            completed_n_songs[(completed_n_songs >= 13)].index
        )
    ]

    counts = frame.groupby(['sound', 'page'])['value'].sum()
    num_people = frame.groupby(['sound', 'page'])['submission_id'].nunique()

    normalised_counts = (
        (counts / num_people)
        .reset_index(name='normalised_count')
    )

    medians = (
        normalised_counts.groupby('sound')
        .median().reset_index()
        .sort_values(by='normalised_count')
    )

    # The plot

    sns.set_palette("pastel", 13)

    fig, ax = plt.subplots(figsize=(6, 3))

    sns.boxplot(x='sound', y='normalised_count',
                order=medians.sound,
                data=normalised_counts,
                fliersize=0,
                color='white',
                ax=ax)

    plt.setp(ax.artists, edgecolor = 'k', facecolor='w')
    # plt.setp(ax.lines, color='k')

    sns.pointplot(x='sound', y='normalised_count',
                  order=medians.sound,
                  data=normalised_counts,
                  dodge=0.1,
                  hue='page',
                  linestyles='--',
                  ax=ax)

    ax.set_ylim(-0.05, 0.65)
    ax.legend_.remove()
    plt.setp(ax.collections, sizes=[80], alpha=0.8)

    sns.despine(offset=5, trim=True)

    ax.set_ylabel('Proportion of times selected')
    ax.set_xlabel('Source Separation Algorithm')

    plt.tight_layout(pad=0)
    plt.savefig(path, dpi=300)
    plt.show()


if __name__ == '__main__':

    plot('../results/algo_boxplots.png')
