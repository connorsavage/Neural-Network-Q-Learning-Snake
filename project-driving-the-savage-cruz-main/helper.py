"""
File Name: helper.py
Author: Connor Savage & Sebastian Cruz
Date Created: 11/21/2023
Last Modified: 11/29/2023
Description: Utility functions for displaying, plotting, and updating game metrics.
"""

import matplotlib.pyplot as plt
from IPython import display

plt.ion()

# Plot and update the scores and mean scores in real-time
def plot(scores, mean_scores):
    display.clear_output(wait=True) # Clear the previous plot
    display.display(plt.gcf()) # Display the current figure
    plt.clf() # Clear the current figure
    plt.title('Training...') # Set title
    plt.xlabel('Number of Games') # Set x-axis label
    plt.ylabel('Score') # Set y-axis label
    plt.plot(scores) # Plot scores
    plt.plot(mean_scores) # Plot mean scores
    plt.ylim(ymin=0) # Set minimum y value
    plt.text(len(scores)-1, scores[-1], str(scores[-1])) # Show latest score
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1])) # Show latest mean score
    plt.show(block=False) # Display plot without blocking execution
    plt.pause(.1) # Pause to update plot
