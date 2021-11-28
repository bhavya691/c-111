import plotly.figure_factory as ff
import pandas as pd
import statistics
import plotly.graph_objects as go
import random
df = pd.read_csv('data.csv')
data = df['Math_score'].tolist()
mean_1 = statistics.mean(data)
stdev_1 = statistics.stdev(data)
mean_list = []
for i in range(0,1000):
    dataset = []
    for j in range(0,100):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean_of_dataset = statistics.mean(dataset)
    mean_list.append(mean_of_dataset)

# print(mean_list)
mean = statistics.mean(mean_list)
stdev = statistics.stdev(mean_list)
# print(mean_list)
print('Mean of raw data: \t', mean_1)
print('Stdev of raw data: \t', stdev_1)
print('Mean of mean_list: \t', mean)
print('Stdev of mean_list: \t', stdev)

stdev_1_start, stdev_1_end = mean - stdev, mean + stdev
stdev_2_start, stdev_2_end = mean - 2*stdev, mean + 2*stdev
stdev_3_start, stdev_3_end = mean - 3*stdev, mean + 3*stdev

df1 = pd.read_csv('data1.csv')
data1 = df1['Math_score'].tolist()
mean1 = statistics.mean(data1)
print('Mean of intervention 1: \t', mean1)

df2 = pd.read_csv('data2.csv')
data2 = df2['Math_score'].tolist()
mean2 = statistics.mean(data2)

df3 = pd.read_csv('data3.csv')
data3 = df3['Math_score'].tolist()
mean3 = statistics.mean(data3)

df3 = pd.read_csv('data3.csv')

fig = ff.create_distplot([mean_list], ['Sampling Distribution'], show_hist=False)
fig.add_trace(go.Scatter(x=[stdev_1_end, stdev_1_end], y=[0,0.2], mode='lines', name='stdev_1_end'))
fig.add_trace(go.Scatter(x=[stdev_2_end, stdev_2_end], y=[0,0.2], mode='lines', name = 'stdev_2_end'))
fig.add_trace(go.Scatter(x=[stdev_3_end, stdev_3_end], y=[0,0.2], mode='lines', name = 'stdev_3_end'))
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.2], mode='lines', name='mean'))
fig.add_trace(go.Scatter(x=[mean3, mean3], y=[0,0.2], mode='lines', name='Mean of intervention 1'))
fig.show()


z = (mean - mean1) / stdev
print(z)
z2 = (mean - mean2) / stdev
print(z2)
z3 = (mean - mean3) / stdev
print(z3)