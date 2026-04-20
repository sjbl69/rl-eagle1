import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium.wrappers import RecordVideo

env = gym.make("LunarLander-v3", render_mode="rgb_array")

env = RecordVideo(
    env,
    video_folder="videos",
    episode_trigger=lambda e: True
)

model = PPO.load("model/ppo_final")

obs, _ = env.reset()
done = False
total_reward = 0

while not done:
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    total_reward += reward

env.close()

print("Reward:", total_reward)