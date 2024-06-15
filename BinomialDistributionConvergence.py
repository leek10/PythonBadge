# Show that the Binomial distribution converges to the large N limit

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters
p = 0.5  # probability of success
M = 1000  # number of simulations

# Different values of N (number of trials)
N_values = [10, 50, 100, 500]

# Generate random samples from Binomial distribution for each N
samples = {N: np.random.binomial(N, p, size=M) for N in N_values}

# Plotting setup
plt.figure(figsize=(12, 8))

# Plot histograms and compare with normal distribution
for i, N in enumerate(N_values):
    plt.subplot(2, 2, i + 1)
    plt.title(f'Binomial Distribution (N={N}) vs Normal Distribution')
    
    # Plot histogram of sampled data
    plt.hist(samples[N], bins=30, density=True, alpha=0.6, label=f'Binomial (N={N}) samples')
    
    # Calculate mean and variance of the Binomial distribution
    mean_binom = np.mean(samples[N])
    var_binom = np.var(samples[N])
    
    # Calculate parameters of the approximating Normal distribution
    mean_norm = N * p
    std_norm = np.sqrt(N * p * (1 - p))
    
    # Plot the Normal distribution approximation
    x = np.linspace(binom.ppf(0.01, N, p), binom.ppf(0.99, N, p), 100)
    plt.plot(x, norm.pdf(x, mean_norm, std_norm), 'r-', lw=2, label='Normal approx.')
    
    plt.legend()

plt.tight_layout()
plt.show()