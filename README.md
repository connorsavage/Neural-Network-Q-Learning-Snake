# Snake Application of Q-Learning
This project is a real-time demonstration of Q-learning using the classic game of Snake. In the video displayed below, you will watch an agent autonomously learn how to play the game through a neural network and reward system. The blue line in our graph represents the high score of each game iteration and the orange line represents the mean score of all iterations.

https://github.com/connorsavage/Neural-Network-Q-Learning-Snake/assets/75349013/37935327-a4ac-4f41-a9ae-fdfa83996da9

## Environment setup
Although you can setup your environment in any manner you'd like, the setup will be based on using Anaconda [Download Link](https://www.anaconda.com/download)

Follow the download instructions after downloading and ensure that within your Environment variables has a path to anaconda3 and anaconda3\Scripts

Create environment with `conda create -n (name of environment) python=3.7`

Activate environment with `conda init` followed by `conda activate (environment name)`
(make sure to activate environment within project folder to function properly)

## Downloading packages
After setting up and activating the environment, install the following packages using `pip install (package name)`

- pip install pygame
- pip install torch torchvision
- pip install matplotlib ipython

## To Run
In the terminal, run conda activate pygame_env, input `python agent.py` to run the AI. Two popups will appear: a window with the Snake game running and an updating graph illustrating the score, number of iterations, and Q-value.
