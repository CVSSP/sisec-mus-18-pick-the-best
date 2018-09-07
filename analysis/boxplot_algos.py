import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.usetex'] = True

def plot(path):

    frame = pd.read_csv('../results/dataset.csv')

    frame['song'] = frame['url'].apply(lambda x: x.split('/')[1])

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

    sns.set_palette("colorblind")

    fig, ax = plt.subplots(figsize=(6, 3))

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

    ax.set_ylim(0, 0.65)

    sns.despine(offset=5, trim=True)

    ax.set_ylabel('Proportion of times selected')
    ax.set_xlabel('Source Separation Algorithm')


    plt.tight_layout(pad=0)
    plt.savefig(path, dpi=300)
    plt.show()


if __name__ == '__main__':

    plot('../results/algo_boxplots.png')
