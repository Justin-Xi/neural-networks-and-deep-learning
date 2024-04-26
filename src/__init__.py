from scipy.stats import binom

n_trials = 20  # Number of trials
p_success = 0.5  # Probability of success on each trial

# Calculate the cumulative probability for 13 or fewer successes
cumulative_probability_13 = binom.cdf(13, n_trials, p_success)
print(cumulative_probability_13)
