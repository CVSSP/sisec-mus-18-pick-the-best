import pandas as pd
import numpy as np
import mir_eval
from untwist.data import audio
import os

def main():

    stimuli_path = '../site/sounds'

    refs = ['ref_vocals.flac',
            'ref_accompaniment.flac',
    ]

    algos = ['JY3', 'STL1', 'TAU1', 'MDL1', 'TAK2', 'UHL3']

    num_songs = 13
    num_algos = len(algos)

    frame = pd.DataFrame(columns=['Song', 'Algo', 'SDR'],
                         index=np.arange(num_songs * num_algos))

    idx = 0
    for song in os.listdir(stimuli_path):

        song_path = os.path.join(stimuli_path, song)

        ref_paths = [os.path.join(song_path, _) for _ in refs]
        
        ref_audio = np.array([audio.Wave.read(_) for _ in ref_paths])

        for algo in algos:

            algo_path = os.path.join(song_path, f'{algo}_vocals.flac')

            algo_audio = np.array([audio.Wave.read(_) for _ in [algo_path]*2 ])

            out = mir_eval.separation.bss_eval_images(ref_audio,
                                                      algo_audio,
                                                      False)

            sdr = out[0][0]

            frame.iloc[idx] = song, algo, sdr

            idx += 1

    frame.to_csv('../results/sdr.csv', index=None)

main()
