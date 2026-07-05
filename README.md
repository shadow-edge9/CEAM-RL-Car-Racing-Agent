# RL Car Racing Agent
Project for CEAM WEEK 4 & 5 \
**TASK:** Build an autonomous racing agent capable of learning to navigate a simple 2D track.

## Project Overview
An Autonomous RL (Reinforcement Learning) Agent trained to navigate a 2D Racing Track using Gymnasium's Car-Racing-v3 environment via pixel inputs.

Reinforcement Learning is a method of training a Machine Learning model to make decisions through trial and error and then rewarding it for implementing the intended behavior. By the end of the training session, you get a reward policy which governs the agent's actions. Unlike Supervised Learning where you train the model with a dataset, RL is learning by doing. If it makes a mistake, it earns negative reward points and that teaches the model to avoid repeating that mistake.

**Basic RL Terminologies:**

* **State:** The current situation or condition of the agent within the environment
* **Action:** The moves or decisions the agent takes in response to a given state
* **Reward:** Feedback provided by the environment to evaluate the success of agent's actions
* **Agent:** The AI being trained
* **Environment:** The setting/world the agent interacts with (here its the race course)
* **Episode:** A single complete sequence of interactions between the agent and its environment (Similar to Epoch in a sense, for familiarity)
* **Exploration vs Exploitation:** : Exploitation is when the agent uses what it previously learnt was correct and doesn't try anything new. Exploration is like allowing the agent to experiment new things.

> NOTE: This isn't a 100% working model. The challenges and issues faced are mentioned below in Challenges.

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

> The entire project uses the premade environment from Gymnasium called `CarRacing-v3` with policy `CnnPolicy`

## How to Run the Project
To play the game and figure out the raw mechanics, run `car_racing_driver_strict.py` . \
To train the model, run `model_trainer.py` first to get a zip file. After that run `test.py`.
## Experimentation Phase

### TRIAL 1
Trial 1 was figuring things out. I initially gave it 10000 timesteps and let the model run naturally.
The result was that it randomly moved around, never on track.


<img width="800" height="588" alt="TRIAL1-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/40dafc3c-d601-44b3-a663-d99835407eb0" />

### TRIAL 2
Surprised by the amount of time it took to process it (I didn't know it would take that long), I tried to train it faster. 
* I changed `render_mode` to `None`
* Used `DummyVecEnv` to reduce transaltion overhead
* Used `VecFrameStack` for frame-shifting operations

But the result I got was far from perfect. It didn't follow the track. Moreover it began...spinning.
I'd increased the timesteps for better accuracy to 40000.

<img width="800" height="588" alt="1783269781532818-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/0bf61f28-0050-4b0a-b8f3-c7ea75801160" />

### TRIAL 3
In this third trial I tried to make a reward function but it failed spectacularly. The car didn't move at all, scared to even proceed. It stayed rooted to the spot the entire time. 
I gave it a -5 penalty for reckless spinning but it didn't work as intended, at 40000 timsteps.

<img width="800" height="588" alt="1783277551359263-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/e63a1f2a-39ce-43c1-bf86-91305ec7163c" />

## TRIAL 4
For this trial, I modified the reward function to have 20% gas at all times, hoping that would make it move. It worked until...it didn't. \
It spun off track, and began to perform donuts.\
I appreciate the skills, but that was NOT what I wanted at all. \
I even adjusted it to 10% gas to see if it will have some control but that failed as well.
Again thsi was at 40000 timesteps.

<img width="800" height="588" alt="TRIAL4-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/f4036b0a-ad9e-412e-9d31-6c6c7cc39f1e" />

Frustrated I decided to dig deeper and understand the raw physics of the environment I was dealing with. I knew the agents mistakes, but what actiosn exactly was it performing? \
To find that out I made the `car_racing_driver_strict.py` script. Its basically `CarRacing-v3` but in this one, **YOU** control the car with your arrow keys. I had fun racing it, and completed the course, simulating what the agent should actually aim for. \

My investigatiosn brought fruit. I found out it was stepping on gas after turning left or right, and then released the left or right keys, and simply did donuts, rooted to the spot. That was the exact combination of actions. (As can be seen in the gif)

<img width="800" height="656" alt="1783279196737938-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/8a25ebca-fba1-4fbc-9322-3f95281a6856" />

With this information in mind, I decided I'd have to ramp up the timesteps even more and 40000 wasn't enough. That lead to my 5th Trial.

### TRIAL 5
`model_trainer.py` is the final version as yet. The metrics are as follows: 

* `render_mode` = `None`
* `continuous` = `True`
* policy " `CnnPolicy`
* `batch_size` = 256
* `learning_rate` = 3e-4
* `ent_coef` = 0.01
* **Timesteps** = 500000

The model improved drastically, failing only at sharp turns. However, once the car spun off the track, it wasn't able to recover or get back on track, aimlessly spinning in circles. 

<img width="800" height="663" alt="1783283906000961-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/8dfdc201-e0eb-4b9d-bf64-4d607f501209" />


## Challenges
I made adjustments and tried to penalize it for spinning but that only results in the car not moving, again. Still working on improving the model. 









