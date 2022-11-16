import pandas as pd
import matplotlib.pyplot as plt

activity_data_frame = pd.read_csv('data/ACTIVITY.csv', sep=',')

plt.plot(activity_data_frame['date'], activity_data_frame['calories'])