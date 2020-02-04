# Sample-oriented Data Visualization
This script implements a data visualization scheme proposed by Ferreira, Fisher
and König in the [article](https://dl.acm.org/doi/10.1145/2556288.2557131) 
"Sample-Oriented Task-Driven Visualizations: Allowing
Users to Make Better, More Confident Decisions," which is designed to help data
analysts make decisions with uncertain data.

For example, suppose that an analyst has statistical data from various years, but
perhaps the statistics were drawn from a sample instead of the entire data set.
Naturally, the analyst would want to know the probability that a  statistic
is truely above or below a given value. To help visualize these probabilities we
represent a series of statistics using a bar chart. The user specifies a value to
compare the statistics to and each bar is shaded on a blue/red scale
depending on the probability that the statistic lies above or below the
user-specified value.

Using MatPlotLib and NumPy, this Python script generates simulated data and then outputs a bar
chart (with confidence intervals) where the bars are shaded accoring to the probability that each statistic
is above or below y_val, a float to be specified by the user.
