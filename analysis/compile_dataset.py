import pylisten


frame = pylisten.parser.Parser('../results/raw').parse()

frame = frame.drop(columns='subject').dropna()

frame.to_csv('../results/dataset.csv', index=None)
