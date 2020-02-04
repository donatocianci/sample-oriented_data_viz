import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from scipy.stats import norm

'''
This script implements a data visualization scheme proposed by Ferreira, Fisher
and König in the article "Sample-Oriented Task-Driven Visualizations: Allowing
Users to Make Better, More Confident Decisions," which is designed to help data
analysts make decisions with uncertain data.

For example, suppose that an analyst has statistical data from various years, but
perhaps the statistics were drawn from a sample instead of the entire data set.
Naturally, the analyst would want to know the probability that a  statistic
is truely above or below a given value. To help visualize these probabilities we
represent statistics using a bar chart. The user specifies a value to
compare the statistics to and each bar is shaded on a scale from blue to red
depending on the probability that the statistic lies above or below the
user-specified value.

Using MatPlotLib, this script generates simulated data and then outputs a bar
chart where the bars are shaded accoring to the probability that each statistic
is above or below y_val, a float to be specified by the user.
'''

#set value to compare:
y_val = 41000

np.random.seed(12345)

#simulated data
df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])


avgs = df.mean(axis = 1)
std_errs = df.sem(axis = 1)
error = 1.96*std_errs.values


plt.figure()
pos = np.arange(len(df.index.values))
my_cmap = plt.cm.get_cmap('bwr')

sm = ScalarMappable(cmap=my_cmap)
sm.set_array([])


for i in np.arange(len(df.index.values)):
    c = norm(loc=avgs.iloc[i], scale=std_errs.iloc[i]).cdf(y_val)
    plt.bar(pos[i], avgs.iloc[i], align='center',edgecolor = 'k',linewidth = 0.2, color=my_cmap(1-c),
            yerr = error[i],capsize = 10)

# soften all labels by turning grey
plt.xticks(pos, df.index.values, alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=True, left=True, right=False, labelleft=True, labelbottom=True)

# remove the frame of the chart
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

#put horizontal line in chart:
plt.axhline(y=y_val, color='k', linestyle='-')

plt.text(pos[-1]+0.45, y_val, "y-value="+str(y_val), size=6,
         ha="left", va="top",
         bbox=dict(boxstyle="square",
                    ec = 'k',
                    fc = 'w'
                   )
         )

plt.subplots_adjust(bottom=0.25, top=0.9)
cax = plt.axes([ 0.4, 0.125, 0.5, 0.05])

cbar = plt.colorbar(sm,ticks=[0,0.25, 0.5,0.75, 1], cax = cax, orientation = 'horizontal')
cbar.set_label('Probability that the statistic is greater than y-value')

plt.show()
