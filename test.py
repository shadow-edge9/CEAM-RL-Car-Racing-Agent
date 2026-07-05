import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack

def make_env():
    return gym.make("CarRacing-v3", render_mode="human", continuous=True)

if __name__ == '__main__':
    print("Initializing evaluation track...")
    env_test = DummyVecEnv([make_env])
    env_test = VecFrameStack(env_test, n_stack=4)

    print("Loading trained model")
    model = PPO.load("car_racing_agent", env=env_test)

    obs = env_test.reset()
    print("Testing Phase Begins...")

    for step in range(2000):
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, infos = env_test.step(action)


    env_test.close()
    print("TESTING PHASE OVER.")

