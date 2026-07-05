# RL Car Racing Agent
Project for CEAM WEEK 4 & 5 \
**TASK:** Build an autonomous racing agent capable of learning to navigate a simple 2D track.

## Project Overview
An Autonomous RL (Reinforcement Learning) Agent trained to navigate a 2D Racing Track using Gymnasium's Car-Racing-v3 environment via pixel inputs.

Reinforcement Learning is a method of training a Machine Learning model to make decisions through trial and error and then rewarding it for implementing the intended behavior. By the end of the training session, you get a reward policy which governs the agent's actions. Unlike Supervised learning where you train the model with a dataset, RL learns by doing. If it makes a mistake, it earns negative reward points and that teaches the model to avoid repeating that mistake.

**Basic RL Terminologies:**

* **State:** The current situation or condition of the agent within the environment
* **Action:** The moves or decisions the agent takes in response to a given state
* **Reward:** Feedback provided by the environment to evaluate the success of agent's actions
* **Agent:** The AI being trained
* **Environment:** The setting/world the agent interacts with (here its the race course)
* **Episode:** A single complete sequence of interactions between the agent and its environment (Similar to Epoch in a sense, for familiarity)
* **Exploration vs Exploitation:** : Exploitation is when the agent uses what it previously learnt was correct and doesn't try anything new. Exploration is like allowing the agent to experiment new things.
  

## Prerequisites
The project was built with Python 3

Modules used in this project are:
 * `gymnasium`
 * `stable_baselines3`
 * `PPO` (from `stable_baselines3`)

The play-it-yourself Car Game `car_racing_driver_strict.py` utilises these modules: 
* `gymnasium`
* `numpy`
* `pygame`

> The entire project uses the premade environment from Gymnasium called `CarRacing-v3`.

##




