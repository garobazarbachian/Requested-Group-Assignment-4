#!/usr/bin/env python
# coding: utf-8

# # Monte Carlo Simulation - Group: James, Garo, Manny

# ### Data Preparation
# 
# First, we will set up this notebook so that it will display multiple outputs for each cell if needed, as well as load the necessary libraries.

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[1]:


import random
import time
import math

def estimate_pi(num_samples):
    """Estimates the value of pi using a Monte Carlo method."""
    points_inside_circle = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point (x, y) is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
    
    # Estimate pi as the ratio of points inside the circle to total points, multiplied by 4
    pi_estimate = 4 * points_inside_circle / num_samples
    return pi_estimate

def main():
    sample_sizes = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    real_pi = math.pi
    
    for num_samples in sample_sizes:
        start_time = time.time()
        
        estimated_pi = estimate_pi(num_samples)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        error_percent = abs((estimated_pi - real_pi) / real_pi) * 100
        
        print(f"Samples: {num_samples}")
        print(f"Estimated value of pi: {estimated_pi:.100f}")
        print(f"Error percent: {error_percent:.10f}%")
        print(f"Elapsed time: {elapsed_time:.4f} seconds")
        print('-' * 60)

if __name__ == "__main__":
    main()

