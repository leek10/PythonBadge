# Use a random number generator to make histograms of Binomial, Normal, and Uniform distributions using numpy and matplotlib
    # Note: the Binomial and Normal distributions should converge to the large N limit

import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)  # generates random numbers based on seed (in this case 42)

# Parameters for distributions
sample_size = 1000  # number of samples for each distribution

# Generate data for each distribution
# Binomial distribution (n = 20, p = 0.5)
binomial_data = np.random.binomial(n = 20, p = 0.5, size = sample_size) 
    # n = number of trials in each binomial experiment
    # p = probability of success

# Plotting the histogram for binomial distribution
plt.subplot(1, 3, 1)
    # first # = total unmber of rows in subplot grid
    # second # = total number of columns in subplot grid
    # third # = position of the subplot in the grid (i.e. this is the first plot in the grid of 3)
plt.hist(binomial_data, bins = 20, color = 'blue', alpha = 0.7)   
    # bins = intervals in whcih the data range is divided in the histogram
    # alpha = histogram opacity ranging from 0 (transparant) to 1 (opague)
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')


# Normal distribution (mean = 0, std = 1)
normal_data = np.random.normal(loc = 0, scale = 1, size = sample_size)
    # loc = center value of the normal distribution
    # scale = standard deviation (std) of the normal distribution

# Plotting the histogram for normal distribution
plt.subplot(1, 3, 2)
plt.hist(normal_data, bins = 20, color = 'green', alpha = 0.7)
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')


# Uniform distribution (between 0 and 1)
uniform_data = np.random.uniform(low = 0, high = 1, size = sample_size)
    # low = lower boundary of the uniform distribution
    # high = upper boundary of the uniform distribution

# Plotting the histogram for uniform distribution
plt.subplot(1, 3, 3)
plt.hist(uniform_data, bins = 20, color = 'orange', alpha = 0.7)
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot histograms
plt.figure(figsize = (15, 5))

# Adjust layout and display
plt.tight_layout()
plt.show()

