import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Charger environnement
env = gym.make("LunarLander-v3")

# Charger modèle PPO final
model = PPO.load("model/ppo_final")

# Évaluation
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=100
)

print(f"Mean reward: {mean_reward} +/- {std_reward}")