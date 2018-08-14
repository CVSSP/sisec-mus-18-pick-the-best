import pandas as pd
import numpy as np
import os
from tempfile import TemporaryDirectory
import matlab.engine


def peass(reference_files,
          estimated_file,
          path_to_peass_toolbox):

    m = matlab.engine.start_matlab()
    m.eval("addpath(genpath('{}'));".format(path_to_peass_toolbox))

    with TemporaryDirectory() as tmp_dir:
        options = {'destDir': tmp_dir, 'segmentationFactor': 1}
        result = m.PEASS_ObjectiveMeasure(reference_files,
                                          estimated_file,
                                          options)

    return result['OPS']


def main(toolbox_path):

    stimuli_path = '../site/sounds'
    songs = os.listdir(stimuli_path)

    refs = ['ref_vocals.flac',
            'ref_accompaniment.flac',
            ]

    algos = ['JY3', 'STL1', 'TAU1', 'MDL1', 'TAK2', 'UHL3']

    num_songs = 13
    num_algos = len(algos)

    frame = pd.DataFrame(columns=['Song', 'Algo', 'OPS'],
                         index=np.arange(num_songs * num_algos))

    idx = 0
    for song in songs:

        song_path = os.path.join(stimuli_path, song)

        ref_paths = [os.path.join(song_path, _) for _ in refs]

        for algo in algos:

            algo_path = os.path.join(song_path, f'{algo}_vocals.flac')

            ops = peass(ref_paths, algo_path, toolbox_path)

            frame.iloc[idx] = song, algo, ops

            idx += 1

    frame.to_csv('../results/ops.csv', index=None)

main(
    '/home/dominic/git/peass-software'
)
