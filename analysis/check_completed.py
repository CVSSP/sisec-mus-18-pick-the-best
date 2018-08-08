import matplotlib.pyplot as plt
import pandas as pd


frame = pd.read_csv('../results/dataset.csv')

num_pages_completed = frame.groupby('submission_id')['value'].sum()

print('Number of submissions: ', len(pd.unique(frame.submission_id)))

print('Number of submissions with all completed 13 pages: ',
      sum(num_pages_completed == 13))

print('Number of submissions with 0 completed pages :',
      sum(num_pages_completed == 0))

num_pages_completed.hist()
plt.show()
