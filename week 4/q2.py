# Given data
sensitivity = 0.93
specificity = 0.88
prevalence = 0.03
non_breach_prob = 1 - prevalence

# Calculate P(Breach Detected)
p_breach_detected = (sensitivity * prevalence) + ((1 - specificity) * non_breach_prob)

# Apply Bayes' Theorem to calculate the posterior probability
p_actual_breach_given_detected = (sensitivity * prevalence) / p_breach_detected

# Print result
print(f"Probability of actual breach given breach detected: {p_actual_breach_given_detected:.4f}")

