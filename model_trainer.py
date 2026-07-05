import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv, VecFrameStack
from stable_baselines3.common.env_util import make_vec_env
import numpy as np

if __name__ == '__main__':

    env_train = make_vec_env("CarRacing-v3", n_envs=4, env_kwargs={"render_mode": None, "continuous": True}, vec_env_cls = SubprocVecEnv) #remove wrapper_class to revert to original

    env_train = VecFrameStack(env_train, n_stack=4)

    model = PPO("CnnPolicy", env_train, verbose=1, batch_size=256, learning_rate=3e-4, ent_coef=0.01)

    print("[INFO]: Training begins...")
    model.learn(total_timesteps=500000)

    model.save("car_racing_agent")
    print("Model Ready.")

    env_train.close()