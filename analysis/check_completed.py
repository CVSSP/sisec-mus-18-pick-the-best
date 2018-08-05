import matplotlib.pyplot as plt
import pandas as pd


frame = pd.read_csv('../results/dataset.csv')

num_pages_completed = frame.groupby('submission_id')['value'].sum()

print(sum(num_pages_completed == 13))

num_pages_completed.hist()
plt.show()
